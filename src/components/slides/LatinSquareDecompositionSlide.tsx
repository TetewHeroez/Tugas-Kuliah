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

type SymbolId = 1 | 2 | 3;
type MatrixValue = number | "eps";
type Matrix = readonly (readonly MatrixValue[])[];
type EntryPosition = readonly [number, number];

const latinSquare = [
  [2, 3, 1],
  [1, 2, 3],
  [3, 1, 2],
] as const;

const decompositionLayers = [
  {
    symbol: 1 as const,
    permutationLabel: "(1\\ 3\\ 2)",
    permutationName: "\\sigma_1",
    positions: [
      [0, 2],
      [1, 0],
      [2, 1],
    ] as const satisfies readonly EntryPosition[],
    permutationMatrix: [
      ["eps", "eps", 0],
      [0, "eps", "eps"],
      ["eps", 0, "eps"],
    ] as const satisfies Matrix,
  },
  {
    symbol: 2 as const,
    permutationLabel: "(1)(2)(3)",
    permutationName: "\\sigma_2",
    positions: [
      [0, 0],
      [1, 1],
      [2, 2],
    ] as const satisfies readonly EntryPosition[],
    permutationMatrix: [
      [0, "eps", "eps"],
      ["eps", 0, "eps"],
      ["eps", "eps", 0],
    ] as const satisfies Matrix,
  },
  {
    symbol: 3 as const,
    permutationLabel: "(1\\ 2\\ 3)",
    permutationName: "\\sigma_3",
    positions: [
      [0, 1],
      [1, 2],
      [2, 0],
    ] as const satisfies readonly EntryPosition[],
    permutationMatrix: [
      ["eps", 0, "eps"],
      ["eps", "eps", 0],
      [0, "eps", "eps"],
    ] as const satisfies Matrix,
  },
] as const;

function getSymbolAccent(symbol: SymbolId) {
  return {
    1: {
      muted: "bg-amber-100 text-amber-900",
      active: "bg-amber-300 text-amber-950 ring-2 ring-amber-600",
      badge: "border-amber-200 bg-amber-100 text-amber-800",
      text: "text-amber-700",
    },
    2: {
      muted: "bg-sky-100 text-sky-900",
      active: "bg-sky-300 text-sky-950 ring-2 ring-sky-600",
      badge: "border-sky-200 bg-sky-100 text-sky-800",
      text: "text-sky-700",
    },
    3: {
      muted: "bg-emerald-100 text-emerald-900",
      active: "bg-emerald-300 text-emerald-950 ring-2 ring-emerald-600",
      badge: "border-emerald-200 bg-emerald-100 text-emerald-800",
      text: "text-emerald-700",
    },
  }[symbol];
}

function matrixCellBase(value: MatrixValue, symbol: SymbolId | null) {
  if (value === "eps") return "bg-stone-50 text-stone-400";
  if (value === 0 && symbol)
    return `${getSymbolAccent(symbol).muted} font-bold`;
  if (value === 0) return "bg-stone-100 font-bold text-stone-700";
  return "bg-white text-stone-900";
}

function LatinSquareCard({
  matrix,
  activeSymbol,
  onSelectSymbol,
}: {
  matrix: readonly (readonly SymbolId[])[];
  activeSymbol: SymbolId | null;
  onSelectSymbol: (symbol: SymbolId) => void;
}) {
  const columns = matrix[0]?.length ?? 1;

  return (
    <section className="shrink-0">
      <h3 className="text-center text-xs font-bold uppercase tracking-[0.24em] text-amber-800">
        Latin Square A
      </h3>
      <div className="mt-2 flex justify-center">
        <div
          className="grid overflow-hidden rounded-md border border-stone-300 bg-white"
          style={{ gridTemplateColumns: `repeat(${columns}, minmax(0, 1fr))` }}
        >
          {matrix.flatMap((row, rowIndex) =>
            row.map((value, colIndex) => {
              const accent = getSymbolAccent(value);
              const isActive = activeSymbol !== null && value === activeSymbol;

              return (
                <button
                  key={`latin-${rowIndex}-${colIndex}`}
                  type="button"
                  onClick={() => onSelectSymbol(value)}
                  className={[
                    "flex h-12 w-12 items-center justify-center border border-stone-200 text-base font-semibold transition-colors sm:h-14 sm:w-14 sm:text-lg",
                    isActive
                      ? accent.active
                      : "bg-white text-stone-900 hover:bg-stone-50",
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

function PermutationMatrixCard({
  titleTex,
  matrix,
  symbol,
}: {
  titleTex: string;
  matrix: Matrix;
  symbol: SymbolId | null;
}) {
  const columns = matrix[0]?.length ?? 1;

  return (
    <section className="shrink-0">
      <div className="text-center text-xs font-bold tracking-[0.24em] text-stone-700 [&_.katex]:text-current">
        <MathBlock tex={titleTex} />
      </div>
      <div className="mt-2 flex justify-center">
        <div
          className="grid overflow-hidden rounded-md border border-stone-300 bg-white"
          style={{ gridTemplateColumns: `repeat(${columns}, minmax(0, 1fr))` }}
        >
          {matrix.flatMap((row, rowIndex) =>
            row.map((value, colIndex) => (
              <div
                key={`${titleTex}-${rowIndex}-${colIndex}`}
                className={[
                  "flex h-12 w-12 items-center justify-center border border-stone-200 text-base font-semibold sm:h-14 sm:w-14 sm:text-lg",
                  matrixCellBase(value, symbol),
                ].join(" ")}
              >
                {value === "eps" ? "ε" : value}
              </div>
            )),
          )}
        </div>
      </div>
    </section>
  );
}

export default function LatinSquareDecompositionSlide() {
  const [activeSymbol, setActiveSymbol] = useState<SymbolId | null>(null);

  const currentLayer = useMemo(
    () =>
      activeSymbol === null
        ? null
        : (decompositionLayers.find((layer) => layer.symbol === activeSymbol) ??
          null),
    [activeSymbol],
  );

  const accent = activeSymbol ? getSymbolAccent(activeSymbol) : null;
  const decompositionFormula = useMemo(
    () =>
      "A = \\bigoplus_{i=1}^n a_i P_{\\sigma_i}, \\quad i = 1, 2, \\ldots, n",
    [],
  );

  const positionText = currentLayer
    ? currentLayer.positions
        .map(([row, col]) => `(${row + 1}, ${col + 1})`)
        .join(", ")
    : "";

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
            Dekomposisi Permutasi
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Matriks Permutasi
          </h2>
          <p className="text-left text-sm leading-relaxed text-stone-600">
            Pada Latin square, setiap simbol muncul tepat satu kali di setiap
            baris dan kolom. Karena itu, posisi kemunculan satu simbol dapat
            dibaca sebagai pemetaan dari himpunan baris ke himpunan kolom, dan
            pemetaan itulah yang direpresentasikan oleh matriks permutasi.
          </p>
        </motion.div>

        <motion.div
          variants={item}
          className="w-full rounded-lg border border-stone-200 bg-white p-5 shadow-sm"
        >
          <div className="space-y-4">
            <div className="overflow-x-auto rounded-2xl border border-stone-200 bg-stone-50 px-4 py-5">
              <MathBlock
                tex={decompositionFormula}
                display
                className="text-stone-950"
              />
            </div>

            <div className="rounded-2xl border border-stone-200 bg-white p-4 sm:p-5">
              <div className="space-y-4">
                {currentLayer && accent ? (
                  <div className="flex flex-wrap items-center gap-3">
                    <span
                      className={[
                        "inline-flex items-center rounded-full border px-3 py-1 text-xs font-bold uppercase tracking-[0.24em]",
                        accent.badge,
                      ].join(" ")}
                    >
                      Simbol {currentLayer.symbol}
                    </span>
                    <p className="text-sm leading-relaxed text-stone-600">
                      Simbol {currentLayer.symbol} muncul pada posisi{" "}
                      <span className="font-semibold text-stone-800">
                        {positionText}
                      </span>
                      . Karena pada setiap baris simbol ini muncul tepat satu
                      kali, daftar posisi tersebut menentukan permutasi{" "}
                      <span
                        className={`inline-flex align-middle font-semibold ${accent.text}`}
                      >
                        <MathBlock tex={currentLayer.permutationName} />
                      </span>{" "}
                      dengan bentuk siklus{" "}
                      <span
                        className={`inline-flex align-middle font-semibold ${accent.text}`}
                      >
                        <MathBlock tex={currentLayer.permutationLabel} />
                      </span>
                      .
                    </p>
                  </div>
                ) : (
                  <p className="text-sm leading-relaxed text-stone-600">
                    Klik salah satu simbol pada Latin square untuk melihat
                    bagaimana kemunculannya di tiap baris membentuk sebuah
                    permutasi.
                  </p>
                )}
                <div className="grid gap-6 min-[520px]:grid-cols-2 min-[520px]:items-start">
                  <LatinSquareCard
                    matrix={latinSquare}
                    activeSymbol={activeSymbol}
                    onSelectSymbol={setActiveSymbol}
                  />
                  {currentLayer ? (
                    <PermutationMatrixCard
                      titleTex={`P_{${currentLayer.permutationName}}`}
                      matrix={currentLayer.permutationMatrix}
                      symbol={currentLayer.symbol}
                    />
                  ) : (
                    <div className="flex min-h-[11rem] items-center justify-center rounded-2xl border border-dashed border-stone-300 bg-stone-50 px-6 text-center text-sm leading-relaxed text-stone-500 sm:min-h-[14rem]">
                      Matriks permutasi akan ditampilkan di sini setelah satu
                      simbol dipilih.
                    </div>
                  )}
                </div>
              </div>
            </div>

            <div className="rounded-2xl border border-teal-200 bg-teal-50 px-5 py-4">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-teal-700">
                Inti ide
              </p>
              <p className="mt-3 text-sm leading-relaxed text-teal-950">
                Jadi dekomposisi Latin square dikerjakan dengan membaca satu
                simbol demi satu simbol. Dari tiap simbol kita peroleh satu
                matriks permutasi, lalu seluruh matriks permutasi itu digabung
                kembali melalui operasi max-plus untuk merepresentasikan Latin
                square semula.
              </p>
            </div>
          </div>
        </motion.div>
      </motion.div>
    </div>
  );
}
