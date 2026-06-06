"use client";

import { useMemo, useState } from "react";
import { motion } from "framer-motion";
import ThesisMatrix from "./ThesisMatrix";

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

const exampleCases = [
  {
    id: "ordo3",
    label: "Ordo 3",
    tag: "Kasus terkecil",
    summary:
      "Pada ordo 3, struktur Latin square sangat ketat. Ini cocok untuk memperlihatkan mekanisme algoritma dalam bentuk paling ringkas.",
    a: [
      [1, 2, 3],
      [3, 1, 2],
      [2, 3, 1],
    ],
    b: [
      [1, 3, 2],
      [2, 1, 3],
      [3, 2, 1],
    ],
    product: [
      [6, 5, 5],
      [5, 6, 5],
      [5, 5, 6],
    ],
    why: "Tahap alternatif langsung bisa dipakai karena permutasi penyusun A saling komutatif.",
  },
  {
    id: "ordo4",
    label: "Ordo 4",
    tag: "Kasus non-sirkulan",
    summary:
      "Ordo 4 menarik karena ada contoh yang tidak sirkulan, tetapi tetap komutatif. Ini menegaskan bahwa hasil laporanmu tidak berhenti pada kasus yang terlalu sederhana.",
    a: [
      [1, 2, 3, 4],
      [2, 1, 4, 3],
      [3, 4, 1, 2],
      [4, 3, 2, 1],
    ],
    b: [
      [1, 2, 4, 3],
      [2, 1, 3, 4],
      [4, 3, 1, 2],
      [3, 4, 2, 1],
    ],
    product: [
      [7, 8, 6, 6],
      [8, 7, 6, 6],
      [6, 6, 7, 8],
      [6, 6, 8, 7],
    ],
    why: "Contoh ini lolos karena permutasi penyusunnya masih hidup dalam grup Klein yang abelian.",
  },
  {
    id: "ordo5",
    label: "Ordo 5",
    tag: "Kasus lebih kaya",
    summary:
      "Di ordo 5, algoritma umum lewat centralizer dan superlevel benar-benar terasa manfaatnya, karena struktur permutasinya sudah jauh lebih beragam.",
    a: [
      [5, 3, 2, 1, 4],
      [2, 1, 4, 5, 3],
      [1, 4, 3, 2, 5],
      [4, 5, 1, 3, 2],
      [3, 2, 5, 4, 1],
    ],
    b: [
      [5, 3, 1, 2, 4],
      [1, 2, 4, 5, 3],
      [2, 1, 3, 4, 5],
      [4, 5, 2, 3, 1],
      [3, 4, 5, 1, 2],
    ],
    product: [
      [10, 8, 9, 8, 9],
      [9, 10, 8, 8, 9],
      [8, 9, 10, 9, 8],
      [9, 8, 9, 10, 8],
      [8, 9, 8, 9, 10],
    ],
    why: "Di sini syarat perlu dari simbol maksimum membantu, tapi keputusan akhirnya tetap datang dari pemeriksaan superlevel.",
  },
] as const;

export default function CommutativeExamplesSlide() {
  const [activeCase, setActiveCase] = useState("ordo4");

  const currentCase = useMemo(
    () =>
      exampleCases.find((item) => item.id === activeCase) ?? exampleCases[0],
    [activeCase],
  );

  return (
    <div className="w-full min-h-dvh px-4 pb-24 pt-24 sm:px-6">
      <motion.div
        variants={container}
        initial="hidden"
        animate="visible"
        className="mx-auto flex w-full max-w-7xl flex-col gap-6"
      >
        <motion.div variants={item} className="space-y-2 text-center">
          <p className="text-xs font-bold uppercase tracking-widest text-amber-600">
            Contoh Hasil
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Pilih ordo, lalu lihat pasangan komutatif yang benar-benar muncul di
            laporan.
          </h2>
          <p className="mx-auto max-w-4xl text-left text-sm leading-relaxed text-stone-600">
            Bagian ini paling cocok buat pengunjung yang ingin bukti visual
            bahwa hasil teorinya memang menghasilkan contoh konkret.
          </p>
        </motion.div>

        <motion.div variants={item} className="flex flex-wrap gap-3">
          {exampleCases.map((item) => {
            const isActive = item.id === activeCase;
            return (
              <button
                key={item.id}
                type="button"
                onClick={() => setActiveCase(item.id)}
                className={[
                  "rounded-full border px-4 py-2 text-sm font-semibold transition-colors",
                  isActive
                    ? "border-rose-500 bg-rose-500 text-white"
                    : "border-stone-300 bg-white text-stone-700 hover:border-rose-400 hover:text-stone-950",
                ].join(" ")}
              >
                {item.label}
              </button>
            );
          })}
        </motion.div>

        <motion.div
          variants={item}
          className="rounded-[1.75rem] border border-stone-200 bg-white p-6 shadow-sm sm:p-8"
        >
          <div className="mb-6 flex flex-col gap-3 lg:flex-row lg:items-end lg:justify-between">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-rose-700">
                {currentCase.tag}
              </p>
              <h3
                className={`${headingClass} mt-2 text-3xl font-bold text-stone-950`}
              >
                {currentCase.label}
              </h3>
            </div>
            <p className="max-w-3xl text-sm leading-relaxed text-stone-600 sm:text-base">
              {currentCase.summary}
            </p>
          </div>

          <div className="grid gap-4 xl:grid-cols-3">
            <ThesisMatrix
              title="Matriks A"
              subtitle="Latin square awal"
              matrix={currentCase.a}
              accent="amber"
            />
            <ThesisMatrix
              title="Matriks B"
              subtitle="Pasangan komutatif yang diperoleh"
              matrix={currentCase.b}
              accent="emerald"
            />
            <ThesisMatrix
              title="A ⊗ B = B ⊗ A"
              subtitle="Hasil kali max-plus yang sama"
              matrix={currentCase.product}
              accent="rose"
            />
          </div>

          <div className="mt-6 rounded-3xl border border-sky-200 bg-sky-50 p-5">
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-sky-700">
              Apa yang bisa dipetik pengunjung
            </p>
            <p className="mt-3 text-sm leading-relaxed text-sky-950 sm:text-base">
              {currentCase.why}
            </p>
          </div>
        </motion.div>
      </motion.div>
    </div>
  );
}
