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

const levelData = [
  {
    level: 2,
    pairs: ["(1,1)"],
    terms: ["P_{\\sigma_1^B \\circ \\sigma_1^A}"],
    kept: false,
  },
  {
    level: 3,
    pairs: ["(1,2)", "(2,1)"],
    terms: [
      "P_{\\sigma_2^B \\circ \\sigma_1^A}",
      "P_{\\sigma_1^B \\circ \\sigma_2^A}",
    ],
    kept: false,
  },
  {
    level: 4,
    pairs: ["(1,3)", "(2,2)", "(3,1)"],
    terms: [
      "P_{\\sigma_3^B \\circ \\sigma_1^A}",
      "P_{\\sigma_2^B \\circ \\sigma_2^A}",
      "P_{\\sigma_1^B \\circ \\sigma_3^A}",
    ],
    kept: true,
  },
  {
    level: 5,
    pairs: ["(2,3)", "(3,2)"],
    terms: [
      "P_{\\sigma_3^B \\circ \\sigma_2^A}",
      "P_{\\sigma_2^B \\circ \\sigma_3^A}",
    ],
    kept: true,
  },
  {
    level: 6,
    pairs: ["(3,3)"],
    terms: ["P_{\\sigma_3^B \\circ \\sigma_3^A}"],
    kept: true,
  },
] as const;

const fullFormula =
  "A \\otimes B = \\bigoplus_{k=2}^{2n} k \\otimes \\left( \\bigoplus_{\\substack{i,j \\in \\underline{n} \\\\ i+j=k}} P_{\\sigma_j^B \\circ \\sigma_i^A} \\right)";

const reducedFormula =
  "A \\otimes B = \\bigoplus_{k=n+1}^{2n} k \\otimes \\left( \\bigoplus_{\\substack{i,j \\in \\underline{n} \\\\ i+j=k}} P_{\\sigma_j^B \\circ \\sigma_i^A} \\right)";

const lowerBoundFormula =
  "[A \\otimes B]_{rs} \\ge n + 1";

const sampleEntryFormula =
  "[A \\otimes B]_{rs} = \\max_t\\left(A_{rt} + B_{ts}\\right) \\ge n + 1";

export default function LatinSquareProductReductionSlide() {
  const [activeLevel, setActiveLevel] = useState<4 | 5 | 6>(4);

  const currentLevel = useMemo(
    () => levelData.find((entry) => entry.level === activeLevel) ?? levelData[2],
    [activeLevel],
  );

  const exampleTex = useMemo(
    () =>
      `A \\otimes B = ${currentLevel.level} \\otimes \\left(${currentLevel.terms.join(
        " \\oplus ",
      )}\\right)`,
    [currentLevel],
  );

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
            Hasil perkalian dua Latin square tidak perlu dihitung dari level 2.
          </h2>
          <p className="text-left text-sm leading-relaxed text-stone-600">
            Di bab 4, dekomposisi hasil kali awalnya memang muncul dari semua
            level {`2`} sampai {`2n`}. Tetapi karena setiap entri pada{" "}
            <span className="font-semibold text-stone-800">A ⊗ B</span> selalu
            bernilai minimal <span className="font-semibold text-stone-800">n+1</span>,
            maka suku-suku dengan level di bawah itu tidak pernah menentukan
            nilai akhir.
          </p>
        </motion.div>

        <motion.div
          variants={item}
          className="grid w-full gap-4 lg:grid-cols-[minmax(0,1.02fr)_minmax(0,1fr)]"
        >
          <div className="space-y-4 rounded-lg border border-stone-200 bg-white p-5 shadow-sm">
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
              Rumus Sebelum dan Sesudah Reduksi
            </p>

            <div className="overflow-x-auto rounded-2xl border border-stone-200 bg-stone-50 px-4 py-5">
              <MathBlock tex={fullFormula} display className="text-stone-950" />
            </div>

            <div className="rounded-2xl border border-emerald-200 bg-emerald-50 px-4 py-5">
              <MathBlock
                tex={reducedFormula}
                display
                className="text-emerald-950"
              />
            </div>

            <div className="rounded-2xl border border-sky-200 bg-sky-50 px-5 py-4">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-sky-700">
                Kenapa boleh direduksi
              </p>
              <div className="mt-3 overflow-x-auto">
                <MathBlock
                  tex={`${lowerBoundFormula} \\quad\\text{karena}\\quad ${sampleEntryFormula}`}
                  display
                  className="text-sky-950"
                />
              </div>
              <p className="mt-3 text-sm leading-relaxed text-sky-950">
                Pada setiap baris A selalu ada simbol maksimum n, dan pada kolom
                B setiap entri minimal bernilai 1. Jadi kontribusi paling kecil
                yang pasti bisa dicapai sudah n+1. Itulah sebabnya level 2
                sampai n tidak lagi berpengaruh.
              </p>
            </div>
          </div>

          <div className="space-y-4 rounded-lg border border-stone-200 bg-white p-5 shadow-sm">
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
              Ilustrasi Ordo 3
            </p>

            <div className="grid grid-cols-5 gap-2">
              {levelData.map((entry) => {
                const isActive = entry.level === activeLevel;
                return (
                  <button
                    key={entry.level}
                    type="button"
                    onClick={() => {
                      if (entry.kept) {
                        setActiveLevel(entry.level as 4 | 5 | 6);
                      }
                    }}
                    className={[
                      "rounded-2xl border px-3 py-3 text-center transition-colors",
                      entry.kept
                        ? isActive
                          ? "border-emerald-500 bg-emerald-500 text-white"
                          : "border-stone-300 bg-white text-stone-700 hover:border-emerald-400 hover:text-stone-950"
                        : "border-stone-200 bg-stone-100 text-stone-400",
                    ].join(" ")}
                  >
                    <p className="text-xs font-bold uppercase tracking-[0.2em]">
                      k
                    </p>
                    <p className="mt-1 text-lg font-bold">{entry.level}</p>
                  </button>
                );
              })}
            </div>

            <div className="rounded-2xl border border-stone-200 bg-stone-50 p-4">
              <p className="text-sm leading-relaxed text-stone-600">
                Untuk ordo 3, dekomposisi awal punya level 2, 3, 4, 5, 6.
                Setelah reduksi, yang tersisa hanya level{" "}
                <span className="font-semibold text-stone-800">4, 5, 6</span>.
              </p>
            </div>

            <div className="grid gap-4 min-[520px]:grid-cols-2">
              <div className="rounded-2xl border border-stone-200 bg-white p-4">
                <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
                  Pasangan indeks yang bertahan
                </p>
                <div className="mt-3 flex flex-wrap gap-2">
                  {currentLevel.pairs.map((pair) => (
                    <span
                      key={pair}
                      className="rounded-full border border-amber-200 bg-amber-100 px-3 py-1 text-sm font-semibold text-amber-800"
                    >
                      {pair}
                    </span>
                  ))}
                </div>
                <p className="mt-3 text-sm leading-relaxed text-stone-600">
                  Ini adalah semua pasangan (i, j) yang memenuhi i + j ={" "}
                  <span className="font-semibold text-stone-800">
                    {currentLevel.level}
                  </span>
                  .
                </p>
              </div>

              <div className="rounded-2xl border border-stone-200 bg-white p-4">
                <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
                  Suku yang muncul pada level itu
                </p>
                <div className="mt-3 overflow-x-auto">
                  <MathBlock
                    tex={exampleTex}
                    display
                    className="text-stone-950"
                  />
                </div>
              </div>
            </div>

            <div className="rounded-2xl border border-emerald-200 bg-emerald-50 px-5 py-4">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-emerald-700">
                Inti ide
              </p>
              <p className="mt-3 text-sm leading-relaxed text-emerald-950">
                Reduksi ini membuat evaluasi hasil kali menjadi lebih efisien
                karena kita langsung mulai dari level yang memang mungkin
                mempengaruhi entri hasil, yaitu n+1 sampai 2n.
              </p>
            </div>
          </div>
        </motion.div>
      </motion.div>
    </div>
  );
}
