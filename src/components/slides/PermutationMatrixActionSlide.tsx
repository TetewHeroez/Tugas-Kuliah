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

type MatrixValue = number | string;
type Matrix = readonly (readonly MatrixValue[])[];

const latinSquare = [
  [2, 3, 1],
  [1, 2, 3],
  [3, 1, 2],
] as const satisfies Matrix;

const sigmaMatrix = [
  ["ε", 0, "ε"],
  ["ε", "ε", 0],
  [0, "ε", "ε"],
] as const satisfies Matrix;

const tauMatrix = [
  ["ε", "ε", 0],
  [0, "ε", "ε"],
  ["ε", 0, "ε"],
] as const satisfies Matrix;

const actionModes = [
  {
    id: "left",
    label: "Kali kiri",
    formula: "P_{\\sigma} \\otimes A",
    explanation:
      "Perkalian kiri oleh matriks permutasi max-plus hanya menukar urutan baris.",
    result: [
      [1, 2, 3],
      [3, 1, 2],
      [2, 3, 1],
    ] as const satisfies Matrix,
  },
  {
    id: "right",
    label: "Kali kanan",
    formula: "A \\otimes P_{\\tau}",
    explanation:
      "Perkalian kanan oleh matriks permutasi max-plus hanya menukar urutan kolom.",
    result: [
      [3, 1, 2],
      [2, 3, 1],
      [1, 2, 3],
    ] as const satisfies Matrix,
  },
  {
    id: "both",
    label: "Dua sisi",
    formula: "P_{\\sigma} \\otimes A \\otimes P_{\\tau}",
    explanation:
      "Kalau keduanya dipakai sekaligus, yang berubah hanyalah posisi baris dan kolomnya; sifat Latin square tetap terjaga.",
    result: [
      [2, 3, 1],
      [1, 2, 3],
      [3, 1, 2],
    ] as const satisfies Matrix,
  },
] as const;

function matrixCellBase(value: MatrixValue) {
  if (value === "ε") return "bg-stone-50 text-stone-400";
  if (value === 0) return "bg-sky-100 font-bold text-sky-900";
  return "bg-white text-stone-900";
}

function MatrixCard({
  title,
  matrix,
  accent = "stone",
}: {
  title: string;
  matrix: Matrix;
  accent?: "amber" | "sky" | "emerald" | "stone";
}) {
  const titleClass = {
    amber: "text-amber-800",
    sky: "text-sky-800",
    emerald: "text-emerald-800",
    stone: "text-stone-700",
  }[accent];

  const columns = matrix[0]?.length ?? 1;

  return (
    <section className="shrink-0">
      <h3 className={`text-center text-xs font-bold uppercase tracking-[0.24em] ${titleClass}`}>
        {title}
      </h3>
      <div className="mt-2 flex justify-center">
        <div
          className="grid overflow-hidden rounded-md border border-stone-300 bg-white"
          style={{ gridTemplateColumns: `repeat(${columns}, minmax(0, 1fr))` }}
        >
          {matrix.flatMap((row, rowIndex) =>
            row.map((value, colIndex) => (
              <div
                key={`${title}-${rowIndex}-${colIndex}`}
                className={[
                  "flex h-10 w-10 items-center justify-center border border-stone-200 text-sm font-semibold sm:h-12 sm:w-12 sm:text-base",
                  matrixCellBase(value),
                ].join(" ")}
              >
                {value}
              </div>
            )),
          )}
        </div>
      </div>
    </section>
  );
}

export default function PermutationMatrixActionSlide() {
  const [activeAction, setActiveAction] = useState<"left" | "right" | "both">(
    "left",
  );

  const currentAction = useMemo(
    () => actionModes.find((mode) => mode.id === activeAction) ?? actionModes[0],
    [activeAction],
  );

  return (
    <div className="w-full min-h-dvh px-4 pb-24 pt-24 sm:px-6">
      <motion.div
        variants={container}
        initial="hidden"
        animate="visible"
        className="mx-auto flex w-full max-w-3xl flex-col items-center gap-6"
      >
        <motion.div variants={item} className="space-y-2 text-center">
          <p className="text-xs font-bold uppercase tracking-widest text-amber-600">
            Aksi Matriks Permutasi
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Perkalian dari kiri dan kanan hanya menyusun ulang baris dan kolom.
          </h2>
          <p className="text-left text-sm leading-relaxed text-stone-600">
            Di bab 4, sudut pandang permutasi dipakai lagi untuk menunjukkan
            bahwa Latin square tetap menjadi Latin square setelah dikalikan oleh
            matriks permutasi max-plus dari kiri, kanan, atau keduanya.
          </p>
        </motion.div>

        <motion.div
          variants={item}
          className="w-full rounded-lg border border-stone-200 bg-white p-5 shadow-sm"
        >
          <div className="space-y-4">
            <div className="flex flex-wrap gap-3">
              {actionModes.map((mode) => {
                const isActive = mode.id === activeAction;
                return (
                  <button
                    key={mode.id}
                    type="button"
                    onClick={() => setActiveAction(mode.id)}
                    className={[
                      "rounded-full border px-4 py-2 text-sm font-semibold transition-colors",
                      isActive
                        ? "border-sky-600 bg-sky-600 text-white"
                        : "border-stone-300 bg-white text-stone-700 hover:border-sky-500 hover:text-stone-950",
                    ].join(" ")}
                  >
                    {mode.label}
                  </button>
                );
              })}
            </div>

            <div className="overflow-x-auto rounded-2xl border border-stone-200 bg-stone-50 px-4 py-5">
              <MathBlock
                tex={currentAction.formula}
                display
                className="text-stone-950"
              />
            </div>

            <div className="grid gap-4 md:grid-cols-2">
              <div className="space-y-4 rounded-2xl border border-stone-200 bg-white p-4">
                <p className="text-sm leading-relaxed text-stone-600">
                  {currentAction.explanation}
                </p>
                <div className="flex flex-wrap items-center justify-center gap-3">
                  {(activeAction === "left" || activeAction === "both") && (
                    <>
                      <MatrixCard title="Pσ" matrix={sigmaMatrix} accent="sky" />
                      <div className="text-2xl font-semibold text-stone-900">
                        ⊗
                      </div>
                    </>
                  )}
                  <MatrixCard title="A" matrix={latinSquare} accent="amber" />
                  {(activeAction === "right" || activeAction === "both") && (
                    <>
                      <div className="text-2xl font-semibold text-stone-900">
                        ⊗
                      </div>
                      <MatrixCard title="Pτ" matrix={tauMatrix} accent="sky" />
                    </>
                  )}
                </div>
              </div>

              <div className="space-y-4 rounded-2xl border border-stone-200 bg-white p-4">
                <p className="text-xs font-bold uppercase tracking-[0.24em] text-emerald-700">
                  Hasil tetap Latin square
                </p>
                <MatrixCard
                  title="Hasil"
                  matrix={currentAction.result}
                  accent="emerald"
                />
                <p className="text-sm leading-relaxed text-stone-600">
                  Yang berubah hanya letak baris dan/atau kolomnya. Setiap
                  simbol tetap muncul tepat satu kali pada setiap baris dan
                  kolom.
                </p>
              </div>
            </div>
          </div>
        </motion.div>
      </motion.div>
    </div>
  );
}
