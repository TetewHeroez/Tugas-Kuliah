from itertools import permutations
from time import perf_counter


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def is_latin_square(A):
    n = len(A)
    symbols = set(range(1, n + 1))
    return (
        all(set(row) == symbols for row in A)
        and all({A[r][c] for r in range(n)} == symbols for c in range(n))
    )


def maxplus_product(A, B):
    n = len(A)
    return tuple(
        tuple(max(A[r][t] + B[t][c] for t in range(n)) for c in range(n))
        for r in range(n)
    )


def is_commutative_pair(A, B):
    return maxplus_product(A, B) == maxplus_product(B, A)


def all_latin_squares(n):
    rows = list(permutations(range(1, n + 1)))
    columns = [set() for _ in range(n)]
    partial = []

    def backtrack():
        if len(partial) == n:
            yield tuple(partial)
            return

        for row in rows:
            if all(row[c] not in columns[c] for c in range(n)):
                partial.append(row)
                for c, value in enumerate(row):
                    columns[c].add(value)

                yield from backtrack()

                for c, value in enumerate(row):
                    columns[c].remove(value)
                partial.pop()

    yield from backtrack()


def build_permutation_context(n):
    perms = list(permutations(range(n)))
    perm_index = {p: i for i, p in enumerate(perms)}

    perm_masks = []
    for p in perms:
        mask = 0
        for r, c in enumerate(p):
            mask |= 1 << (r * n + c)
        perm_masks.append(mask)

    comp_index = [[0] * len(perms) for _ in perms]
    for a, p in enumerate(perms):
        for b, q in enumerate(perms):
            comp_index[a][b] = perm_index[compose(p, q)]

    commute = [[False] * len(perms) for _ in perms]
    for a in range(len(perms)):
        for b in range(len(perms)):
            commute[a][b] = comp_index[a][b] == comp_index[b][a]

    comp_masks = [
        [perm_masks[comp_index[a][b]] for b in range(len(perms))]
        for a in range(len(perms))
    ]

    return {
        "n": n,
        "perms": perms,
        "perm_index": perm_index,
        "perm_masks": perm_masks,
        "commute": commute,
        "comp_masks": comp_masks,
    }


def decompose_latin_square_indices(A, ctx):
    n = len(A)
    return {
        symbol: ctx["perm_index"][tuple(row.index(symbol) for row in A)]
        for symbol in range(1, n + 1)
    }


def matrix_from_sigma_indices(sigmas, ctx):
    n = ctx["n"]
    B = [[0] * n for _ in range(n)]
    for symbol, sigma_index in sigmas.items():
        for r, c in enumerate(ctx["perms"][sigma_index]):
            B[r][c] = symbol
    return tuple(tuple(row) for row in B)


def find_commuting_partners(A, ctx=None):
    A = tuple(tuple(row) for row in A)
    n = len(A)
    ctx = build_permutation_context(n) if ctx is None else ctx
    perms = ctx["perms"]
    perm_masks = ctx["perm_masks"]
    commute = ctx["commute"]
    comp_masks = ctx["comp_masks"]
    A_sigmas = decompose_latin_square_indices(A, ctx)
    partners = {}

    if all(
        commute[A_sigmas[i]][A_sigmas[j]]
        for i in range(1, n + 1)
        for j in range(1, n + 1)
    ):
        for pi in permutations(range(1, n + 1)):
            B_sigmas = {i: A_sigmas[pi[i - 1]] for i in range(1, n + 1)}
            partners[matrix_from_sigma_indices(B_sigmas, ctx)] = "alternatif"

    centralizer = [p for p in range(len(perms)) if commute[p][A_sigmas[n]]]
    B_grid = [[0] * n for _ in range(n)]
    B_sigmas = {}
    occupied_mask = 0

    def add_symbol(symbol, sigma_index):
        nonlocal occupied_mask
        B_sigmas[symbol] = sigma_index
        occupied_mask |= perm_masks[sigma_index]
        for r, c in enumerate(perms[sigma_index]):
            B_grid[r][c] = symbol

    def remove_symbol(symbol, sigma_index):
        nonlocal occupied_mask
        del B_sigmas[symbol]
        occupied_mask ^= perm_masks[sigma_index]
        for r, c in enumerate(perms[sigma_index]):
            B_grid[r][c] = 0

    def superlevel_equal(v):
        ab_mask = 0
        ba_mask = 0
        for i, sigma_i_A in A_sigmas.items():
            for j, sigma_j_B in B_sigmas.items():
                if i + j >= v:
                    ab_mask |= comp_masks[sigma_j_B][sigma_i_A]
                    ba_mask |= comp_masks[sigma_i_A][sigma_j_B]
        return ab_mask == ba_mask

    def remaining_sigma_for_symbol_one():
        sigma = []
        used_columns = set()
        for r in range(n):
            empty_columns = [c for c in range(n) if B_grid[r][c] == 0]
            if len(empty_columns) != 1 or empty_columns[0] in used_columns:
                return None
            sigma.append(empty_columns[0])
            used_columns.add(empty_columns[0])
        if len(used_columns) != n:
            return None
        return ctx["perm_index"][tuple(sigma)]

    def backtrack(m):
        if m == 1:
            sigma_1 = remaining_sigma_for_symbol_one()
            if sigma_1 is None:
                return
            B_sigmas[1] = sigma_1
            partners.setdefault(matrix_from_sigma_indices(B_sigmas, ctx), "umum")
            del B_sigmas[1]
            return

        v = n + m
        for sigma_index in range(len(perms)):
            if occupied_mask & perm_masks[sigma_index] == 0:
                add_symbol(m, sigma_index)
                if superlevel_equal(v):
                    backtrack(m - 1)
                remove_symbol(m, sigma_index)

    for tau in centralizer:
        add_symbol(n, tau)
        backtrack(n - 1)
        remove_symbol(n, tau)

    return list(partners.keys())


def validate_order(n, show_each=False):
    started = perf_counter()
    ctx = build_permutation_context(n)
    details = []
    total_partners = 0
    all_valid = True

    for index, A in enumerate(all_latin_squares(n), start=1):
        partners = find_commuting_partners(A, ctx)
        valid = all(is_latin_square(B) and is_commutative_pair(A, B) for B in partners)
        total_partners += len(partners)
        all_valid = all_valid and valid
        details.append(
            {
                "index": index,
                "A": A,
                "jumlah_pasangan": len(partners),
                "valid": valid,
                "pasangan": partners,
            }
        )

        if show_each:
            print(f"A ke-{index}: {len(partners)} pasangan, valid={valid}")

    summary = {
        "orde": n,
        "jumlah_latin_square": len(details),
        "total_pasangan_ditemukan": total_partners,
        "semua_valid": all_valid,
        "waktu_detik": round(perf_counter() - started, 3),
    }
    return summary, details


summary_orde_3, detail_orde_3 = validate_order(3, show_each=True)
summary_orde_3

summary_orde_4, detail_orde_4 = validate_order(4, show_each=True)
summary_orde_4

summary_orde_5, detail_orde_5 = validate_order(5, show_each=False)
summary_orde_5
