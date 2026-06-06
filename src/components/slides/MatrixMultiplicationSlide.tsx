"use client";

import { AnimatePresence, motion } from "framer-motion";
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
type ModeId = "ordinary" | "maxplus";
type MatrixPosition = readonly [number, number];

const matrixA = [
  [1, 2, 0],
  [3, 1, 2],
  [2, 4, 1],
] as const satisfies Matrix;

const matrixB = [
  [2, 1, 3],
  [0, 4, 2],
  [1, 2, 5],
] as const satisfies Matrix;

const ordinaryResult = [
  [2, 9, 7],
  [8, 11, 21],
  [5, 20, 19],
] as const satisfies Matrix;

const maxPlusResult = [
  [3, 6, 5],
  [5, 5, 7],
  [4, 8, 6],
] as const satisfies Matrix;

const modes = [
  {
    id: "ordinary",
    label: "Aljabar Biasa",
    accent: "amber",
    formula: "c_{ij} = \\sum_{k=1}^{n} a_{ik}b_{kj}",
    note: "Kali dulu, lalu jumlahkan semua hasilnya.",
    result: ordinaryResult,
  },
  {
    id: "maxplus",
    label: "Aljabar Max-Plus",
    accent: "sky",
    formula: "c_{ij} =  \\max_k(a_{ik}+b_{kj})",
    note: "Tambah dulu, lalu ambil nilai maksimum.",
    result: maxPlusResult,
  },
] as const;

function matrixWrapperClass(accent: "amber" | "sky" | "emerald") {
  return {
    amber: "text-amber-800",
    sky: "text-sky-800",
    emerald: "text-emerald-800",
  }[accent];
}

function matrixCellClass(
  accent: "amber" | "sky" | "emerald",
  isActive: boolean,
) {
  if (!isActive) return "bg-white text-stone-900";

  return {
    amber: "bg-amber-200 text-amber-950",
    sky: "bg-sky-200 text-sky-950",
    emerald: "bg-emerald-500 text-emerald-950 ring-2 ring-emerald-700",
  }[accent];
}

function MatrixView({
  title,
  accent,
  matrix,
  activeRow,
  activeCol,
  selectedCell,
  onSelect,
}: {
  title: string;
  accent: "amber" | "sky" | "emerald";
  matrix: Matrix;
  activeRow?: number | null;
  activeCol?: number | null;
  selectedCell?: MatrixPosition | null;
  onSelect?: (position: MatrixPosition) => void;
}) {
  const columns = matrix[0]?.length ?? 1;
  const titleClass = matrixWrapperClass(accent);

  return (
    <section className="shrink-0">
      <h3
        className={`text-center text-xl font-bold uppercase tracking-[0.24em] ${titleClass}`}
      >
        {title}
      </h3>
      <div className="mt-1.5 flex items-center justify-center gap-1 sm:gap-1.5">
        <div
          className="grid overflow-hidden rounded-md border border-stone-300 bg-white"
          style={{ gridTemplateColumns: `repeat(${columns}, minmax(0, 1fr))` }}
        >
          {matrix.flatMap((row, rowIndex) =>
            row.map((value, colIndex) => {
              const isActiveRow = activeRow === rowIndex;
              const isActiveCol = activeCol === colIndex;
              const isSelected =
                selectedCell?.[0] === rowIndex &&
                selectedCell?.[1] === colIndex;
              const isHighlighted =
                accent === "amber"
                  ? isActiveRow
                  : accent === "sky"
                    ? isActiveCol
                    : isSelected;
              const cellClass = [
                "flex h-10 w-10 items-center justify-center border border-stone-200 text-base font-semibold transition-colors sm:h-12 sm:w-12 sm:text-lg",
                matrixCellClass(accent, isHighlighted),
                onSelect ? "cursor-pointer hover:bg-stone-100" : "",
                isSelected && accent === "emerald" ? "relative z-10" : "",
              ].join(" ");

              if (onSelect) {
                return (
                  <button
                    key={`${title}-${rowIndex}-${colIndex}`}
                    type="button"
                    onClick={() => onSelect([rowIndex, colIndex] as const)}
                    className={cellClass}
                  >
                    {value}
                  </button>
                );
              }

              return (
                <div
                  key={`${title}-${rowIndex}-${colIndex}`}
                  className={cellClass}
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
function buildMaxPlusExpression(row: number, col: number) {
  const sums = matrixA[row].map(
    (a, index) => `{\\color{orange}${a}}+{\\color{blue}${matrixB[index][col]}}`,
  );
  const values = matrixA[row].map((a, index) => a + matrixB[index][col]);
  const total = Math.max(...values);

  return [
    `c_{${row + 1}${col + 1}} = \\max\\left(${sums.join(",\\ ")}\\right)`,
    `\\max\\left({\\color{green}${values.join("{\\color{black},}\\ ")}}\\right) = {\\color{green}${total}}`,
  ].join(" = ");
}

function buildOrdinaryExpression(row: number, col: number) {
  const terms = matrixA[row].map((a, index) => {
    const b = matrixB[index][col];
    return `({\\color{orange}${a}}\\times{\\color{blue}${b}})`;
  });
  const values = matrixA[row].map((a, index) => a * matrixB[index][col]);
  const total = values.reduce((sum, value) => sum + value, 0);

  return [
    `c_{${row + 1}${col + 1}} = ${terms.join(" + ")}`,
    `{\\color{green}${values.join(" {\\color{black}\\ +\\ } ")}} = {\\color{green}${total}}`,
  ].join(" = ");
}

export default function MatrixMultiplicationSlide() {
  const [activeMode, setActiveMode] = useState<ModeId>("ordinary");
  const [selectedEntry, setSelectedEntry] = useState<MatrixPosition>([0, 0]);

  const mode = useMemo(
    () => modes.find((entry) => entry.id === activeMode) ?? modes[0],
    [activeMode],
  );

  const [selectedRow, selectedCol] = selectedEntry;
  const expression =
    activeMode === "ordinary"
      ? buildOrdinaryExpression(selectedRow, selectedCol)
      : buildMaxPlusExpression(selectedRow, selectedCol);
  const productOperator = activeMode === "ordinary" ? "\\times" : "\\otimes";

  return (
    <div className="w-full min-h-dvh px-4 pb-40 pt-28 sm:px-6 sm:pb-36 sm:pt-28">
      <motion.div
        variants={container}
        initial="hidden"
        animate="visible"
        className="mx-auto flex w-full max-w-5xl flex-col items-center gap-8"
      >
        <motion.div variants={item} className="max-w-3xl space-y-2 text-center">
          <p className="text-xs font-bold uppercase tracking-widest text-amber-600">
            Perbandingan Operasi
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Aljabar Max-Plus
          </h2>
          <p className="text-left text-sm leading-relaxed text-stone-600">
            Sebelum masuk ke hasil penelitian, kita bandingkan dulu dua cara
            mengalikan matriks. Bentuk matriksnya sama, tetapi aturan di
            dalamnya berubah. Pada aljabar biasa kita memakai kali lalu jumlah.
            Pada aljabar max-plus, kali diganti menjadi tambah dan jumlah
            diganti menjadi maksimum.
          </p>
        </motion.div>

        <motion.div
          variants={item}
          className="flex flex-wrap justify-center gap-3"
        >
          {modes.map((entry) => {
            const isActive = entry.id === activeMode;
            return (
              <button
                key={entry.id}
                type="button"
                onClick={() => setActiveMode(entry.id)}
                className={[
                  "rounded-full border px-4 py-2 text-sm font-semibold transition-colors",
                  isActive
                    ? entry.id === "ordinary"
                      ? "border-amber-500 bg-amber-500 text-white"
                      : "border-sky-600 bg-sky-600 text-white"
                    : "border-stone-300 bg-white text-stone-700 hover:border-stone-500 hover:text-stone-950",
                ].join(" ")}
              >
                {entry.label}
              </button>
            );
          })}
        </motion.div>

        <motion.div
          variants={item}
          className="grid w-full gap-4 lg:grid-cols-[minmax(0,1fr)_minmax(0,1.15fr)]"
        >
          <div className="min-w-0 space-y-4">
            <AnimatePresence mode="wait">
              <motion.div
                key={activeMode}
                initial={{
                  opacity: 0,
                  x: activeMode === "ordinary" ? -24 : 24,
                  filter: "blur(6px)",
                  scale: 0.98,
                }}
                animate={{ opacity: 1, x: 0, filter: "blur(0px)", scale: 1 }}
                exit={{
                  opacity: 0,
                  x: activeMode === "ordinary" ? 24 : -24,
                  filter: "blur(6px)",
                  scale: 0.98,
                }}
                transition={{ duration: 0.24, ease: [0.16, 1, 0.3, 1] }}
                className="space-y-4"
              >
                <div className="rounded-lg border border-stone-200 bg-white p-5 shadow-sm">
                  <p className="text-xs font-bold uppercase tracking-widest text-stone-600">
                    Rumus Utama
                  </p>
                  <div className="mt-3 overflow-x-auto">
                    <MathBlock
                      tex={mode.formula}
                      display
                      className="text-stone-950"
                    />
                  </div>
                </div>
              </motion.div>
            </AnimatePresence>
          </div>

          <div className="min-w-0 rounded-lg border border-stone-200 bg-white p-5 shadow-sm">
            <p className="text-xs font-bold uppercase tracking-widest text-stone-600">
              Ilustrasi Interaktif
            </p>
            <div className="mt-3 overflow-x-auto">
              <MathBlock tex={expression} display className="text-stone-950" />
            </div>
            <div className="mt-4 overflow-x-auto overflow-y-hidden">
              <div className="flex min-w-max items-center justify-center gap-2 px-1 py-2 sm:gap-3">
                <MatrixView
                  title="A"
                  accent="amber"
                  matrix={matrixA}
                  activeRow={selectedRow}
                />
                <div className="pt-4 shrink-0 px-0.5 text-stone-900 text-[1.5rem] sm:text-[2rem]">
                  <MathBlock tex={productOperator} />
                </div>
                <MatrixView
                  title="B"
                  accent="sky"
                  matrix={matrixB}
                  activeCol={selectedCol}
                />
                <div className="pt-4 shrink-0 px-0.5 text-stone-900 text-[1.5rem] sm:text-[2rem]">
                  <MathBlock tex="=" />
                </div>
                <MatrixView
                  title="C"
                  accent="emerald"
                  matrix={mode.result}
                  selectedCell={selectedEntry}
                  onSelect={setSelectedEntry}
                />
              </div>
            </div>
            <p className="mt-4 text-center text-sm leading-relaxed text-stone-600">
              Klik salah satu entri pada matriks{" "}
              <span className="font-semibold text-emerald-700">C</span>. Baris
              di <span className="font-semibold text-amber-700">A</span>, kolom
              di <span className="font-semibold text-sky-700">B</span>, dan
              ekspresi hitungnya akan ikut berubah.
            </p>
          </div>
        </motion.div>
      </motion.div>
    </div>
  );
}
