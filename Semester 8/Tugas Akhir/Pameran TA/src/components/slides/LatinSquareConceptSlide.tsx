"use client";

import { motion } from "framer-motion";
import MathBlock from "@/components/ui/MathBlock";
import LatinSquarePuzzle from "@/components/LatinSquare/LatinSquarePuzzle";

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

const ruleCards = [
  {
    icon: "R",
    label: "Setiap baris",
    desc: "berisi semua simbol tepat satu kali",
  },
  {
    icon: "C",
    label: "Setiap kolom",
    desc: "berisi semua simbol tepat satu kali",
  },
] as const;

const latinSquareExamples = [
  {
    label: "Orde 3",
    desc: "Pada ordo 3, simbol 1, 2, dan 3 masing-masing muncul tepat satu kali di setiap baris dan kolom.",
    tex: "\\left[\\begin{array}{ccc}1 & 2 & 3\\\\2 & 3 & 1\\\\3 & 1 & 2\\end{array}\\right]",
  },
  {
    label: "Orde 4",
    desc: "Ini contoh yang tadi sempat ada: empat simbol tetap berputar sehingga setiap baris dan kolom berisi 1 sampai 4 tepat satu kali.",
    tex: "\\left[\\begin{array}{cccc}1 & 2 & 3 & 4\\\\2 & 3 & 4 & 1\\\\3 & 4 & 1 & 2\\\\4 & 1 & 2 & 3\\end{array}\\right]",
  },
  {
    label: "Orde 5",
    desc: "Saat naik ke ordo 5, prinsipnya tidak berubah, hanya ukuran matriks dan banyak simbolnya yang bertambah.",
    tex: "\\left[\\begin{array}{ccccc}1 & 2 & 3 & 4 & 5\\\\2 & 3 & 4 & 5 & 1\\\\3 & 4 & 5 & 1 & 2\\\\4 & 5 & 1 & 2 & 3\\\\5 & 1 & 2 & 3 & 4\\end{array}\\right]",
  },
] as const;

const latinSquareExamplesTex = latinSquareExamples
  .map((example) => example.tex)
  .join(",\\; ");

export default function LatinSquareConceptSlide() {
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
            Objek Penelitian
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Latin Square
          </h2>
          <p className="text-left text-sm leading-relaxed text-stone-600">
            Latin square hampir sama seperti Sudoku. Bedanya, aturan bahwa
            setiap region 3x3 harus memuat semua simbol dihapus. Jadi yang
            tersisa hanya dua syarat utama: setiap simbol muncul tepat satu kali
            pada setiap baris dan setiap kolom.
          </p>
          <p className="text-left text-sm leading-relaxed text-stone-600">
            Dengan cara pandang ini, Latin square bisa dianggap sebagai versi
            Sudoku yang lebih sederhana. Itulah sebabnya slide ini menjadi
            jembatan sebelum masuk ke pembahasan penelitian inti.
          </p>
        </motion.div>

        <motion.div
          variants={item}
          className="w-full rounded-lg border border-stone-200 bg-white p-5 shadow-sm"
        >
          <p className="mb-3 text-xs font-bold uppercase tracking-wider text-stone-600">
            Aturan Latin Square
          </p>
          <div className="grid grid-cols-1 gap-3 min-[520px]:grid-cols-2">
            {ruleCards.map((rule) => (
              <div key={rule.label} className="flex items-start gap-3">
                <span className="mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-md border border-sky-200 bg-sky-100 text-sm font-bold text-sky-800">
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

        <motion.div
          variants={item}
          className="w-full rounded-lg border border-stone-200 bg-white p-5 shadow-sm"
        >
          <p className="mb-3 text-xs font-bold uppercase tracking-wider text-stone-600">
            Contoh Latin Square
          </p>
          <div className="grid grid-cols-1 gap-4">
            <div className="rounded-2xl border border-stone-200 bg-stone-50 px-3 py-4 sm:px-4 sm:py-5">
              <div className="overflow-x-auto">
                <MathBlock
                  tex={latinSquareExamplesTex}
                  display
                  className="[&_.katex]:text-[0.68rem] sm:[&_.katex]:text-[0.82rem] md:[&_.katex]:text-[0.92rem] [&_.katex-display]:my-0 text-stone-950"
                />
              </div>
            </div>
          </div>
        </motion.div>

        <motion.div variants={item} className="w-full">
          <LatinSquarePuzzle />
        </motion.div>
      </motion.div>
    </div>
  );
}
