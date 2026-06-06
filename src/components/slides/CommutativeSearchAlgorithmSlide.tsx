"use client";

import { useMemo, useState } from "react";
import { motion } from "framer-motion";
import MathBlock from "@/components/ui/MathBlock";

const headingClass = "font-[family:var(--font-heading)]";
const item = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] as const },
  },
};

const container = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { staggerChildren: 0.14, delayChildren: 0.1 },
  },
};

type CellValue = 1 | 2 | 3 | 4;
type MatrixValue = CellValue | ".";
type Matrix = readonly (readonly MatrixValue[])[];
type EditableMatrix = CellValue[][];
type Permutation = readonly [1 | 2 | 3 | 4, 1 | 2 | 3 | 4, 1 | 2 | 3 | 4, 1 | 2 | 3 | 4];
type SymbolStep = 4 | 3 | 2;

const defaultA: EditableMatrix = [
  [1, 2, 3, 4],
  [2, 1, 4, 3],
  [3, 4, 1, 2],
  [4, 3, 2, 1],
];

const stepsMeta = [
  {
    id: "start",
    short: "1",
    title: "Mulai dari matriks kandidat B*",
    focus: "Kerangka awal",
    note: "Pencarian dimulai dari B* yang masih kosong. Yang ditetapkan dulu adalah data dari A dan kandidat permutasi yang boleh dipakai untuk membangun B.",
  },
  {
    id: "sigma4",
    short: "2",
    title: "Pilih posisi simbol maksimum",
    focus: "Tentukan sigma_4^B",
    note: "Untuk simbol maksimum, kandidatnya datang dari centralizer. Jadi sigma_4^B tidak dipilih acak, tetapi dibatasi oleh permutasi yang komutatif dengan sigma_4^A.",
    formula: "\\sigma_4^B",
  },
  {
    id: "sigma3",
    short: "3",
    title: "Tambahkan simbol berikutnya",
    focus: "Tentukan sigma_3^B",
    note: "Sesudah sigma_4^B dipilih, algoritma mencari sigma_3^B yang masih mungkin dan kemudian memeriksa level tertinggi yang relevan.",
    formula: "\\mathcal{U}_{\\ge 7}^{AB} = \\mathcal{U}_{\\ge 7}^{BA}",
  },
  {
    id: "sigma2",
    short: "4",
    title: "Lanjutkan satu simbol lagi",
    focus: "Tentukan sigma_2^B",
    note: "Di tahap ini B* sudah hampir lengkap. Pemilihan sigma_2^B juga dibatasi oleh posisi yang tersisa dan oleh pemeriksaan superlevel berikutnya.",
    formula: "\\mathcal{U}_{\\ge 6}^{AB} = \\mathcal{U}_{\\ge 6}^{BA}",
  },
  {
    id: "finish",
    short: "5",
    title: "Dari B* menjadi B",
    focus: "Lengkapi simbol 1",
    note: "Kalau semua pilihan sebelumnya lolos, posisi yang tersisa otomatis menentukan simbol 1. Pada titik ini kandidat parsial B* berubah menjadi Latin square penuh B.",
    formula: "B",
  },
] as const;

const allPermutations: Permutation[] = (() => {
  const base = [1, 2, 3, 4] as const;
  const result: Permutation[] = [];

  const build = (prefix: number[], rest: number[]) => {
    if (rest.length === 0) {
      result.push(prefix as Permutation);
      return;
    }

    rest.forEach((value, index) => {
      build(
        [...prefix, value],
        [...rest.slice(0, index), ...rest.slice(index + 1)],
      );
    });
  };

  build([], [...base]);
  return result;
})();

function permutationToTex(perm: Permutation) {
  const visited = new Set<number>();
  const cycles: string[] = [];

  for (let start = 1; start <= 4; start += 1) {
    if (visited.has(start)) continue;

    const cycle: number[] = [];
    let current = start;

    while (!visited.has(current)) {
      visited.add(current);
      cycle.push(current);
      current = perm[current - 1];
    }

    cycles.push(`(${cycle.join("\\ ")})`);
  }

  return cycles.join("");
}

function matrixToSigma4(matrix: EditableMatrix): Permutation | null {
  const columns: number[] = [];
  const seenCols = new Set<number>();

  for (let row = 0; row < 4; row += 1) {
    const matches = matrix[row]
      .map((value, col) => ({ value, col }))
      .filter((entry) => entry.value === 4);

    if (matches.length !== 1) return null;

    const colIndex = matches[0].col + 1;
    if (seenCols.has(colIndex)) return null;
    seenCols.add(colIndex);
    columns.push(colIndex);
  }

  return seenCols.size === 4 ? (columns as Permutation) : null;
}

function composePermutations(left: Permutation, right: Permutation): Permutation {
  return right.map((value) => left[value - 1]) as Permutation;
}

function centralizerOf(perm: Permutation): Permutation[] {
  return allPermutations.filter((candidate) => {
    const ab = composePermutations(perm, candidate);
    const ba = composePermutations(candidate, perm);
    return ab.every((value, index) => value === ba[index]);
  });
}

function placementsFromSelected(
  selected: Partial<Record<SymbolStep, Permutation | null>>,
) {
  const placements = new Map<number, Map<number, CellValue>>();

  ([4, 3, 2] as const).forEach((symbol) => {
    const perm = selected[symbol];
    if (!perm) return;

    for (let row = 0; row < 4; row += 1) {
      if (!placements.has(row)) placements.set(row, new Map());
      placements.get(row)!.set(perm[row] - 1, symbol);
    }
  });

  return placements;
}

function candidatePermutations(
  selected: Partial<Record<SymbolStep, Permutation | null>>,
) {
  const placements = placementsFromSelected(selected);

  return allPermutations.filter((perm) => {
    for (let row = 0; row < 4; row += 1) {
      const col = perm[row] - 1;
      const occupied = placements.get(row)?.has(col);
      if (occupied) return false;
    }
    return true;
  });
}

function buildPartialMatrix(
  selected: Partial<Record<SymbolStep, Permutation | null>>,
  visibleSymbols: number[],
): Matrix {
  const board: MatrixValue[][] = Array.from({ length: 4 }, () =>
    Array(4).fill("."),
  );

  visibleSymbols.forEach((symbol) => {
    const perm = selected[symbol as SymbolStep];
    if (!perm) return;

    for (let row = 0; row < 4; row += 1) {
      board[row][perm[row] - 1] = symbol as CellValue;
    }
  });

  return board;
}

function completeMatrix(
  selected: Partial<Record<SymbolStep, Permutation | null>>,
): Matrix {
  const board: MatrixValue[][] = buildPartialMatrix(selected, [4, 3, 2]).map(
    (row) => [...row],
  );

  for (let row = 0; row < 4; row += 1) {
    for (let col = 0; col < 4; col += 1) {
      if (board[row][col] === ".") {
        board[row][col] = 1;
      }
    }
  }

  return board;
}

function MatrixPreview({
  matrix,
  editable = false,
  onCellClick,
  highlightValue,
}: {
  matrix: Matrix | EditableMatrix;
  editable?: boolean;
  onCellClick?: (row: number, col: number) => void;
  highlightValue?: number | null;
}) {
  const columns = matrix[0]?.length ?? 1;

  return (
    <div
      className="grid overflow-hidden rounded-xl border border-stone-300 bg-white"
      style={{ gridTemplateColumns: `repeat(${columns}, minmax(0, 1fr))` }}
    >
      {matrix.flatMap((row, rowIndex) =>
        row.map((value, colIndex) => {
          const isEmpty = value === ".";
          const isHighlighted = highlightValue !== null && value === highlightValue;
          const baseClass = isEmpty
            ? "bg-stone-50 text-stone-300"
            : isHighlighted
              ? "bg-amber-100 text-amber-950 ring-1 ring-amber-400"
              : "bg-emerald-50 text-stone-900";

          const className = [
            "flex h-11 w-11 items-center justify-center border border-stone-200 text-sm font-semibold transition-colors sm:h-12 sm:w-12 sm:text-base",
            baseClass,
            editable ? "cursor-pointer hover:bg-stone-100" : "",
          ].join(" ");

          if (editable && onCellClick) {
            return (
              <button
                key={`${rowIndex}-${colIndex}`}
                type="button"
                onClick={() => onCellClick(rowIndex, colIndex)}
                className={className}
              >
                {value}
              </button>
            );
          }

          return (
            <div key={`${rowIndex}-${colIndex}`} className={className}>
              {value}
            </div>
          );
        }),
      )}
    </div>
  );
}

function PermutationChoices({
  title,
  candidates,
  activeIndex,
  onSelect,
}: {
  title: string;
  candidates: Permutation[];
  activeIndex: number;
  onSelect: (index: number) => void;
}) {
  if (candidates.length === 0) {
    return (
      <div className="rounded-2xl border border-dashed border-stone-300 bg-stone-50 px-5 py-4 text-sm leading-relaxed text-stone-500">
        Belum ada kandidat yang bisa dipilih di tahap ini.
      </div>
    );
  }

  return (
    <div className="space-y-3">
      <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
        {title}
      </p>
      <div className="grid gap-3 sm:grid-cols-2">
        {candidates.map((candidate, index) => {
          const isActive = index === activeIndex;
          return (
            <button
              key={`${title}-${candidate.join("-")}`}
              type="button"
              onClick={() => onSelect(index)}
              className={[
                "rounded-2xl border px-4 py-3 text-left transition-colors",
                isActive
                  ? "border-amber-500 bg-amber-500 text-white"
                  : "border-stone-300 bg-white text-stone-700 hover:border-amber-400 hover:text-stone-950",
              ].join(" ")}
            >
              <div className="overflow-x-auto [scrollbar-width:none] [-ms-overflow-style:none] [&::-webkit-scrollbar]:hidden">
                <MathBlock
                  tex={permutationToTex(candidate)}
                  className={isActive ? "text-white" : "text-stone-900"}
                />
              </div>
            </button>
          );
        })}
      </div>
    </div>
  );
}

export default function CommutativeSearchAlgorithmSlide() {
  const [matrixA, setMatrixA] = useState<EditableMatrix>(defaultA);

  const sigma4A = useMemo(() => matrixToSigma4(matrixA), [matrixA]);
  const sigma4Candidates = useMemo(
    () => (sigma4A ? centralizerOf(sigma4A) : []),
    [sigma4A],
  );

  const [sigma4Index, setSigma4Index] = useState(0);
  const sigma4B = sigma4Candidates[sigma4Index] ?? null;

  const sigma3Candidates = useMemo(
    () =>
      sigma4B
        ? candidatePermutations({ 4: sigma4B })
        : [],
    [sigma4B],
  );
  const [sigma3Index, setSigma3Index] = useState(0);
  const sigma3B = sigma3Candidates[sigma3Index] ?? null;

  const sigma2Candidates = useMemo(
    () =>
      sigma4B && sigma3B
        ? candidatePermutations({ 4: sigma4B, 3: sigma3B })
        : [],
    [sigma4B, sigma3B],
  );
  const [sigma2Index, setSigma2Index] = useState(0);
  const sigma2B = sigma2Candidates[sigma2Index] ?? null;

  const selectedPermutations = useMemo(
    () => ({ 4: sigma4B, 3: sigma3B, 2: sigma2B }),
    [sigma4B, sigma3B, sigma2B],
  );

  const stepMatrices = useMemo(
    () => ({
      start: buildPartialMatrix(selectedPermutations, []),
      sigma4: buildPartialMatrix(selectedPermutations, [4]),
      sigma3: buildPartialMatrix(selectedPermutations, [4, 3]),
      sigma2: buildPartialMatrix(selectedPermutations, [4, 3, 2]),
      finish: completeMatrix(selectedPermutations),
    }),
    [selectedPermutations],
  );

  const handleEditA = (row: number, col: number) => {
    setMatrixA((current) =>
      current.map((currentRow, rowIndex) =>
        currentRow.map((value, colIndex) => {
          if (rowIndex !== row || colIndex !== col) return value as CellValue;
          return ((value % 4) + 1) as CellValue;
        }),
      ),
    );
    setSigma4Index(0);
    setSigma3Index(0);
    setSigma2Index(0);
  };

  const resetFollowing = (step: SymbolStep) => {
    if (step === 4) {
      setSigma3Index(0);
      setSigma2Index(0);
    }
    if (step === 3) {
      setSigma2Index(0);
    }
  };

  return (
    <div className="w-full min-h-dvh px-4 pb-24 pt-24 sm:px-6">
      <motion.div
        variants={container}
        initial="hidden"
        animate="visible"
        className="mx-auto flex w-full max-w-5xl flex-col gap-6"
      >
        <motion.div variants={item} className="space-y-2 text-center">
          <p className="text-xs font-bold uppercase tracking-widest text-amber-600">
            Prosedur Konstruksi
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Pencarian dimulai dari A, memilih permutasi kandidat, lalu membangun B* sampai B.
          </h2>
          <p className="mx-auto max-w-4xl text-left text-sm leading-relaxed text-stone-600">
            Jadi bukan cuma sigma_4^B yang punya pilihan. Setelah centralizer
            memberi kandidat awal, simbol berikutnya juga punya opsi permutasi
            sendiri yang masih mungkin, lalu disaring lagi oleh pemeriksaan
            level superlevel.
          </p>
        </motion.div>

        <motion.div
          variants={item}
          className="grid gap-5 rounded-[1.75rem] border border-stone-200 bg-white p-5 shadow-sm lg:grid-cols-[minmax(0,0.78fr)_minmax(0,1.22fr)]"
        >
          <div className="space-y-4">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
                Latin Square A
              </p>
              <p className="mt-2 text-sm leading-relaxed text-stone-600">
                Klik sel untuk mengganti simbol. Yang dibaca di sini adalah
                posisi simbol 4 pada A.
              </p>
            </div>

            <div className="flex justify-center">
              <MatrixPreview
                matrix={matrixA}
                editable
                onCellClick={handleEditA}
                highlightValue={4}
              />
            </div>

            <div className="rounded-2xl border border-stone-200 bg-stone-50 px-4 py-5">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
                Sigma maksimum dari A
              </p>
              {sigma4A ? (
                <div className="mt-3 overflow-x-auto [scrollbar-width:none] [-ms-overflow-style:none] [&::-webkit-scrollbar]:hidden">
                  <MathBlock
                    tex={`\\sigma_4^A = ${permutationToTex(sigma4A)}`}
                    display
                    className="text-stone-950"
                  />
                </div>
              ) : (
                <p className="mt-3 text-sm leading-relaxed text-rose-700">
                  Supaya sigma_4^A valid, setiap baris dan kolom harus punya
                  tepat satu angka 4.
                </p>
              )}
            </div>
          </div>

          <div className="space-y-4">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
                Kandidat permutasi yang sedang dipakai
              </p>
              <p className="mt-2 text-sm leading-relaxed text-stone-600">
                Yang aku tampilkan di sini bukan tebakan acak. Algoritma
                memilih kandidat per tahap: sigma_4^B dari centralizer, lalu
                sigma_3^B dan sigma_2^B dari permutasi yang masih muat di B*
                sambil dicek di level U&gt;=7 dan U&gt;=6.
              </p>
            </div>

            {sigma4A ? (
              <>
                <div className="rounded-2xl border border-amber-200 bg-amber-50 px-4 py-5">
                  <p className="text-xs font-bold uppercase tracking-[0.24em] text-amber-700">
                    Centralizer kandidat awal
                  </p>
                  <div className="mt-3 overflow-x-auto [scrollbar-width:none] [-ms-overflow-style:none] [&::-webkit-scrollbar]:hidden">
                    <MathBlock
                      tex={"C_{S_4}(\\sigma_4^A)"}
                      display
                      className="text-amber-950 [&_.katex-display]:my-0"
                    />
                  </div>
                </div>

                <div className="space-y-3 rounded-2xl border border-stone-200 bg-stone-50 px-4 py-5">
                  <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
                    Pilihan aktif saat ini
                  </p>

                  <div className="space-y-3">
                    <div className="rounded-2xl border border-white/80 bg-white px-4 py-4">
                      <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-500">
                        Sigma 4
                      </p>
                      <MathBlock
                        tex={
                          sigma4B
                            ? `\\sigma_4^B = ${permutationToTex(sigma4B)}`
                            : "\\sigma_4^B"
                        }
                        display
                        className="text-stone-950 [&_.katex-display]:my-1"
                      />
                    </div>

                    <div className="rounded-2xl border border-white/80 bg-white px-4 py-4">
                      <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-500">
                        Sigma 3
                      </p>
                      <MathBlock
                        tex={
                          sigma3B
                            ? `\\sigma_3^B = ${permutationToTex(sigma3B)}`
                            : "\\sigma_3^B"
                        }
                        display
                        className="text-stone-950 [&_.katex-display]:my-1"
                      />
                    </div>

                    <div className="rounded-2xl border border-white/80 bg-white px-4 py-4">
                      <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-500">
                        Sigma 2
                      </p>
                      <MathBlock
                        tex={
                          sigma2B
                            ? `\\sigma_2^B = ${permutationToTex(sigma2B)}`
                            : "\\sigma_2^B"
                        }
                        display
                        className="text-stone-950 [&_.katex-display]:my-1"
                      />
                    </div>
                  </div>
                </div>
              </>
            ) : (
              <div className="rounded-2xl border border-dashed border-stone-300 bg-stone-50 px-5 py-4 text-sm leading-relaxed text-stone-500">
                Centralizer dan kandidat berikutnya baru bisa ditampilkan
                setelah posisi simbol 4 pada A membentuk permutasi yang valid.
              </div>
            )}
          </div>
        </motion.div>

        <motion.div variants={item} className="space-y-3">
          {stepsMeta.map((step, index) => (
            <details
              key={step.id}
              open={index === 0}
              className="group rounded-lg border border-stone-200 bg-white shadow-sm open:border-emerald-400"
            >
              <summary className="flex cursor-pointer list-none items-start justify-between gap-4 px-5 py-4">
                <div className="flex items-start gap-4 text-left">
                  <span className="mt-0.5 flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-amber-500 text-sm font-bold text-white">
                    {step.short}
                  </span>
                  <div className="space-y-2">
                    <p className="text-xs font-bold uppercase tracking-[0.24em] text-emerald-700">
                      {step.focus}
                    </p>
                    <div>
                      <p className="text-lg font-bold text-stone-950">
                        {step.title}
                      </p>
                      <p className="mt-1 text-sm leading-relaxed text-stone-600">
                        {step.note}
                      </p>
                    </div>
                  </div>
                </div>
                <span className="mt-1 shrink-0 text-xl font-semibold text-stone-400 transition-transform duration-200 group-open:rotate-45 group-open:text-emerald-700">
                  +
                </span>
              </summary>

              <div className="border-t border-stone-200 px-5 py-5">
                <div className="grid gap-5 md:grid-cols-[minmax(0,0.85fr)_minmax(0,1.15fr)] md:items-start">
                  <div className="flex justify-center">
                    <MatrixPreview
                      matrix={stepMatrices[step.id as keyof typeof stepMatrices]}
                    />
                  </div>

                  <div className="space-y-4">
                    {step.id === "sigma4" && sigma4B ? (
                      <>
                        <div className="rounded-2xl border border-stone-200 bg-stone-50 px-4 py-5">
                          <MathBlock
                            tex={`\\sigma_4^B = ${permutationToTex(sigma4B)}`}
                            display
                            className="text-stone-950"
                          />
                        </div>
                        <div className="space-y-4 rounded-2xl border border-amber-200 bg-amber-50 px-4 py-5">
                          <div className="space-y-2">
                            <p className="text-xs font-bold uppercase tracking-[0.24em] text-amber-700">
                              Penyaring tahap ini
                            </p>
                            <p className="text-sm leading-relaxed text-amber-950">
                              Langkah pertama memang ditentukan dari
                              centralizer. Jadi semua tombol di bawah adalah
                              kandidat yang komutatif dengan sigma_4^A.
                            </p>
                          </div>
                          <div className="overflow-x-auto [scrollbar-width:none] [-ms-overflow-style:none] [&::-webkit-scrollbar]:hidden">
                            <MathBlock
                              tex={"C_{S_4}(\\sigma_4^A)"}
                              display
                              className="text-amber-950 [&_.katex-display]:my-0"
                            />
                          </div>
                          <PermutationChoices
                            title="Pilih sigma_4^B"
                            candidates={sigma4Candidates}
                            activeIndex={sigma4Index}
                            onSelect={(index) => {
                              setSigma4Index(index);
                              resetFollowing(4);
                            }}
                          />
                        </div>
                      </>
                    ) : null}

                    {step.id === "sigma3" && sigma3B ? (
                      <>
                        <div className="rounded-2xl border border-stone-200 bg-stone-50 px-4 py-5">
                          <MathBlock
                            tex={`\\sigma_3^B = ${permutationToTex(sigma3B)}`}
                            display
                            className="text-stone-950"
                          />
                        </div>
                        <div className="space-y-4 rounded-2xl border border-sky-200 bg-sky-50 px-4 py-5">
                          <div className="space-y-2">
                            <p className="text-xs font-bold uppercase tracking-[0.24em] text-sky-700">
                              Penyaring tahap ini
                            </p>
                            <p className="text-sm leading-relaxed text-sky-950">
                              Sesudah sigma_4^B dipasang, algoritma tidak bebas
                              memilih sigma_3^B. Tombol di bawah hanya memuat
                              permutasi yang masih bisa ditempatkan pada sel
                              kosong B*, lalu cabang aktif dibaca bersamaan
                              dengan pemeriksaan level U&gt;=7.
                            </p>
                          </div>
                          <PermutationChoices
                            title="Pilih sigma_3^B setelah cek U>=7"
                            candidates={sigma3Candidates}
                            activeIndex={sigma3Index}
                            onSelect={(index) => {
                              setSigma3Index(index);
                              resetFollowing(3);
                            }}
                          />
                        </div>
                      </>
                    ) : null}

                    {step.id === "sigma2" && sigma2B ? (
                      <>
                        <div className="rounded-2xl border border-stone-200 bg-stone-50 px-4 py-5">
                          <MathBlock
                            tex={`\\sigma_2^B = ${permutationToTex(sigma2B)}`}
                            display
                            className="text-stone-950"
                          />
                        </div>
                        <div className="space-y-4 rounded-2xl border border-emerald-200 bg-emerald-50 px-4 py-5">
                          <div className="space-y-2">
                            <p className="text-xs font-bold uppercase tracking-[0.24em] text-emerald-700">
                              Penyaring tahap ini
                            </p>
                            <p className="text-sm leading-relaxed text-emerald-950">
                              Di tahap berikutnya, opsi makin sempit lagi.
                              Tombol yang tersisa adalah permutasi untuk
                              sigma_2^B yang tidak menabrak posisi simbol 4 dan
                              3, lalu divisualisasikan bersama cek level
                              U&gt;=6.
                            </p>
                          </div>
                          <PermutationChoices
                            title="Pilih sigma_2^B setelah cek U>=6"
                            candidates={sigma2Candidates}
                            activeIndex={sigma2Index}
                            onSelect={setSigma2Index}
                          />
                        </div>
                      </>
                    ) : null}

                    {step.formula ? (
                      <div className="rounded-2xl border border-sky-200 bg-sky-50 px-4 py-5">
                        <MathBlock
                          tex={step.formula}
                          display
                          className="text-sky-950"
                        />
                      </div>
                    ) : null}

                    <div className="rounded-2xl border border-emerald-200 bg-emerald-50 px-5 py-4">
                      <p className="text-xs font-bold uppercase tracking-[0.24em] text-emerald-700">
                        Cara membacanya
                      </p>
                      <p className="mt-3 text-sm leading-relaxed text-emerald-950">
                        {step.id === "start"
                          ? "B* masih kosong. Yang diputuskan baru data dari A dan kumpulan kandidat permutasi yang boleh dipakai."
                          : step.id === "sigma4"
                            ? "Di sini algoritma benar-benar memakai centralizer untuk menentukan opsi awal sigma_4^B."
                            : step.id === "sigma3"
                              ? "Sesudah sigma_4^B dipilih, sigma_3^B punya beberapa opsi lagi. Yang divisualisasikan di sini adalah cabang yang sedang aktif."
                              : step.id === "sigma2"
                                ? "Tahap ini juga tidak tunggal. Opsi sigma_2^B yang masih mungkin ditentukan dari posisi tersisa dan pemeriksaan level berikutnya."
                                : "Setelah sigma_4^B, sigma_3^B, dan sigma_2^B dipilih, simbol 1 tinggal mengisi posisi yang tersisa sehingga B terbentuk penuh."}
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </details>
          ))}
        </motion.div>
      </motion.div>
    </div>
  );
}
