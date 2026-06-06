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

function matrixCellBase(value: MatrixValue) {
  if (value === "eps") return "bg-stone-50 text-stone-400";
  if (value === 0) return "bg-sky-100 font-bold text-sky-900";
  return "bg-white text-stone-900";
}

function LatinSquareCard({
  matrix,
  activeSymbol,
  onSelectSymbol,
}: {
  matrix: readonly (readonly SymbolId[])[];
  activeSymbol: SymbolId;
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
              const isActive = value === activeSymbol;

              return (
                <button
                  key={`latin-${rowIndex}-${colIndex}`}
                  type="button"
                  onClick={() => onSelectSymbol(value)}
                  className={[
                    "flex h-10 w-10 items-center justify-center border border-stone-200 text-sm font-semibold transition-colors sm:h-12 sm:w-12 sm:text-base",
                    isActive ? accent.active : accent.muted,
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
}: {
  titleTex: string;
  matrix: Matrix;
}) {
  const columns = matrix[0]?.length ?? 1;

  return (
    <section className="shrink-0">
      <div className="text-center text-xs font-bold uppercase tracking-[0.24em] text-sky-800 [&_.katex]:text-current">
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
                  "flex h-10 w-10 items-center justify-center border border-stone-200 text-sm font-semibold sm:h-12 sm:w-12 sm:text-base",
                  matrixCellBase(value),
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
  const [activeSymbol, setActiveSymbol] = useState<SymbolId>(1);

  const currentLayer = useMemo(
    () =>
      decompositionLayers.find((layer) => layer.symbol === activeSymbol) ??
      decompositionLayers[0],
    [activeSymbol],
  );

  const accent = getSymbolAccent(activeSymbol);
  const decompositionFormula = useMemo(
    () =>
      [
        "A = 1P_{\\sigma_1} \\oplus 2P_{\\sigma_2} \\oplus 3P_{\\sigma_3}",
        `\\quad\\text{dan untuk simbol ${currentLayer.symbol},}\\quad ${currentLayer.permutationName} = ${currentLayer.permutationLabel}`,
      ].join(" "),
    [currentLayer],
  );

  const positionText = currentLayer.positions
    .map(([row, col]) => `(${row + 1}, ${col + 1})`)
    .join(", ");

  return (
    <div className="w-full min-h-dvh px-4 pb-40 pt-28 sm:px-6 sm:pb-36 sm:pt-28">
      <motion.div
        variants={container}
        initial="hidden"
        animate="visible"
        className="mx-auto flex w-full max-w-3xl flex-col items-center gap-8"
      >
        <motion.div variants={item} className="space-y-2 text-center">
          <p className="text-xs font-bold uppercase tracking-widest text-amber-600">
            Dekomposisi Permutasi
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Setiap simbol pada Latin square menunjukkan satu permutasi.
          </h2>
          <p className="text-left text-sm leading-relaxed text-stone-600">
            Jadi sekarang simbolnya tidak kita pisah dulu lewat tombol. Klik
            saja salah satu angka pada Latin square, lalu slide ini akan
            menunjukkan simbol itu membentuk permutasi yang mana.
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

            <div className="rounded-2xl border border-stone-200 bg-white p-4">
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
                  Posisinya ada di {positionText}, sehingga simbol ini
                  menunjukkan{" "}
                  <span className={`inline-flex align-middle font-semibold ${accent.text}`}>
                    <MathBlock tex={currentLayer.permutationName} />
                  </span>{" "}
                  dengan siklus{" "}
                  <span className={`inline-flex align-middle font-semibold ${accent.text}`}>
                    <MathBlock tex={currentLayer.permutationLabel} />
                  </span>
                  .
                </p>
              </div>
            </div>

            <div className="grid gap-4 md:grid-cols-2">
              <div className="space-y-4 rounded-2xl border border-stone-200 bg-white p-4">
                <div>
                  <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
                    Klik simbol pada contoh
                  </p>
                  <p className="mt-2 text-sm leading-relaxed text-stone-600">
                    Setiap angka sudah dibedakan warnanya. Saat kamu klik satu
                    simbol, semua kemunculan simbol itu langsung dibaca sebagai
                    satu pola permutasi.
                  </p>
                </div>
                <LatinSquareCard
                  matrix={latinSquare}
                  activeSymbol={activeSymbol}
                  onSelectSymbol={setActiveSymbol}
                />
              </div>

              <div className="space-y-4 rounded-2xl border border-stone-200 bg-white p-4">
                <div>
                  <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
                    Matriks permutasi max-plus
                  </p>
                  <p className="mt-2 text-sm leading-relaxed text-stone-600">
                    Nilai 0 muncul tepat pada posisi hasil permutasi simbol
                    terpilih, sedangkan entri lain bernilai ε.
                  </p>
                </div>
                <PermutationMatrixCard
                  titleTex={`P_{${currentLayer.permutationName}}`}
                  matrix={currentLayer.permutationMatrix}
                />
              </div>
            </div>

            <div className="rounded-2xl border border-emerald-200 bg-emerald-50 px-5 py-4">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-emerald-700">
                Inti ide
              </p>
              <p className="mt-3 text-sm leading-relaxed text-emerald-950">
                Jadi dekomposisi itu bukan memisahkan simbol secara acak, tetapi
                membaca setiap simbol sebagai jejak posisi yang persis
                membentuk satu matriks permutasi.
              </p>
            </div>
          </div>
        </motion.div>
      </motion.div>
    </div>
  );
}
