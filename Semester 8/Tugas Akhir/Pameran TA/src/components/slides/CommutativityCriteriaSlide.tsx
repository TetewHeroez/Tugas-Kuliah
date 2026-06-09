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

const criteriaPanels = [
  {
    id: "necessary",
    label: "Syarat perlu",
    eyebrow: "Penyaring awal",
    title: "Cek dulu simbol maksimum.",
    explainer:
      "Kalau A dan B komutatif, permutasi yang membawa simbol maksimum n wajib saling komutatif. Ini membuat pencarian kandidat awal jauh lebih sempit.",
    formula: "\\sigma_n^A \\circ \\sigma_n^B = \\sigma_n^B \\circ \\sigma_n^A",
    takeaway:
      "Artinya kandidat untuk simbol maksimum pada B harus hidup di centralizer dari simbol maksimum pada A.",
  },
  {
    id: "sufficient",
    label: "Syarat cukup",
    eyebrow: "Jaminan komutatif",
    title: "Kalau semua permutasi masuk subgrup abelian yang sama, selesai.",
    explainer:
      "Begitu semua permutasi penyusun A dan B saling kompatibel di satu subgrup abelian, setiap suku pada A \\otimes B punya pasangan yang sama di B \\otimes A.",
    formula: "\\sigma_i^A, \\sigma_j^B \\in H \\le S_n,\\; H \\text{ abelian}",
    takeaway:
      "Ini menjelaskan mengapa banyak Latin square sirkulan otomatis komutatif.",
  },
  {
    id: "iff",
    label: "Perlu-cukup",
    eyebrow: "Uji final",
    title: "Bandingkan himpunan superlevel dari level tertinggi ke bawah.",
    explainer:
      "Komutativitas benar-benar terjadi jika dan hanya jika posisi-posisi yang mencapai ambang level v sama pada A \\otimes B dan B \\otimes A untuk semua level yang relevan.",
    formula:
      "\\mathcal{U}_{\\ge v}^{AB} = \\mathcal{U}_{\\ge v}^{BA},\\; v \\in \\{n+2,\\ldots,2n\\}",
    takeaway:
      "Ini yang kemudian dipakai sebagai mesin pemeriksaan pada algoritma pencarian pasangan.",
  },
] as const;

export default function CommutativityCriteriaSlide() {
  return (
    <div className="h-dvh w-full overflow-hidden px-4 pb-24 pt-24 sm:px-6">
      <motion.div
        variants={container}
        initial="hidden"
        animate="visible"
        className="mx-auto flex h-full w-full max-w-3xl flex-col gap-6 overflow-y-auto pr-1 [scrollbar-width:none] [-ms-overflow-style:none] [&::-webkit-scrollbar]:hidden"
      >
        <motion.div variants={item} className="space-y-2 text-center">
          <p className="text-xs font-bold uppercase tracking-widest text-amber-600">
            Syarat Kekomutatifan
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Teorema Kekomutatifan
          </h2>
          <p className="mx-auto max-w-4xl text-left text-sm leading-relaxed text-stone-600">
            Dengan memperhatikan struktur permutasi pembangun entri pada A dan
            B, kita bisa merumuskan tiga kriteria yang harus dipenuhi.
          </p>
        </motion.div>

        <motion.div variants={item} className="space-y-3">
          {criteriaPanels.map((panel) => (
            <details
              key={panel.id}
              // open={index === 0}
              className="group rounded-lg border border-stone-200 bg-white shadow-sm open:border-emerald-400"
            >
              <summary className="flex cursor-pointer list-none items-start justify-between gap-4 px-5 py-4">
                <div className="space-y-2 text-left">
                  <p className="text-xs font-bold uppercase tracking-[0.24em] text-emerald-700">
                    {panel.eyebrow}
                  </p>
                  <div>
                    <p className="text-lg font-bold text-stone-950">
                      {panel.label}
                    </p>
                    <p className="mt-1 text-sm leading-relaxed text-stone-600">
                      {panel.title}
                    </p>
                  </div>
                </div>
                <span className="mt-1 shrink-0 text-xl font-semibold text-stone-400 transition-transform duration-200 group-open:rotate-45 group-open:text-emerald-700">
                  +
                </span>
              </summary>

              <div className="border-t border-stone-200 px-5 py-5">
                <div className="space-y-5">
                  <p className="text-sm leading-relaxed text-stone-600">
                    {panel.explainer}
                  </p>

                  <div className="overflow-x-auto rounded-2xl border border-stone-200 bg-stone-50 px-4 py-5 [scrollbar-width:none] [-ms-overflow-style:none] [&::-webkit-scrollbar]:hidden">
                    <MathBlock
                      tex={panel.formula}
                      display
                      className="text-stone-950"
                    />
                  </div>

                  <div className="rounded-2xl border border-sky-200 bg-sky-50 px-5 py-4">
                    <p className="text-xs font-bold uppercase tracking-[0.24em] text-sky-700">
                      Cara membacanya
                    </p>
                    <p className="mt-3 text-sm leading-relaxed text-sky-950">
                      {panel.takeaway}
                    </p>
                  </div>
                </div>
              </div>
            </details>
          ))}
        </motion.div>
      </motion.div>
    </div>
  );
}
