"use client";

import { motion } from "framer-motion";
import SudokuGrid from "../Sudoku/SudokuGrid";

interface SudokuSlideProps {
  onSolved: () => void;
}

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

export default function SudokuPuzzleSlide({ onSolved }: SudokuSlideProps) {
  return (
    <div className="w-full min-h-dvh px-4 pt-24 pb-24 sm:px-6">
      <motion.div
        variants={container}
        initial="hidden"
        animate="visible"
        className="mx-auto flex w-full max-w-3xl flex-col items-center gap-6"
      >
        <motion.div variants={item} className="space-y-2 text-center">
          <p className="text-xs font-bold uppercase tracking-widest text-amber-600">
            Puzzle
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Sudoku (数独)
          </h2>
          <p className="text-left text-sm leading-relaxed text-stone-600">
            Permainan ini berasal dari teka-teki angka yang berkembang di Barat,
            lalu dipopulerkan di Jepang oleh perusahaan penerbit Nikoli pada
            tahun 1980-an. Mereka menyingkat nama panjang 『数字は独身に限る』 (
            <i>sūji wa dokushin ni kagiru</i>) menjadi 『数独』(<i>sūdoku</i>),
            yang kemudian terkenal ke seluruh dunia sebagai &quot;Sudoku&quot;.
          </p>
        </motion.div>

        <motion.div
          variants={item}
          className="w-full rounded-lg border border-stone-200 bg-white p-5 shadow-sm"
        >
          <p className="mb-3 text-xs font-bold uppercase tracking-wider text-stone-600">
            Aturan Sudoku
          </p>
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
            {[
              {
                icon: "R",
                label: "Setiap baris",
                desc: "berisi angka 1-9 tepat satu kali",
              },
              {
                icon: "C",
                label: "Setiap kolom",
                desc: "berisi angka 1-9 tepat satu kali",
              },
              {
                icon: "B",
                label: "Setiap region 3x3",
                desc: "berisi angka 1-9 tepat satu kali",
              },
            ].map((rule) => (
              <div key={rule.label} className="flex items-start gap-3">
                <span className="mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-amber-400/15 text-sm font-bold text-amber-700">
                  {rule.icon}
                </span>
                <div>
                  <p className="text-sm font-semibold text-stone-900">
                    {rule.label}
                  </p>
                  <p className="text-xs leading-relaxed text-stone-600">
                    {rule.desc}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </motion.div>

        <motion.div variants={item} className="flex w-full justify-center">
          <SudokuGrid onSolved={onSolved} />
        </motion.div>
      </motion.div>
    </div>
  );
}
