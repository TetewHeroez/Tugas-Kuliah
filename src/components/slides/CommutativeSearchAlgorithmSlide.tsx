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

const defaultA: EditableMatrix = [
  [1, 2, 3, 4],
  [2, 1, 4, 3],
  [3, 4, 1, 2],
  [4, 3, 2, 1],
];

const baseSteps = [
  {
    id: "start",
    short: "1",
    title: "Mulai dari matriks kandidat B*",
    focus: "Kerangka awal",
    note: "Kita mulai dari B* yang masih kosong. Algoritma belum mengisi apa-apa, tetapi struktur pencariannya sudah siap.",
  },
  {
    id: "sigma4",
    short: "2",
    title: "Pilih posisi simbol maksimum",
    focus: "Tentukan sigma_4^B",
    note: "Dari centralizer inilah kandidat awal untuk sigma_4^B dipilih. Begitu satu kandidat dipilih, posisi semua angka 4 pada B* langsung terbentuk.",
  },
  {
    id: "sigma3",
    short: "3",
    title: "Tambahkan simbol berikutnya dan cek level",
    focus: "Isi simbol 3",
    note: "Simbol 3 mulai dimasukkan ke posisi yang masih mungkin. Setelah itu pemeriksaan level tinggi bisa menolak cabang yang sudah tidak konsisten.",
    formula: "\\mathcal{U}_{\\ge 7}^{AB} = \\mathcal{U}_{\\ge 7}^{BA}",
  },
  {
    id: "sigma2",
    short: "4",
    title: "Lengkapi B* sedikit demi sedikit",
    focus: "Isi simbol 2",
    note: "Jika level sebelumnya lolos, bentuk B* makin lengkap. Di tahap ini biasanya struktur Latin square-nya sudah mulai terlihat jelas.",
    formula: "\\mathcal{U}_{\\ge 6}^{AB} = \\mathcal{U}_{\\ge 6}^{BA}",
  },
  {
    id: "finish",
    short: "5",
    title: "Dari B* menjadi B",
    focus: "Isi simbol 1",
    note: "Kalau semua pemeriksaan lolos, sel yang tersisa diisi simbol 1. Kandidat parsial B* pun berubah menjadi Latin square penuh B.",
    formula: "B",
  },
] as const;

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

  if (seenCols.size !== 4) return null;
  return columns as Permutation;
}

function composePermutations(left: Permutation, right: Permutation): Permutation {
  return right.map((value) => left[value - 1]) as Permutation;
}

function centralizerOf(perm: Permutation): Permutation[] {
  const nums = [1, 2, 3, 4] as const;
  const result: Permutation[] = [];

  const build = (prefix: number[], rest: number[]) => {
    if (rest.length === 0) {
      const candidate = prefix as Permutation;
      const ab = composePermutations(perm, candidate);
      const ba = composePermutations(candidate, perm);
      if (ab.every((value, index) => value === ba[index])) {
        result.push(candidate);
      }
      return;
    }

    rest.forEach((value, index) => {
      const nextRest = [...rest.slice(0, index), ...rest.slice(index + 1)];
      build([...prefix, value], nextRest);
    });
  };

  build([], [...nums]);
  return result;
}

function solveLatinSquareWithFixedFours(perm: Permutation): EditableMatrix | null {
  const board: number[][] = Array.from({ length: 4 }, () => Array(4).fill(0));
  const rowUsed = Array.from({ length: 4 }, () => new Set<number>());
  const colUsed = Array.from({ length: 4 }, () => new Set<number>());

  for (let row = 0; row < 4; row += 1) {
    const col = perm[row] - 1;
    board[row][col] = 4;
    rowUsed[row].add(4);
    colUsed[col].add(4);
  }

  const empties: Array<[number, number]> = [];
  for (let row = 0; row < 4; row += 1) {
    for (let col = 0; col < 4; col += 1) {
      if (board[row][col] === 0) empties.push([row, col]);
    }
  }

  const backtrack = (index: number): boolean => {
    if (index >= empties.length) return true;
    const [row, col] = empties[index];

    for (const candidate of [1, 2, 3, 4] as const) {
      if (rowUsed[row].has(candidate) || colUsed[col].has(candidate)) {
        continue;
      }

      board[row][col] = candidate;
      rowUsed[row].add(candidate);
      colUsed[col].add(candidate);

      if (backtrack(index + 1)) return true;

      board[row][col] = 0;
      rowUsed[row].delete(candidate);
      colUsed[col].delete(candidate);
    }

    return false;
  };

  return backtrack(0) ? (board as EditableMatrix) : null;
}

function maskMatrix(matrix: EditableMatrix, visibleSymbols: number[]): Matrix {
  return matrix.map((row) =>
    row.map((value) => (visibleSymbols.includes(value) ? value : ".")),
  );
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

export default function CommutativeSearchAlgorithmSlide() {
  const [matrixA, setMatrixA] = useState<EditableMatrix>(defaultA);

  const sigma4A = useMemo(() => matrixToSigma4(matrixA), [matrixA]);
  const centralizerCandidates = useMemo(
    () => (sigma4A ? centralizerOf(sigma4A) : []),
    [sigma4A],
  );

  const [selectedCandidateIndex, setSelectedCandidateIndex] = useState(0);
  const selectedCandidate =
    centralizerCandidates[selectedCandidateIndex] ?? null;

  const completedB = useMemo(
    () => (selectedCandidate ? solveLatinSquareWithFixedFours(selectedCandidate) : null),
    [selectedCandidate],
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
    setSelectedCandidateIndex(0);
  };

  const steps = useMemo(() => {
    const partialB = completedB
      ? {
          start: maskMatrix(completedB, []),
          sigma4: maskMatrix(completedB, [4]),
          sigma3: maskMatrix(completedB, [3, 4]),
          sigma2: maskMatrix(completedB, [2, 3, 4]),
          finish: completedB as Matrix,
        }
      : {
          start: maskMatrix(defaultA, []),
          sigma4: maskMatrix(defaultA, []),
          sigma3: maskMatrix(defaultA, []),
          sigma2: maskMatrix(defaultA, []),
          finish: maskMatrix(defaultA, []),
        };

    return baseSteps.map((step) => ({
      ...step,
      matrix: partialB[step.id as keyof typeof partialB],
    }));
  }, [completedB]);

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
            Pencarian dimulai dari A, memilih centralizer, lalu membangun B* sampai B.
          </h2>
          <p className="mx-auto max-w-4xl text-left text-sm leading-relaxed text-stone-600">
            Di slide ini A bisa diubah langsung. Posisi simbol 4 pada A akan
            menentukan <span className="font-semibold text-stone-800">sigma_4^A</span>,
            lalu centralizer-nya menjadi sumber kandidat awal untuk{" "}
            <span className="font-semibold text-stone-800">sigma_4^B</span>.
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
                Klik sel untuk mengganti simbol. Yang dibaca untuk centralizer
                di sini adalah posisi simbol 4.
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
                  Supaya sigma_4^A terbaca, setiap baris dan kolom harus punya
                  tepat satu angka 4.
                </p>
              )}
            </div>
          </div>

          <div className="space-y-4">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
                Pilih kandidat dari centralizer
              </p>
              <p className="mt-2 text-sm leading-relaxed text-stone-600">
                Tiap pilihan centralizer memberi alur pembentukan B* yang
                berbeda, lalu berujung ke Latin square B yang berbeda juga.
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

                <div className="grid gap-3 sm:grid-cols-2">
                  {centralizerCandidates.map((candidate, index) => {
                    const isActive = index === selectedCandidateIndex;
                    return (
                      <button
                        key={`${candidate.join("-")}`}
                        type="button"
                        onClick={() => setSelectedCandidateIndex(index)}
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
              </>
            ) : (
              <div className="rounded-2xl border border-dashed border-stone-300 bg-stone-50 px-5 py-4 text-sm leading-relaxed text-stone-500">
                Centralizer baru bisa ditampilkan setelah posisi simbol 4 pada A
                membentuk permutasi yang valid.
              </div>
            )}
          </div>
        </motion.div>

        <motion.div variants={item} className="space-y-3">
          {steps.map((step, index) => (
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
                    <MatrixPreview matrix={step.matrix} />
                  </div>

                  <div className="space-y-4">
                    {step.formula ? (
                      <div className="rounded-2xl border border-stone-200 bg-stone-50 px-4 py-5">
                        <MathBlock
                          tex={step.id === "sigma4" && selectedCandidate
                            ? `\\sigma_4^B = ${permutationToTex(selectedCandidate)}`
                            : step.formula}
                          display
                          className="text-stone-950"
                        />
                      </div>
                    ) : null}

                    <div className="rounded-2xl border border-sky-200 bg-sky-50 px-5 py-4">
                      <p className="text-xs font-bold uppercase tracking-[0.24em] text-sky-700">
                        Cara membacanya
                      </p>
                      <p className="mt-3 text-sm leading-relaxed text-sky-950">
                        {step.id === "start"
                          ? "Di tahap ini B* masih kosong. Yang sedang diputuskan baru data awal dari A dan centralizer yang akan dipakai."
                          : step.id === "sigma4"
                            ? "Pilihan centralizer yang sedang aktif langsung menentukan bentuk awal B*. Kalau kamu ganti kandidat di atas, bentuk angka 4 pada tahap ini ikut berubah."
                            : step.id === "sigma3"
                              ? "Sesudah sigma_4^B dipilih, simbol 3 ditambahkan pada cabang yang sama. Jadi visual ini memang mengikuti pilihan centralizer yang kamu klik."
                              : step.id === "sigma2"
                                ? "Di sini B* sudah hampir lengkap. Kalau kandidat centralizer tadi berbeda, pola yang kamu lihat di tahap ini juga bisa berbeda."
                                : "Setelah semua pemeriksaan lolos, B* ditutup menjadi B penuh. Jadi pengunjung bisa lihat bahwa pilihan centralizer memang menghasilkan keluaran akhir yang berbeda."}
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
