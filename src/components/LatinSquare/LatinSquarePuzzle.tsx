"use client";

import {
  type CSSProperties,
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
} from "react";
import { AnimatePresence, motion } from "framer-motion";

const headingClass = "font-[family:var(--font-heading)]";
const gridClass =
  "grid w-full overflow-hidden rounded-lg border-2 border-stone-500 bg-stone-50";
const baseCellClass =
  "relative flex aspect-square select-none touch-manipulation items-center justify-center border border-stone-300 text-stone-900 outline-none";
const numberKeyClass =
  "h-11 min-w-11 rounded-lg border border-stone-300 bg-white px-3 text-sm font-bold text-stone-900 transition-all duration-150 hover:-translate-y-px hover:border-sky-600 hover:bg-sky-600 hover:text-white active:scale-95 disabled:cursor-not-allowed disabled:opacity-30 disabled:hover:translate-y-0 disabled:hover:border-stone-300 disabled:hover:bg-white disabled:hover:text-stone-900";
const clearKeyClass =
  "border-rose-400 text-rose-600 hover:border-rose-600 hover:bg-rose-600 hover:text-white disabled:hover:border-rose-400 disabled:hover:bg-white disabled:hover:text-rose-600";
const confettiColors = [
  "bg-amber-400",
  "bg-sky-500",
  "bg-emerald-500",
  "bg-amber-200",
  "bg-rose-400",
  "bg-indigo-400",
];

const puzzleSizeClasses: Record<
  number,
  { gridWidth: string; cellText: string }
> = {
  3: {
    gridWidth: "max-w-[210px] sm:max-w-[240px]",
    cellText: "text-base sm:text-lg",
  },
  4: {
    gridWidth: "max-w-[236px] sm:max-w-[276px]",
    cellText: "text-sm sm:text-base",
  },
  5: {
    gridWidth: "max-w-[255px] sm:max-w-[300px]",
    cellText: "text-sm sm:text-base",
  },
};

type PuzzleId = "ordo3" | "ordo4" | "ordo5";

interface LatinSquarePuzzleData {
  id: PuzzleId;
  label: string;
  order: number;
  solution: number[][];
  description: string;
  clueCount: number;
}

const latinSquarePuzzles: LatinSquarePuzzleData[] = [
  {
    id: "ordo3",
    label: "Orde 3",
    order: 3,
    solution: [
      [1, 2, 3],
      [2, 3, 1],
      [3, 1, 2],
    ],
    description:
      "Mulai dari contoh kecil dulu. Simbol yang dipakai hanya 1, 2, dan 3.",
    clueCount: 4,
  },
  {
    id: "ordo4",
    label: "Orde 4",
    order: 4,
    solution: [
      [1, 2, 3, 4],
      [2, 3, 4, 1],
      [3, 4, 1, 2],
      [4, 1, 2, 3],
    ],
    description:
      "Di ordo 4, pola mulai terasa lebih mirip matriks penuh yang nanti muncul di contoh-contoh penelitian.",
    clueCount: 6,
  },
  {
    id: "ordo5",
    label: "Orde 5",
    order: 5,
    solution: [
      [1, 2, 3, 4, 5],
      [2, 3, 4, 5, 1],
      [3, 4, 5, 1, 2],
      [4, 5, 1, 2, 3],
      [5, 1, 2, 3, 4],
    ],
    description:
      "Kalau pola dasarnya sudah kebaca, coba lanjut ke ordo 5 dengan simbol 1 sampai 5.",
    clueCount: 9,
  },
];

function cloneGrid(grid: (number | null)[][]) {
  return grid.map((row) => [...row]);
}

function shuffle<T>(items: T[]) {
  const next = [...items];
  for (let index = next.length - 1; index > 0; index--) {
    const swapIndex = Math.floor(Math.random() * (index + 1));
    [next[index], next[swapIndex]] = [next[swapIndex], next[index]];
  }
  return next;
}

function createRandomGiven(solution: number[][], clueCount: number) {
  const order = solution.length;
  const given = solution.map((row) => row.map(() => null as number | null));
  const selected = new Set<string>();
  const rowCounts = Array.from({ length: order }, () => 0);
  const colCounts = Array.from({ length: order }, () => 0);

  const rows = shuffle(Array.from({ length: order }, (_, index) => index));
  const cols = shuffle(Array.from({ length: order }, (_, index) => index));

  rows.forEach((row, index) => {
    const preferredCol = cols[index % cols.length];
    const fallbackCols = shuffle(
      Array.from({ length: order }, (_, colIndex) => colIndex).filter(
        (col) => col !== preferredCol,
      ),
    );
    const candidates = [preferredCol, ...fallbackCols];
    const col =
      candidates.find((candidate) => colCounts[candidate] === 0) ??
      candidates[0];
    const key = `${row}-${col}`;
    if (selected.has(key)) return;

    selected.add(key);
    rowCounts[row] += 1;
    colCounts[col] += 1;
    given[row][col] = solution[row][col];
  });

  const remainingPositions = shuffle(
    Array.from(
      { length: order * order },
      (_, index) => [Math.floor(index / order), index % order] as const,
    ).filter(([row, col]) => !selected.has(`${row}-${col}`)),
  );

  for (const [row, col] of remainingPositions) {
    if (selected.size >= clueCount) break;

    selected.add(`${row}-${col}`);
    rowCounts[row] += 1;
    colCounts[col] += 1;
    given[row][col] = solution[row][col];
  }

  return given;
}

function buildLockedCells(given: (number | null)[][]) {
  return given.map((row) => row.map((cell) => cell !== null));
}

function cellHasConflict(grid: (number | null)[][], row: number, col: number) {
  const value = grid[row][col];
  if (value === null) return false;

  for (let index = 0; index < grid.length; index++) {
    if (index !== col && grid[row][index] === value) return true;
    if (index !== row && grid[index][col] === value) return true;
  }

  return false;
}

function isPuzzleSolved(
  grid: (number | null)[][],
  solution: number[][],
  order: number,
) {
  for (let row = 0; row < order; row++) {
    for (let col = 0; col < order; col++) {
      if (grid[row][col] !== solution[row][col]) {
        return false;
      }
    }
  }

  return true;
}

function getCellStyle(options: {
  isSelected: boolean;
  highlighted: boolean;
  conflict: boolean;
}): CSSProperties {
  const style: CSSProperties = {};

  if (options.isSelected) {
    style.backgroundColor = "var(--color-indigo-300)";
  } else if (options.highlighted) {
    style.backgroundColor = "var(--color-sky-200)";
  }

  if (options.conflict) {
    style.backgroundColor = "var(--color-rose-200)";
    style.color = "var(--color-rose-700)";
  }

  return style;
}

function buildConfetti() {
  return Array.from({ length: 36 }, (_, index) => ({
    id: index,
    left: Math.random() * 100,
    colorClass: confettiColors[index % confettiColors.length],
    delay: Math.random() * 0.8,
    size: 7 + Math.random() * 7,
    duration: 2.1 + Math.random(),
  }));
}

function getPuzzleSizeClass(order: number) {
  return (
    puzzleSizeClasses[order] ?? {
      gridWidth: "max-w-[255px] sm:max-w-[300px]",
      cellText: "text-sm sm:text-base",
    }
  );
}

export default function LatinSquarePuzzle() {
  const [activePuzzleId, setActivePuzzleId] = useState<PuzzleId>("ordo3");
  const activePuzzle = useMemo(
    () =>
      latinSquarePuzzles.find((puzzle) => puzzle.id === activePuzzleId) ??
      latinSquarePuzzles[0],
    [activePuzzleId],
  );
  const [givenGrid, setGivenGrid] = useState<(number | null)[][]>(() =>
    createRandomGiven(activePuzzle.solution, activePuzzle.clueCount),
  );
  const [grid, setGrid] = useState<(number | null)[][]>(() =>
    cloneGrid(givenGrid),
  );
  const [lockedCells, setLockedCells] = useState<boolean[][]>(() =>
    buildLockedCells(givenGrid),
  );
  const [selected, setSelected] = useState<[number, number] | null>(null);
  const [solved, setSolved] = useState(false);
  const [showSuccess, setShowSuccess] = useState(false);
  const [confetti, setConfetti] = useState<
    {
      id: number;
      left: number;
      colorClass: string;
      delay: number;
      size: number;
      duration: number;
    }[]
  >([]);
  const closeTimer = useRef<ReturnType<typeof setTimeout> | null>(null);

  const resetPuzzle = useCallback((puzzle: LatinSquarePuzzleData) => {
    const nextGiven = createRandomGiven(puzzle.solution, puzzle.clueCount);
    setGivenGrid(nextGiven);
    setGrid(cloneGrid(nextGiven));
    setLockedCells(buildLockedCells(nextGiven));
    setSelected(null);
    setSolved(false);
    setShowSuccess(false);
    setConfetti([]);
    if (closeTimer.current) {
      clearTimeout(closeTimer.current);
      closeTimer.current = null;
    }
  }, []);

  useEffect(() => {
    return () => {
      if (closeTimer.current) clearTimeout(closeTimer.current);
    };
  }, []);

  const completePuzzle = useCallback(() => {
    setSolved(true);
    setShowSuccess(true);
    setSelected(null);
    setConfetti(buildConfetti());
    if (closeTimer.current) clearTimeout(closeTimer.current);
    closeTimer.current = setTimeout(() => {
      setShowSuccess(false);
      closeTimer.current = null;
    }, 2200);
  }, []);

  const dismissSuccess = useCallback(() => {
    setShowSuccess(false);
    if (closeTimer.current) {
      clearTimeout(closeTimer.current);
      closeTimer.current = null;
    }
  }, []);

  const inputNumber = useCallback(
    (value: number | null) => {
      if (!selected || solved) return;

      const [row, col] = selected;
      if (lockedCells[row][col]) return;

      const nextGrid = cloneGrid(grid);
      nextGrid[row][col] = value;
      setGrid(nextGrid);

      if (
        value !== null &&
        isPuzzleSolved(nextGrid, activePuzzle.solution, activePuzzle.order)
      ) {
        completePuzzle();
      }
    },
    [
      activePuzzle.order,
      activePuzzle.solution,
      completePuzzle,
      grid,
      lockedCells,
      selected,
      solved,
    ],
  );

  const fillHint = useCallback(() => {
    if (solved) return;

    const candidates: [number, number][] = [];
    for (let row = 0; row < activePuzzle.order; row++) {
      for (let col = 0; col < activePuzzle.order; col++) {
        if (lockedCells[row][col]) continue;
        if (grid[row][col] === activePuzzle.solution[row][col]) continue;
        candidates.push([row, col]);
      }
    }

    if (candidates.length === 0) return;

    const [row, col] =
      candidates[Math.floor(Math.random() * candidates.length)];
    const nextGrid = cloneGrid(grid);
    const nextLocked = lockedCells.map((line) => [...line]);
    nextGrid[row][col] = activePuzzle.solution[row][col];
    nextLocked[row][col] = true;

    setGrid(nextGrid);
    setLockedCells(nextLocked);
    setSelected(null);

    if (isPuzzleSolved(nextGrid, activePuzzle.solution, activePuzzle.order)) {
      completePuzzle();
    }
  }, [
    activePuzzle.order,
    activePuzzle.solution,
    completePuzzle,
    grid,
    lockedCells,
    solved,
  ]);

  const revealSolution = useCallback(() => {
    if (solved) return;

    setGrid(activePuzzle.solution.map((row) => [...row]));
    setLockedCells(activePuzzle.solution.map((row) => row.map(() => true)));
    completePuzzle();
  }, [activePuzzle.solution, completePuzzle, solved]);

  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if (solved) return;

      if (event.key === "Escape") {
        setSelected(null);
        return;
      }

      if (!selected) return;

      const [row, col] = selected;
      if (event.key === "ArrowUp") {
        event.preventDefault();
        if (row > 0) setSelected([row - 1, col]);
        return;
      }
      if (event.key === "ArrowDown") {
        event.preventDefault();
        if (row < activePuzzle.order - 1) setSelected([row + 1, col]);
        return;
      }
      if (event.key === "ArrowLeft") {
        event.preventDefault();
        if (col > 0) setSelected([row, col - 1]);
        return;
      }
      if (event.key === "ArrowRight") {
        event.preventDefault();
        if (col < activePuzzle.order - 1) setSelected([row, col + 1]);
        return;
      }

      const parsed = Number(event.key);
      if (
        Number.isInteger(parsed) &&
        parsed >= 1 &&
        parsed <= activePuzzle.order
      ) {
        inputNumber(parsed);
        return;
      }

      if (
        event.key === "Backspace" ||
        event.key === "Delete" ||
        event.key === "0"
      ) {
        inputNumber(null);
      }
    };

    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [activePuzzle.order, inputNumber, selected, solved]);

  const isHighlighted = useCallback(
    (row: number, col: number) => {
      if (!selected) return false;

      const [selectedRow, selectedCol] = selected;
      return row === selectedRow || col === selectedCol;
    },
    [selected],
  );

  const handlePuzzleChange = useCallback(
    (puzzleId: PuzzleId) => {
      if (puzzleId === activePuzzleId) return;

      const nextPuzzle =
        latinSquarePuzzles.find((puzzle) => puzzle.id === puzzleId) ??
        latinSquarePuzzles[0];
      setActivePuzzleId(puzzleId);
      resetPuzzle(nextPuzzle);
    },
    [activePuzzleId, resetPuzzle],
  );

  const puzzleSize = getPuzzleSizeClass(activePuzzle.order);

  return (
    <div className="flex w-full flex-col items-center gap-5">
      <div className="w-full rounded-lg border border-stone-200 bg-white p-5 shadow-sm">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
          <div className="space-y-2">
            <p className="text-xs font-bold uppercase tracking-wider text-stone-600">
              Coba Susun Latin Square
            </p>
            <p className="text-sm leading-relaxed text-stone-600">
              Lengkapi matriks yang sudah dimulai. Di sini tidak ada aturan
              region 3x3, jadi ceknya hanya benturan pada baris dan kolom.
            </p>
          </div>

          <div className="flex flex-wrap gap-2 pt-1">
            {latinSquarePuzzles.map((puzzle) => {
              const isActive = puzzle.id === activePuzzleId;
              return (
                <button
                  key={puzzle.id}
                  type="button"
                  onClick={() => handlePuzzleChange(puzzle.id)}
                  className={[
                    "rounded-lg border px-3 py-2 text-sm font-bold transition-colors duration-150",
                    isActive
                      ? "border-sky-600 bg-sky-600 text-white"
                      : "border-stone-300 bg-white text-stone-700 hover:border-sky-600 hover:text-sky-700",
                  ].join(" ")}
                >
                  {puzzle.label}
                </button>
              );
            })}
          </div>
        </div>
      </div>

      <div
        className={[
          gridClass,
          puzzleSize.gridWidth,
        ].join(" ")}
        style={{
          gridTemplateColumns: `repeat(${activePuzzle.order}, minmax(0, 1fr))`,
        }}
      >
        {grid.map((row, rowIndex) =>
          row.map((cell, colIndex) => {
            const isOriginallyGiven = givenGrid[rowIndex][colIndex] !== null;
            const isLocked = lockedCells[rowIndex][colIndex];
            const isSelected =
              selected?.[0] === rowIndex && selected?.[1] === colIndex;
            const highlighted =
              !isSelected && isHighlighted(rowIndex, colIndex);
            const conflict = cellHasConflict(grid, rowIndex, colIndex);
            const isCorrectPlayerEntry =
              !isLocked &&
              cell !== null &&
              cell === activePuzzle.solution[rowIndex][colIndex] &&
              !conflict;
            const isHintedCell = isLocked && !isOriginallyGiven;

            const cellClass = [
              baseCellClass,
              puzzleSize.cellText,
              isOriginallyGiven
                ? "cursor-default bg-stone-200 font-extrabold text-stone-950"
                : isHintedCell
                  ? "cursor-default bg-sky-100 font-extrabold text-sky-700"
                  : "cursor-pointer bg-stone-50 hover:bg-amber-50",
              isCorrectPlayerEntry
                ? "font-extrabold text-emerald-700"
                : "font-extrabold",
              conflict ? "font-extrabold text-rose-700" : "",
            ].join(" ");

            return (
              <motion.button
                key={`${activePuzzle.id}-${rowIndex}-${colIndex}`}
                type="button"
                style={getCellStyle({
                  isSelected,
                  highlighted,
                  conflict,
                })}
                onClick={() => {
                  if (isLocked || solved) return;
                  setSelected((current) =>
                    current?.[0] === rowIndex && current?.[1] === colIndex
                      ? null
                      : [rowIndex, colIndex],
                  );
                }}
                animate={conflict ? { x: [0, -5, 5, -3, 3, 0] } : undefined}
                transition={
                  conflict ? { duration: 0.35, ease: "easeInOut" } : undefined
                }
                className={cellClass}
                aria-label={`R${rowIndex + 1}C${colIndex + 1}${cell ? ` = ${cell}` : " kosong"}`}
              >
                {cell !== null && <span>{cell}</span>}
              </motion.button>
            );
          }),
        )}
      </div>

      {!solved && (
        <>
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="flex flex-wrap items-center justify-center gap-2"
          >
            {Array.from(
              { length: activePuzzle.order },
              (_, index) => index + 1,
            ).map((value) => (
              <button
                key={value}
                type="button"
                onClick={() => inputNumber(value)}
                disabled={!selected}
                className={numberKeyClass}
              >
                {value}
              </button>
            ))}
            <button
              type="button"
              onClick={() => inputNumber(null)}
              disabled={!selected}
              title="Hapus"
              className={`${numberKeyClass} ${clearKeyClass}`}
            >
              x
            </button>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.28 }}
            className="flex flex-wrap items-center justify-center gap-2"
          >
            <button
              type="button"
              onClick={fillHint}
              className="rounded-lg border border-sky-300 bg-sky-50 px-4 py-2 text-sm font-bold text-sky-700 transition-colors duration-150 hover:bg-sky-100"
            >
              Hint
            </button>
            <button
              type="button"
              onClick={revealSolution}
              className="rounded-lg border border-amber-300 bg-amber-50 px-4 py-2 text-sm font-bold text-amber-700 transition-colors duration-150 hover:bg-amber-100"
            >
              Selesaikan
            </button>
          </motion.div>
        </>
      )}

      {!solved && (
        <p className="text-center text-xs text-stone-600">
          {selected
            ? `Pilih angka 1-${activePuzzle.order}, atau pakai keyboard dan tombol panah.`
            : "Klik sel kosong untuk mulai mengisi."}
        </p>
      )}

      <AnimatePresence>
        {showSuccess && (
          <>
            {confetti.map((piece) => (
              <motion.div
                key={piece.id}
                initial={{ y: -120, rotate: 0, opacity: 1 }}
                animate={{ y: "120vh", rotate: 720, opacity: 0 }}
                transition={{
                  duration: piece.duration,
                  ease: "easeIn",
                  delay: piece.delay,
                }}
                className={`pointer-events-none fixed top-[-12px] z-[300] rounded-sm ${piece.colorClass}`}
                style={{
                  left: `${piece.left}%`,
                  width: piece.size,
                  height: piece.size,
                }}
              />
            ))}
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={dismissSuccess}
              className="fixed inset-0 z-[200] flex items-center justify-center bg-stone-950/45 backdrop-blur-sm"
            >
              <motion.div
                initial={{ scale: 0.75, opacity: 0, y: 30 }}
                animate={{ scale: 1, opacity: 1, y: 0 }}
                exit={{ scale: 0.9, opacity: 0 }}
                transition={{
                  type: "spring",
                  stiffness: 220,
                  damping: 22,
                  delay: 0.15,
                }}
                className="mx-4 max-w-sm rounded-2xl bg-white p-8 text-center shadow-2xl"
              >
                <span className="mb-4 block text-5xl">OK</span>
                <h3
                  className={`${headingClass} mb-3 text-2xl font-bold text-emerald-500`}
                >
                  Latin Square Selesai!
                </h3>
                <p className="text-sm leading-relaxed text-stone-600">
                  Setiap baris dan kolom sudah terisi benar. Sekarang pola Latin
                  square-nya sudah kelihatan.
                </p>
              </motion.div>
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </div>
  );
}
