"use client";

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

const matrixA = "\\begin{bmatrix}1 & 2\\\\3 & 4\\end{bmatrix}";
const matrixB = "\\begin{bmatrix}5 & 6\\\\7 & 8\\end{bmatrix}";
const ordinaryResult = "\\begin{bmatrix}19 & 22\\\\43 & 50\\end{bmatrix}";
const maxPlusResult = "\\begin{bmatrix}9 & 10\\\\11 & 12\\end{bmatrix}";

const ordinaryFormula = "c_{ij} = \\sum_{k=1}^{n} a_{ik}b_{kj}";
const maxPlusFormula =
  "c_{ij} = \\bigoplus_{k=1}^{n}(a_{ik} \\otimes b_{kj}) = \\max_k(a_{ik}+b_{kj})";

const ordinaryExample = "c_{11} = (1\\times5) + (2\\times7) = 5 + 14 = 19";
const maxPlusExample = "c_{11} = \\max(1+5,\\ 2+7) = \\max(6, 9) = 9";

function ComparisonCard({
  title,
  accentClass,
  bulletClass,
  formula,
  example,
  result,
}: {
  title: string;
  accentClass: string;
  bulletClass: string;
  formula: string;
  example: string;
  result: string;
}) {
  return (
    <div className="rounded-lg border border-stone-200 bg-white p-5 shadow-sm">
      <div className="space-y-4">
        <div className="space-y-2">
          <p className={`text-xs font-bold uppercase tracking-widest ${accentClass}`}>
            {title}
          </p>
          <MathBlock tex={formula} display className="text-stone-950" />
        </div>

        <div className="space-y-2 text-sm leading-relaxed text-stone-600">
          <p className={bulletClass}>Gunakan matriks yang sama, tetapi aturannya berbeda.</p>
          <p>
            Matriks contoh:
            {" "}
            <span className="inline-block align-middle">
              <MathBlock
                tex={`A=${matrixA},\\quad B=${matrixB}`}
                className="text-stone-950"
              />
            </span>
          </p>
        </div>

        <div className="rounded-2xl border border-stone-200 bg-stone-50 px-4 py-4">
          <p className="mb-2 text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
            Contoh Entri
          </p>
          <MathBlock tex={example} display className="text-stone-950" />
        </div>

        <div className="rounded-2xl border border-stone-200 bg-stone-50 px-4 py-4">
          <p className="mb-2 text-xs font-bold uppercase tracking-[0.24em] text-stone-600">
            Hasil Matriks C
          </p>
          <MathBlock tex={`C=${result}`} display className="text-stone-950" />
        </div>
      </div>
    </div>
  );
}

export default function BasicVsMaxPlusSlide() {
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
            Aljabar Biasa vs Aljabar Max-Plus
          </h2>
          <p className="text-left text-sm leading-relaxed text-stone-600">
            Sebelum masuk ke hasil penelitian, kita bandingkan dulu dua cara
            mengalikan matriks. Bentuk matriksnya sama, tetapi operasi di
            dalamnya berubah. Pada aljabar biasa kita memakai kali lalu jumlah,
            sedangkan pada aljabar max-plus kita mengganti kali menjadi tambah
            dan jumlah menjadi maksimum.
          </p>
        </motion.div>

        <motion.div variants={item} className="grid w-full gap-4 lg:grid-cols-2">
          <ComparisonCard
            title="Aljabar Biasa"
            accentClass="text-amber-700"
            bulletClass="font-medium text-stone-700"
            formula={ordinaryFormula}
            example={ordinaryExample}
            result={ordinaryResult}
          />
          <ComparisonCard
            title="Aljabar Max-Plus"
            accentClass="text-sky-700"
            bulletClass="font-medium text-stone-700"
            formula={maxPlusFormula}
            example={maxPlusExample}
            result={maxPlusResult}
          />
        </motion.div>

        <motion.div
          variants={item}
          className="w-full rounded-lg border border-emerald-200 bg-emerald-50 px-5 py-4"
        >
          <p className="text-xs font-bold uppercase tracking-widest text-emerald-700">
            Inti Transisi
          </p>
          <p className="mt-2 text-sm leading-relaxed text-emerald-950">
            Perubahan aturan operasi inilah yang nanti dipakai saat Latin
            square ditulis dalam bentuk matriks permutasi max-plus. Jadi slide
            berikutnya bukan ganti topik, tetapi lanjutan langsung dari cara
            pandang ini.
          </p>
        </motion.div>
      </motion.div>
    </div>
  );
}
