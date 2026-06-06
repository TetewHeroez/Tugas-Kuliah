"use client";

import { useMemo, useState } from "react";
import { motion } from "framer-motion";

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

const algorithmSteps = [
  {
    id: "decompose",
    short: "1",
    title: "Dekomposisi A",
    detail:
      "Ambil posisi tiap simbol di A, lalu ubah menjadi permutasi penyusun. Di titik ini persoalan matriks diubah menjadi persoalan susunan permutasi.",
  },
  {
    id: "alternative",
    short: "2",
    title: "Cek jalur cepat",
    detail:
      "Kalau semua permutasi penyusun A saling komutatif, ada jalur alternatif: susun ulang permutasi A untuk membentuk kandidat B yang otomatis komutatif.",
  },
  {
    id: "centralizer",
    short: "3",
    title: "Mulai dari simbol maksimum",
    detail:
      "Jika jalur cepat gagal, pencarian dimulai dari permutasi simbol maksimum pada B. Kandidatnya dibatasi oleh centralizer dari simbol maksimum pada A.",
  },
  {
    id: "superlevel",
    short: "4",
    title: "Turun per level",
    detail:
      "Setelah simbol n dipilih, algoritma mengisi simbol n-1, n-2, dan seterusnya sambil memeriksa kesamaan himpunan superlevel dari level tertinggi ke bawah.",
  },
  {
    id: "finish",
    short: "5",
    title: "Lengkapi dan verifikasi",
    detail:
      "Jika semua level lolos, sisa posisi diisi simbol 1. Hasil akhirnya adalah kandidat B yang memenuhi A ⊗ B = B ⊗ A.",
  },
] as const;

const algorithmWins = [
  "Cabang yang gagal bisa dipotong lebih awal.",
  "Tidak perlu menebak seluruh B dari awal.",
  "Contoh ordo 3, 4, dan 5 menunjukkan prosedurnya benar-benar bekerja.",
];

export default function CommutativeSearchAlgorithmSlide() {
  const [activeStep, setActiveStep] = useState("decompose");

  const currentStep = useMemo(
    () =>
      algorithmSteps.find((step) => step.id === activeStep) ??
      algorithmSteps[0],
    [activeStep],
  );

  return (
    <div className="w-full min-h-dvh px-4 pb-24 pt-24 sm:px-6">
      <motion.div
        variants={container}
        initial="hidden"
        animate="visible"
        className="mx-auto flex w-full max-w-6xl flex-col gap-6"
      >
        <motion.div variants={item} className="space-y-2 text-center">
          <p className="text-xs font-bold uppercase tracking-widest text-amber-600">
            Prosedur Konstruksi
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Dari satu Latin square A, algoritma ini mencari pasangan B yang
            komutatif.
          </h2>
          <p className="mx-auto max-w-4xl text-left text-sm leading-relaxed text-stone-600">
            Ini bagian yang paling enak dibikin interaktif karena pengunjung
            bisa mengikuti logika pencariannya seperti sedang melihat decision
            path.
          </p>
        </motion.div>

        <motion.div
          variants={item}
          className="grid gap-6 lg:grid-cols-[0.52fr_0.48fr]"
        >
          <div className="space-y-4">
            {algorithmSteps.map((step) => {
              const isActive = step.id === activeStep;
              return (
                <button
                  key={step.id}
                  type="button"
                  onClick={() => setActiveStep(step.id)}
                  className={[
                    "flex w-full items-start gap-4 rounded-3xl border px-5 py-4 text-left transition-colors",
                    isActive
                      ? "border-amber-500 bg-amber-50"
                      : "border-stone-200 bg-white hover:border-amber-300",
                  ].join(" ")}
                >
                  <span
                    className={[
                      "mt-0.5 flex h-9 w-9 shrink-0 items-center justify-center rounded-full text-sm font-bold",
                      isActive
                        ? "bg-amber-500 text-white"
                        : "bg-stone-100 text-stone-700",
                    ].join(" ")}
                  >
                    {step.short}
                  </span>
                  <div>
                    <p className="text-lg font-bold text-stone-950">
                      {step.title}
                    </p>
                    <p className="mt-2 text-sm leading-relaxed text-stone-600">
                      {step.detail}
                    </p>
                  </div>
                </button>
              );
            })}
          </div>

          <motion.div
            key={currentStep.id}
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
            className="flex h-full flex-col justify-between rounded-[1.75rem] border border-stone-200 bg-white p-6 shadow-sm sm:p-8"
          >
            <div className="space-y-4">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-amber-700">
                Step aktif
              </p>
              <h3
                className={`${headingClass} text-3xl font-bold text-stone-950`}
              >
                {currentStep.title}
              </h3>
              <p className="text-base leading-relaxed text-stone-600">
                {currentStep.detail}
              </p>
            </div>

            <div className="mt-8 rounded-3xl border border-emerald-200 bg-emerald-50 p-5">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-emerald-700">
                Kenapa algoritma ini penting
              </p>
              <div className="mt-4 space-y-3">
                {algorithmWins.map((item) => (
                  <div
                    key={item}
                    className="rounded-2xl bg-white/80 px-4 py-3 text-sm leading-relaxed text-emerald-950"
                  >
                    {item}
                  </div>
                ))}
              </div>
            </div>
          </motion.div>
        </motion.div>
      </motion.div>
    </div>
  );
}
