"use client";

import { useState, useCallback, useEffect, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  BLOCK_SIZE,
  GRID_SIZE,
  mainPuzzle,
  initializeGrid,
  cellHasConflict,
  isGridComplete,
} from "./sudokuUtils";

interface SudokuGridProps {
  onSolved: () => void;
}

const headingClass = "font-[family:var(--font-heading)]";
const gridClass =
  "grid w-full max-w-[350px] overflow-hidden rounded-lg border-2 border-stone-500 bg-stone-50 sm:max-w-[430px]";
const baseCellClass =
  "relative flex aspect-square select-none touch-manipulation items-center justify-center border border-stone-300 text-stone-900 outline-none";
const numberKeyClass =
  "h-11 w-11 rounded-lg border border-stone-300 bg-white text-sm font-bold text-stone-900 transition-all duration-150 hover:-translate-y-px hover:border-emerald-600 hover:bg-emerald-600 hover:text-white active:scale-95 disabled:cursor-not-allowed disabled:opacity-30 disabled:hover:translate-y-0 disabled:hover:border-stone-300 disabled:hover:bg-white disabled:hover:text-stone-900";
const clearKeyClass =
  "border-rose-400 text-rose-600 hover:border-rose-600 hover:bg-rose-600 hover:text-white disabled:hover:border-rose-400 disabled:hover:bg-white disabled:hover:text-rose-600";
const confettiColors = [
  "bg-amber-400",
  "bg-emerald-600",
  "bg-amber-200",
  "bg-emerald-400",
  "bg-rose-600",
  "bg-rose-300",
  "bg-amber-600",
];

function initializeLockedCells() {
  return mainPuzzle.given.map((row) => [...row]);
}

function buildConflictKeys(
  grid: (number | null)[][],
  anchor: [number, number] | null,
) {
  if (!anchor) return new Set<string>();

  const [row, col] = anchor;
  const value = grid[row][col];
  if (value === null) return new Set<string>();

  const keys = new Set<string>([`${row}-${col}`]);

  for (let index = 0; index < GRID_SIZE; index++) {
    if (index !== col && grid[row][index] === value) {
      keys.add(`${row}-${index}`);
    }
    if (index !== row && grid[index][col] === value) {
      keys.add(`${index}-${col}`);
    }
  }

  const startRow = Math.floor(row / BLOCK_SIZE) * BLOCK_SIZE;
  const startCol = Math.floor(col / BLOCK_SIZE) * BLOCK_SIZE;
  for (let currentRow = startRow; currentRow < startRow + BLOCK_SIZE; currentRow++) {
    for (
      let currentCol = startCol;
      currentCol < startCol + BLOCK_SIZE;
      currentCol++
    ) {
      if (
        (currentRow !== row || currentCol !== col) &&
        grid[currentRow][currentCol] === value
      ) {
        keys.add(`${currentRow}-${currentCol}`);
      }
    }
  }

  return keys.size > 1 ? keys : new Set<string>();
}

function getCellStyle(
  row: number,
  col: number,
  options: {
    isSelected: boolean;
    highlighted: boolean;
    highlightedGiven: boolean;
    conflict: boolean;
    givenConflict: boolean;
    persistentConflict: boolean;
  },
): React.CSSProperties {
  const thinBorder = "1px solid var(--color-stone-300)";
  const thickBorder = "2px solid var(--color-stone-500)";
  const style: React.CSSProperties = {
    borderRight:
      col === GRID_SIZE - 1
        ? "none"
        : (col + 1) % BLOCK_SIZE === 0
          ? thickBorder
          : thinBorder,
    borderBottom:
      row === GRID_SIZE - 1
        ? "none"
        : (row + 1) % BLOCK_SIZE === 0
          ? thickBorder
          : thinBorder,
    borderLeft: col === 0 ? "none" : undefined,
    borderTop: row === 0 ? "none" : undefined,
  };

  if (options.isSelected) {
    style.backgroundColor = "var(--color-indigo-300)";
  } else if (options.highlighted) {
    style.backgroundColor = options.highlightedGiven
      ? "var(--color-sky-300)"
      : "var(--color-sky-200)";
  }

  if (options.persistentConflict) {
    style.backgroundColor = "var(--color-rose-200)";
    style.color = "var(--color-rose-700)";
  }

  if (options.conflict) {
    style.backgroundColor = options.givenConflict
      ? "var(--color-rose-300)"
      : "var(--color-rose-200)";
    style.color = options.givenConflict
      ? "var(--color-rose-900)"
      : "var(--color-rose-700)";
  }

  return style;
}

function buildConfetti() {
  return Array.from({ length: 50 }, (_, i) => ({
    id: i,
    left: Math.random() * 100,
    colorClass: confettiColors[i % confettiColors.length],
    delay: Math.random() * 1.2,
    size: 7 + Math.random() * 9,
    duration: 2.5 + Math.random(),
  }));
}

export default function SudokuGrid({ onSolved }: SudokuGridProps) {
  const [grid, setGrid] = useState<(number | null)[][]>(() =>
    initializeGrid(mainPuzzle),
  );
  const [lockedCells, setLockedCells] = useState<boolean[][]>(() =>
    initializeLockedCells(),
  );
  const [selected, setSelected] = useState<[number, number] | null>(null);
  const [conflictAnchor, setConflictAnchor] = useState<[number, number] | null>(
    null,
  );
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
  const unlockTimer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const conflictTimer = useRef<ReturnType<typeof setTimeout> | null>(null);

  const completePuzzle = useCallback(() => {
    if (solved) return;

    setSolved(true);
    setShowSuccess(true);
    setSelected(null);
    setConflictAnchor(null);
    setConfetti(buildConfetti());
    unlockTimer.current = setTimeout(() => onSolved(), 2200);
  }, [onSolved, solved]);

  const dismissSuccess = useCallback(() => {
    setShowSuccess(false);
    if (unlockTimer.current) {
      clearTimeout(unlockTimer.current);
      unlockTimer.current = null;
    }
    onSolved();
  }, [onSolved]);

  const clearConflictFeedback = useCallback(() => {
    setConflictAnchor(null);
  }, []);

  const inputNumber = useCallback(
    (num: number | null) => {
      if (!selected || solved) return;

      const [r, c] = selected;
      if (lockedCells[r][c]) return;

      const next = grid.map((row) => [...row]);
      next[r][c] = num;
      setGrid(next);

      if (num !== null && cellHasConflict(next, r, c)) {
        setConflictAnchor([r, c]);
      } else {
        setConflictAnchor(null);
      }

      if (num !== null && isGridComplete(next)) {
        completePuzzle();
      }
    },
    [completePuzzle, grid, lockedCells, selected, solved],
  );

  const fillHint = useCallback(() => {
    if (solved) return;

    const candidates: [number, number][] = [];
    for (let r = 0; r < GRID_SIZE; r++) {
      for (let c = 0; c < GRID_SIZE; c++) {
        if (lockedCells[r][c]) continue;
        if (grid[r][c] === mainPuzzle.solution[r][c]) continue;
        candidates.push([r, c]);
      }
    }

    if (candidates.length === 0) return;

    const [r, c] = candidates[Math.floor(Math.random() * candidates.length)];
    const nextGrid = grid.map((row) => [...row]);
    const nextLocked = lockedCells.map((row) => [...row]);
    nextGrid[r][c] = mainPuzzle.solution[r][c];
    nextLocked[r][c] = true;

    setGrid(nextGrid);
    setLockedCells(nextLocked);
    setSelected(null);
    setConflictAnchor(null);

    if (isGridComplete(nextGrid)) {
      completePuzzle();
    }
  }, [completePuzzle, grid, lockedCells, solved]);

  const revealSolution = useCallback(() => {
    if (solved) return;

    setGrid(mainPuzzle.solution.map((row) => [...row]));
    setLockedCells(mainPuzzle.solution.map((row) => row.map(() => true)));
    setConflictAnchor(null);
    completePuzzle();
  }, [completePuzzle, solved]);

  useEffect(() => {
    return () => {
      if (unlockTimer.current) clearTimeout(unlockTimer.current);
      if (conflictTimer.current) clearTimeout(conflictTimer.current);
    };
  }, []);

  useEffect(() => {
    if (!conflictAnchor) {
      if (conflictTimer.current) {
        clearTimeout(conflictTimer.current);
        conflictTimer.current = null;
      }
      return;
    }

    if (conflictTimer.current) clearTimeout(conflictTimer.current);
    conflictTimer.current = setTimeout(() => {
      setConflictAnchor(null);
      conflictTimer.current = null;
    }, 1600);

    return () => {
      if (conflictTimer.current) {
        clearTimeout(conflictTimer.current);
        conflictTimer.current = null;
      }
    };
  }, [conflictAnchor]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (!selected || solved) return;

      const [r, c] = selected;
      if (e.key === "ArrowUp") {
        e.preventDefault();
        if (r > 0) {
          clearConflictFeedback();
          setSelected([r - 1, c]);
        }
      } else if (e.key === "ArrowDown") {
        e.preventDefault();
        if (r < GRID_SIZE - 1) {
          clearConflictFeedback();
          setSelected([r + 1, c]);
        }
      } else if (e.key === "ArrowLeft") {
        e.preventDefault();
        if (c > 0) {
          clearConflictFeedback();
          setSelected([r, c - 1]);
        }
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        if (c < GRID_SIZE - 1) {
          clearConflictFeedback();
          setSelected([r, c + 1]);
        }
      } else if ("123456789".includes(e.key)) {
        inputNumber(Number(e.key));
      } else if (e.key === "Backspace" || e.key === "Delete" || e.key === "0") {
        inputNumber(null);
      } else if (e.key === "Escape") {
        clearConflictFeedback();
        setSelected(null);
      }
    };

    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [clearConflictFeedback, inputNumber, selected, solved]);

  const isHighlighted = (r: number, c: number) => {
    if (!selected) return false;

    const [sr, sc] = selected;
    if (r === sr || c === sc) return true;

    return (
      Math.floor(r / BLOCK_SIZE) === Math.floor(sr / BLOCK_SIZE) &&
      Math.floor(c / BLOCK_SIZE) === Math.floor(sc / BLOCK_SIZE)
    );
  };

  const conflictKeys = buildConflictKeys(grid, conflictAnchor);

  return (
    <div className="flex flex-col items-center gap-5 w-full">
      <div
        className={gridClass}
        style={{ gridTemplateColumns: "repeat(9, minmax(0, 1fr))" }}
      >
        {grid.map((row, r) =>
          row.map((cell, c) => {
            const isOriginallyGiven = mainPuzzle.given[r][c];
            const isLocked = lockedCells[r][c];
            const isSelected = selected?.[0] === r && selected?.[1] === c;
            const highlighted = !isSelected && isHighlighted(r, c);
            const highlightedGiven = highlighted && isOriginallyGiven;
            const conflict = conflictKeys.has(`${r}-${c}`);
            const givenConflict = conflict && isOriginallyGiven;
            const actualConflict = cellHasConflict(grid, r, c);
            const persistentConflict =
              !isLocked && cell !== null && actualConflict;
            const isCorrectPlayerEntry =
              !isLocked &&
              cell !== null &&
              cell === mainPuzzle.solution[r][c] &&
              !actualConflict;
            const isHintedCell = isLocked && !isOriginallyGiven;

            const cellClass = [
              baseCellClass,
              isOriginallyGiven
                ? conflict
                  ? "cursor-default bg-rose-300 font-extrabold text-rose-900"
                  : "cursor-default bg-stone-200 font-extrabold text-stone-950"
                : isHintedCell
                  ? "cursor-default bg-sky-100 font-extrabold text-sky-700"
                  : "cursor-pointer bg-stone-50 hover:bg-amber-50",
              isCorrectPlayerEntry
                ? "font-extrabold text-emerald-700"
                : "font-extrabold",
              conflict || persistentConflict ? "font-extrabold text-rose-700" : "",
            ].join(" ");

            return (
              <motion.button
                key={`${r}-${c}`}
                style={getCellStyle(r, c, {
                  isSelected,
                  highlighted,
                  highlightedGiven,
                  conflict,
                  givenConflict,
                  persistentConflict,
                })}
                onClick={() => {
                  if (isLocked || solved) return;
                  if (conflictAnchor) {
                    clearConflictFeedback();
                  }
                  setSelected((current) =>
                    current?.[0] === r && current?.[1] === c ? null : [r, c],
                  );
                }}
                animate={conflict ? { x: [0, -5, 5, -3, 3, 0] } : undefined}
                transition={
                  conflict ? { duration: 0.35, ease: "easeInOut" } : undefined
                }
                className={cellClass}
                aria-label={`R${r + 1}C${c + 1}${cell ? " = " + cell : " kosong"}`}
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
            className="grid grid-cols-5 gap-2 sm:flex sm:justify-center"
          >
            {[1, 2, 3, 4, 5, 6, 7, 8, 9].map((num) => (
              <button
                key={num}
                onClick={() => inputNumber(num)}
                disabled={!selected}
                className={numberKeyClass}
              >
                {num}
              </button>
            ))}
            <button
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

      <AnimatePresence>
        {showSuccess && (
          <>
            {confetti.map((p) => (
              <motion.div
                key={p.id}
                initial={{ y: -120, rotate: 0, opacity: 1 }}
                animate={{ y: "120vh", rotate: 720, opacity: 0 }}
                transition={{
                  duration: p.duration,
                  ease: "easeIn",
                  delay: p.delay,
                }}
                className={`pointer-events-none fixed top-[-12px] z-[300] rounded-sm ${p.colorClass}`}
                style={{
                  left: `${p.left}%`,
                  width: p.size,
                  height: p.size,
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
                  Puzzle Selesai!
                </h3>
                <p className="text-sm leading-relaxed text-stone-600">
                  Setiap baris, kolom, dan region 3x3 sudah terisi benar.
                  Sekarang kita bisa lanjut ke ide Latin Square.
                </p>
              </motion.div>
            </motion.div>
          </>
        )}
      </AnimatePresence>
      {!solved && (
        <p className="text-center text-xs text-stone-600">
          {selected
            ? "Pilih angka 1-9, atau pakai keyboard dan tombol panah."
            : "Klik sel kosong untuk mulai mengisi."}
        </p>
      )}
    </div>
  );
}
