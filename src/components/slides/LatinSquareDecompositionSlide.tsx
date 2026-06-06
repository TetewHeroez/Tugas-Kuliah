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
type EntryPosition = readonly [number, number];

const latinSquare = [
  [2, 3, 1],
  [1, 2, 3],
  [3, 1, 2],
] as const;

const decompositionLayers = [
  {
    symbol: 1,
    permutationLabel: "(1\\ 3\\ 2)",
    permutationName: "\\sigma_1",
    positions: [
      [0, 2],
      [1, 0],
      [2, 1],
    ] as const satisfies readonly EntryPosition[],
    permutationMatrix: [
      ["ε", "ε", 0],
      [0, "ε", "ε"],
      ["ε", 0, "ε"],
    ] as const satisfies Matrix,
  },
  {
    symbol: 2,
    permutationLabel: "(1)(2)(3)",
    permutationName: "\\sigma_2",
    positions: [
      [0, 0],
      [1, 1],
      [2, 2],
    ] as const satisfies readonly EntryPosition[],
    permutationMatrix: [
      [0, "ε", "ε"],
      ["ε", 0, "ε"],
      ["ε", "ε", 0],
    ] as const satisfies Matrix,
  },
  {
    symbol: 3,
    permutationLabel: "(1\\ 2\\ 3)",
    permutationName: "\\sigma_3",
    positions: [
      [0, 1],
      [1, 2],
      [2, 0],
    ] as const satisfies readonly EntryPosition[],
    permutationMatrix: [
      ["ε", 0, "ε"],
      ["ε", "ε", 0],
      [0, "ε", "ε"],
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
  highlightedPositions = [],
}: {
  title: string;
  matrix: Matrix;
  accent?: "amber" | "sky" | "emerald" | "stone";
  highlightedPositions?: readonly EntryPosition[];
}) {
  const titleClass = {
    amber: "text-amber-800",
    sky: "text-sky-800",
    emerald: "text-emerald-800",
    stone: "text-stone-700",
  }[accent];

  const highlightClass = {
    amber: "bg-amber-200 text-amber-950",
    sky: "bg-sky-200 text-sky-950",
    emerald: "bg-emerald-200 text-emerald-950",
    stone: "bg-stone-200 text-stone-950",
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
            row.map((value, colIndex) => {
              const isHighlighted = highlightedPositions.some(
                ([r, c]) => r === rowIndex && c === colIndex,
              );
              return (
                <div
                  key={`${title}-${rowIndex}-${colIndex}`}
                  className={[
                    "flex h-10 w-10 items-center justify-center border border-stone-200 text-sm font-semibold sm:h-12 sm:w-12 sm:text-base",
                    matrixCellBase(value),
                    isHighlighted ? highlightClass : "",
                  ].join(" ")}
                >
                  {value}
                </div>
              );
            }),
          )}
        </div>
      </div>
    </section>
  );
}

export default function LatinSquareDecompositionSlide() {
  const [activeSymbol, setActiveSymbol] = useState(1);

  const currentLayer = useMemo(
    () =>
      decompositionLayers.find((layer) => layer.symbol === activeSymbol) ??
      decompositionLayers[0],
    [activeSymbol],
  );

  const decompositionFormula = useMemo(
    () =>
      [
        "A = 1P_{\\sigma_1} \\oplus 2P_{\\sigma_2} \\oplus 3P_{\\sigma_3}",
        `\\quad\\text{dengan}\\quad ${currentLayer.permutationName} = ${currentLayer.permutationLabel}`,
      ].join(" "),
    [currentLayer],
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
            Dekomposisi Permutasi
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Latin square bisa dibaca sebagai gabungan simbol dan matriks
            permutasi.
          </h2>
          <p className="text-left text-sm leading-relaxed text-stone-600">
            Di bab 2, Latin square ditulis sebagai penjumlahan max-plus dari
            beberapa matriks permutasi. Artinya, setiap simbol tidak cuma punya
            nilai, tapi juga punya pola posisi yang membentuk permutasi sendiri.
          </p>
        </motion.div>

        <motion.div
          variants={item}
          className="w-full rounded-lg border border-stone-200 bg-white p-5 shadow-sm"
        >
          <div className="space-y-4">
            <div className="flex flex-wrap gap-3">
              {decompositionLayers.map((layer) => {
                const isActive = layer.symbol === activeSymbol;
                return (
                  <button
                    key={layer.symbol}
                    type="button"
                    onClick={() => setActiveSymbol(layer.symbol)}
                    className={[
                      "rounded-full border px-4 py-2 text-sm font-semibold transition-colors",
                      isActive
                        ? "border-amber-500 bg-amber-500 text-white"
                        : "border-stone-300 bg-white text-stone-700 hover:border-amber-400 hover:text-stone-950",
                    ].join(" ")}
                  >
                    Simbol {layer.symbol}
                  </button>
                );
              })}
            </div>

            <div className="overflow-x-auto rounded-2xl border border-stone-200 bg-stone-50 px-4 py-5">
              <MathBlock
                tex={decompositionFormula}
                display
                className="text-stone-950"
              />
            </div>

            <div className="grid gap-4 md:grid-cols-2">
              <div className="space-y-4 rounded-2xl border border-stone-200 bg-white p-4">
                <div>
                  <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
                    Dari simbol ke posisi
                  </p>
                  <p className="mt-2 text-sm leading-relaxed text-stone-600">
                    Setiap simbol muncul tepat satu kali pada setiap baris dan
                    kolom. Posisi-posisi itu membentuk sebuah permutasi.
                  </p>
                </div>
                <MatrixCard
                  title="Latin Square A"
                  matrix={latinSquare}
                  accent="amber"
                  highlightedPositions={currentLayer.positions}
                />
              </div>

              <div className="space-y-4 rounded-2xl border border-stone-200 bg-white p-4">
                <div>
                  <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
                    Matriks permutasi max-plus
                  </p>
                  <p className="mt-2 text-sm leading-relaxed text-stone-600">
                    Entri 0 menandai posisi hasil permutasi, sedangkan ε
                    menandai posisi lain.
                  </p>
                </div>
                <MatrixCard
                  title={`P${currentLayer.permutationName}`}
                  matrix={currentLayer.permutationMatrix}
                  accent="sky"
                />
              </div>
            </div>

            <div className="rounded-2xl border border-emerald-200 bg-emerald-50 px-5 py-4">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-emerald-700">
                Inti ide
              </p>
              <p className="mt-3 text-sm leading-relaxed text-emerald-950">
                Jadi satu Latin square bisa dibaca sebagai tumpukan beberapa
                matriks permutasi max-plus, masing-masing diberi bobot simbol
                yang sesuai.
              </p>
            </div>
          </div>
        </motion.div>
      </motion.div>
    </div>
  );
}
