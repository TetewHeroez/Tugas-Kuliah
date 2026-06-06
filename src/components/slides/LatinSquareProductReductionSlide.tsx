"use client";

import { motion } from "framer-motion";
import { useMemo, useState } from "react";
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

type Matrix = readonly (readonly number[])[];

const order = 4;
const lowerBound = order + 1;

const matrixA = [
  [1, 2, 4, 3],
  [3, 1, 2, 4],
  [2, 4, 3, 1],
  [4, 3, 1, 2],
] as const satisfies Matrix;

const matrixB = [
  [1, 2, 3, 4],
  [2, 3, 4, 1],
  [3, 4, 1, 2],
  [4, 1, 2, 3],
] as const satisfies Matrix;

const compactFullFormula = "A \\otimes B = \\bigoplus_{k=2}^{2n} k \\otimes M_k";
const compactReducedFormula =
  "A \\otimes B = \\bigoplus_{k=n+1}^{2n} k \\otimes M_k";
const compactDefinition = "M_k = \\bigoplus_{i+j=k} P_{\\sigma_j^B \\circ \\sigma_i^A}";

function MatrixView({
  title,
  matrix,
  accent,
  activeRow,
  activeCol,
  onSelect,
}: {
  title: string;
  matrix: Matrix;
  accent: "amber" | "sky";
  activeRow?: number | null;
  activeCol?: number | null;
  onSelect: (row: number, col: number) => void;
}) {
  const titleClass = accent === "amber" ? "text-amber-800" : "text-sky-800";
  const activeClass =
    accent === "amber"
      ? "bg-amber-200 text-amber-950 ring-1 ring-amber-500"
      : "bg-sky-200 text-sky-950 ring-1 ring-sky-500";

  return (
    <section className="w-full">
      <h3
        className={`text-center text-xs font-bold uppercase tracking-[0.24em] ${titleClass}`}
      >
        {title}
      </h3>
      <div className="mt-3 flex justify-center">
        <div
          className="grid overflow-hidden rounded-xl border border-stone-300 bg-white"
          style={{ gridTemplateColumns: `repeat(${matrix[0]?.length ?? 1}, minmax(0, 1fr))` }}
        >
          {matrix.flatMap((row, rowIndex) =>
            row.map((value, colIndex) => {
              const isActive =
                activeRow === rowIndex || activeCol === colIndex;

              return (
                <button
                  key={`${title}-${rowIndex}-${colIndex}`}
                  type="button"
                  onClick={() => onSelect(rowIndex, colIndex)}
                  className={[
                    "flex h-12 w-12 items-center justify-center border border-stone-200 bg-white text-base font-semibold text-stone-900 transition-colors sm:h-14 sm:w-14 sm:text-lg",
                    isActive ? activeClass : "hover:bg-stone-50",
                  ].join(" ")}
                >
                  {value}
                </button>
              );
            }),
          )}
        </div>
      </div>
    </section>
  );
}

export default function LatinSquareProductReductionSlide() {
  const [selectedRow, setSelectedRow] = useState(0);
  const [selectedCol, setSelectedCol] = useState(0);

  const entryTerms = useMemo(
    () =>
      matrixA[selectedRow].map((aValue, index) => {
        const bValue = matrixB[index][selectedCol];
        const sum = aValue + bValue;
        return {
          index,
          aValue,
          bValue,
          sum,
        };
      }),
    [selectedRow, selectedCol],
  );

  const maxValue = useMemo(
    () => Math.max(...entryTerms.map((term) => term.sum)),
    [entryTerms],
  );

  const entryTex = `[(A \\otimes B)]_{${selectedRow + 1}${selectedCol + 1}}`;

  return (
    <div className="w-full min-h-dvh px-4 pb-40 pt-28 sm:px-6 sm:pb-36 sm:pt-28">
      <motion.div
        variants={container}
        initial="hidden"
        animate="visible"
        className="mx-auto flex w-full max-w-4xl flex-col items-center gap-8"
      >
        <motion.div variants={item} className="space-y-2 text-center">
          <p className="text-xs font-bold uppercase tracking-widest text-amber-600">
            Reduksi Dekomposisi
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Level kecil bisa dibuang karena hasil perkalian selalu minimal n+1.
          </h2>
          <p className="text-left text-sm leading-relaxed text-stone-600">
            Jadi intinya bukan semua level harus dicek. Karena setiap entri
            hasil perkalian sudah pasti bernilai minimal{" "}
            <span className="font-semibold text-stone-800">{lowerBound}</span>,
            maka level 2 sampai n tidak akan menentukan hasil akhir.
          </p>
        </motion.div>

        <motion.div
          variants={item}
          className="grid w-full gap-4 lg:grid-cols-[minmax(0,0.96fr)_minmax(0,1.04fr)]"
        >
          <div className="space-y-4 rounded-lg border border-stone-200 bg-white p-5 shadow-sm">
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
              Bentuk Ringkas
            </p>

            <div className="rounded-2xl border border-rose-200 bg-rose-50 px-4 py-5">
              <MathBlock
                tex={compactFullFormula}
                display
                className="text-stone-950 [&_.katex]:text-[0.95rem] sm:[&_.katex]:text-base"
              />
            </div>

            <div className="rounded-2xl border border-emerald-200 bg-emerald-50 px-4 py-5">
              <MathBlock
                tex={compactReducedFormula}
                display
                className="text-emerald-950 [&_.katex]:text-[0.95rem] sm:[&_.katex]:text-base"
              />
            </div>

            <div className="rounded-2xl border border-stone-200 bg-stone-50 px-4 py-5">
              <MathBlock
                tex={compactDefinition}
                display
                className="text-stone-950 [&_.katex]:text-[0.9rem] sm:[&_.katex]:text-[0.96rem]"
              />
            </div>

            <div className="rounded-2xl border border-sky-200 bg-sky-50 px-5 py-4">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-sky-700">
                Kenapa boleh direduksi?
              </p>
              <p className="mt-3 text-sm leading-relaxed text-sky-950">
                Pada setiap baris Latin square A selalu ada simbol maksimum n,
                sedangkan pada setiap entri Latin square B nilainya minimal 1.
                Maka untuk entri apa pun pada hasil perkalian, pasti ada satu
                penjumlahan yang nilainya mencapai minimal n+1.
              </p>
            </div>
          </div>

          <div className="space-y-4 rounded-lg border border-stone-200 bg-white p-5 shadow-sm">
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
              Visualisasi Ordo 4
            </p>
            <p className="text-sm leading-relaxed text-stone-600">
              Klik satu sel pada A untuk memilih{" "}
              <span className="font-semibold text-amber-700">baris</span>, lalu
              klik satu sel pada B untuk memilih{" "}
              <span className="font-semibold text-sky-700">kolom</span>.
              Setelah itu, kita lihat semua penjumlahan yang mungkin untuk
              entri hasil tersebut.
            </p>

            <div className="grid gap-5 min-[560px]:grid-cols-2">
              <MatrixView
                title="Latin Square A"
                matrix={matrixA}
                accent="amber"
                activeRow={selectedRow}
                onSelect={(row) => setSelectedRow(row)}
              />
              <MatrixView
                title="Latin Square B"
                matrix={matrixB}
                accent="sky"
                activeCol={selectedCol}
                onSelect={(_, col) => setSelectedCol(col)}
              />
            </div>

            <div className="rounded-2xl border border-stone-200 bg-stone-50 px-5 py-4">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
                Perhitungan entri terpilih
              </p>
              <div className="mt-3">
                <MathBlock
                  tex={entryTex}
                  display
                  className="text-stone-950 [&_.katex-display]:my-0"
                />
              </div>
              <div className="mt-4 grid gap-2">
                {entryTerms.map((term) => {
                  const isMax = term.sum === maxValue;

                  return (
                    <div
                      key={`${term.index}-${term.sum}`}
                      className={[
                        "flex items-center justify-between rounded-xl border px-4 py-3 text-sm sm:text-base",
                        isMax
                          ? "border-emerald-300 bg-emerald-50 text-emerald-950"
                          : "border-stone-200 bg-white text-stone-700",
                      ].join(" ")}
                    >
                      <span>
                        {term.aValue} + {term.bValue}
                      </span>
                      <span className="font-semibold">= {term.sum}</span>
                    </div>
                  );
                })}
              </div>
              <div className="mt-4 rounded-2xl border border-emerald-200 bg-emerald-50 px-4 py-4">
                <p className="text-sm leading-relaxed text-emerald-950">
                  Nilai maksimumnya adalah{" "}
                  <span className="font-semibold">{maxValue}</span>, sehingga
                  untuk entri ini berlaku{" "}
                  <span className="font-semibold">
                    {maxValue} &gt;= {lowerBound}
                  </span>
                  . Contoh ini menunjukkan kenapa semua entri pada A x B selalu
                  punya batas bawah n+1.
                </p>
              </div>
            </div>
          </div>
        </motion.div>
      </motion.div>
    </div>
  );
}
