from __future__ import annotations
from typing import List, Iterable, Any, Tuple
import numpy as np


def generate_latin_squares(values: List[Any]) -> Iterable[list[list[Any]]]:
    n = len(values)
    vals = list(values)
    if len(set(vals)) != n:
        raise ValueError("All entries in `values` must be distinct.")

    row_used = [[False] * n for _ in range(n)]
    col_used = [[False] * n for _ in range(n)]
    square: list[list[Any]] = [[None] * n for _ in range(n)]

    def backtrack(cell: int):
        if cell == n * n:
            yield [row[:] for row in square]
            return
        r, c = divmod(cell, n)
        for k, v in enumerate(vals):
            if not row_used[r][k] and not col_used[c][k]:
                square[r][c] = v
                row_used[r][k] = True
                col_used[c][k] = True
                yield from backtrack(cell + 1)
                row_used[r][k] = False
                col_used[c][k] = False
                square[r][c] = None

    return backtrack(0)


def maxplus_mul(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Max-plus matrix multiplication: (A ⊗ B)_{ij} = max_k (A_{ik} + B_{kj})."""
    if A.ndim != 2 or B.ndim != 2:
        raise ValueError("A dan B harus matriks 2D.")
    m, n = A.shape
    n2, p = B.shape
    if n != n2:
        raise ValueError("Dimensi tidak cocok: kolom(A) harus = baris(B).")
    # Broadcast addition then take max along k-axis
    C = np.max(A[:, :, None] + B[None, :, :], axis=1)
    return C


def is_latin_square_matrix(M: np.ndarray) -> bool:
    """Check if a numeric matrix is a Latin square (each row/col is a permutation of the symbol set)."""
    if M.ndim != 2:
        return False
    n, m = M.shape
    if n != m:
        return False
    symbols = np.unique(M)
    if symbols.size != n:
        return False
    symbol_set = set(symbols.tolist())
    for i in range(n):
        if set(M[i, :].tolist()) != symbol_set:
            return False
        if set(M[:, i].tolist()) != symbol_set:
            return False
    return True


def find_commutative_latin_pairs(matrices: List[np.ndarray], allow_self: bool = False) -> List[Tuple[np.ndarray, np.ndarray]]:
    """Find pairs (A, B) of Latin-square matrices that commute under max-plus multiplication.

    - If allow_self=False, only i < j (no (A,A) and no duplicates).
    - If allow_self=True, i <= j (allow (A,A), still no (B,A) separately).
    """
    result: List[Tuple[np.ndarray, np.ndarray]] = []
    n = len(matrices)
    for i in range(n):
        A = matrices[i]
        if not is_latin_square_matrix(A):
            continue
        start_j = i if allow_self else i + 1
        for j in range(start_j, n):
            B = matrices[j]
            if not is_latin_square_matrix(B):
                continue
            AB = maxplus_mul(A, B)
            BA = maxplus_mul(B, A)
            if np.array_equal(AB, BA):
                result.append((A, B))
    return result


def find_commutative_latin_pairs_two_sets(matrices1: List[np.ndarray], matrices2: List[np.ndarray]) -> List[Tuple[np.ndarray, np.ndarray]]:
    """Find commuting pairs (A, B) with A from matrices1 and B from matrices2 under max-plus multiplication."""
    result: List[Tuple[np.ndarray, np.ndarray]] = []
    for A in matrices1:
        if not is_latin_square_matrix(A):
            continue
        for B in matrices2:
            if not is_latin_square_matrix(B):
                continue
            AB = maxplus_mul(A, B)
            BA = maxplus_mul(B, A)
            if np.array_equal(AB, BA):
                result.append((A, B))
    return result


def analyze_commutative_pairs(values1: List[Any], values2: List[Any]) -> List[Tuple[np.ndarray, np.ndarray]]:
    """Generate Latin squares from two value sets and print/return max-plus commuting pairs."""
    latin_list1 = list(generate_latin_squares(values1))
    latin_list2 = list(generate_latin_squares(values2))
    matrices1 = [np.array(L, dtype=float) for L in latin_list1]
    matrices2 = [np.array(L, dtype=float) for L in latin_list2]
    pairs = find_commutative_latin_pairs_two_sets(matrices1, matrices2)

    print(f"Jumlah pasangan komutatif dari dua himpunan berbeda: {len(pairs)}")
    for idx, (A, B) in enumerate(pairs, start=1):
        print(f"Pasangan {idx}:")
        print(f"A (dari {values1}) =")
        print(A)
        print(f"B (dari {values2}) =")
        print(B)
        print("A * B =")
        print(maxplus_mul(A, B))
        print("-")

    return pairs


__all__ = [
    "generate_latin_squares",
    "maxplus_mul",
    "is_latin_square_matrix",
    "find_commutative_latin_pairs",
    "find_commutative_latin_pairs_two_sets",
    "analyze_commutative_pairs",
]
