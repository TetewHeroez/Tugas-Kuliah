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

type MatrixValue = number | ".";
type Matrix = readonly (readonly MatrixValue[])[];

const constructionSteps = [
  {
    id: "start",
    short: "1",
    title: "Mulai dari matriks kandidat B*",
    focus: "Kerangka awal",
    note: "Pencarian tidak menebak seluruh B sekaligus. Kita mulai dari matriks kandidat parsial B* yang masih kosong, lalu diisi simbol demi simbol.",
    matrix: [
      [".", ".", ".", "."],
      [".", ".", ".", "."],
      [".", ".", ".", "."],
      [".", ".", ".", "."],
    ] as const satisfies Matrix,
  },
  {
    id: "sigma4",
    short: "2",
    title: "Pilih posisi simbol maksimum",
    focus: "Tentukan sigma_4^B",
    note: "Langkah pertama adalah memilih posisi simbol 4. Pilihan ini dibatasi oleh centralizer dari simbol maksimum pada A, jadi cabangnya belum liar sejak awal.",
    matrix: [
      [".", ".", ".", 4],
      [".", ".", 4, "."],
      [".", 4, ".", "."],
      [4, ".", ".", "."],
    ] as const satisfies Matrix,
    formula: "\\sigma_4^B",
  },
  {
    id: "sigma3",
    short: "3",
    title: "Tambahkan simbol berikutnya dan cek level",
    focus: "Isi simbol 3",
    note: "Setelah simbol 4 dipilih, simbol 3 dimasukkan ke posisi yang masih mungkin. Di titik ini pemeriksaan superlevel mulai bisa menolak cabang yang salah sebelum B* lengkap.",
    matrix: [
      [".", ".", 3, 4],
      [".", 3, 4, "."],
      [3, 4, ".", "."],
      [4, ".", ".", 3],
    ] as const satisfies Matrix,
    formula: "\\mathcal{U}_{\\ge 7}^{AB} = \\mathcal{U}_{\\ge 7}^{BA}",
  },
  {
    id: "sigma2",
    short: "4",
    title: "Lengkapi B* sedikit demi sedikit",
    focus: "Isi simbol 2",
    note: "Kalau level sebelumnya lolos, simbol 2 bisa ditambahkan. Sekarang bentuk B* sudah makin terlihat, tetapi masih ada satu simbol yang belum ditentukan.",
    matrix: [
      [".", 2, 3, 4],
      [2, 3, 4, "."],
      [3, 4, ".", 2],
      [4, ".", 2, 3],
    ] as const satisfies Matrix,
    formula: "\\mathcal{U}_{\\ge 6}^{AB} = \\mathcal{U}_{\\ge 6}^{BA}",
  },
  {
    id: "finish",
    short: "5",
    title: "Dari B* menjadi B",
    focus: "Isi simbol 1",
    note: "Kalau semua level lolos, sel yang tersisa otomatis diisi simbol 1. Pada titik itu kandidat parsial B* berubah menjadi Latin square penuh B.",
    matrix: [
      [1, 2, 3, 4],
      [2, 3, 4, 1],
      [3, 4, 1, 2],
      [4, 1, 2, 3],
    ] as const satisfies Matrix,
    formula: "B",
  },
] as const;

function MatrixPreview({ matrix }: { matrix: Matrix }) {
  const columns = matrix[0]?.length ?? 1;

  return (
    <div
      className="grid overflow-hidden rounded-xl border border-stone-300 bg-white"
      style={{ gridTemplateColumns: `repeat(${columns}, minmax(0, 1fr))` }}
    >
      {matrix.flatMap((row, rowIndex) =>
        row.map((value, colIndex) => {
          const isEmpty = value === ".";
          return (
            <div
              key={`${rowIndex}-${colIndex}`}
              className={[
                "flex h-11 w-11 items-center justify-center border border-stone-200 text-sm font-semibold sm:h-12 sm:w-12 sm:text-base",
                isEmpty
                  ? "bg-stone-50 text-stone-300"
                  : "bg-emerald-50 text-stone-900",
              ].join(" ")}
            >
              {value}
            </div>
          );
        }),
      )}
    </div>
  );
}

export default function CommutativeSearchAlgorithmSlide() {
  return (
    <div className="w-full min-h-dvh px-4 pb-24 pt-24 sm:px-6">
      <motion.div
        variants={container}
        initial="hidden"
        animate="visible"
        className="mx-auto flex w-full max-w-4xl flex-col gap-6"
      >
        <motion.div variants={item} className="space-y-2 text-center">
          <p className="text-xs font-bold uppercase tracking-widest text-amber-600">
            Prosedur Konstruksi
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Pencarian dimulai dari B* lalu dilengkapi sampai menjadi B.
          </h2>
          <p className="mx-auto max-w-4xl text-left text-sm leading-relaxed text-stone-600">
            Jadi algoritma ini bukan menebak seluruh Latin square sekaligus.
            Ia membangun kandidat parsial <span className="font-semibold text-stone-800">B*</span>,
            memeriksa level-level penting di tengah jalan, lalu hanya
            melanjutkan cabang yang masih konsisten.
          </p>
        </motion.div>

        <motion.div variants={item} className="space-y-3">
          {constructionSteps.map((step, index) => (
            <details
              key={step.id}
              open={index === 0}
              className="group rounded-lg border border-stone-200 bg-white shadow-sm open:border-emerald-400"
            >
              <summary className="flex cursor-pointer list-none items-start justify-between gap-4 px-5 py-4">
                <div className="flex items-start gap-4 text-left">
                  <span className="mt-0.5 flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-amber-500 text-sm font-bold text-white">
                    {step.short}
                  </span>
                  <div className="space-y-2">
                    <p className="text-xs font-bold uppercase tracking-[0.24em] text-emerald-700">
                      {step.focus}
                    </p>
                    <div>
                      <p className="text-lg font-bold text-stone-950">
                        {step.title}
                      </p>
                      <p className="mt-1 text-sm leading-relaxed text-stone-600">
                        {step.note}
                      </p>
                    </div>
                  </div>
                </div>
                <span className="mt-1 shrink-0 text-xl font-semibold text-stone-400 transition-transform duration-200 group-open:rotate-45 group-open:text-emerald-700">
                  +
                </span>
              </summary>

              <div className="border-t border-stone-200 px-5 py-5">
                <div className="grid gap-5 md:grid-cols-[minmax(0,0.85fr)_minmax(0,1.15fr)] md:items-start">
                  <div className="flex justify-center">
                    <MatrixPreview matrix={step.matrix} />
                  </div>

                  <div className="space-y-4">
                    {step.formula ? (
                      <div className="rounded-2xl border border-stone-200 bg-stone-50 px-4 py-5">
                        <MathBlock
                          tex={step.formula}
                          display
                          className="text-stone-950"
                        />
                      </div>
                    ) : null}

                    <div className="rounded-2xl border border-sky-200 bg-sky-50 px-5 py-4">
                      <p className="text-xs font-bold uppercase tracking-[0.24em] text-sky-700">
                        Cara membacanya
                      </p>
                      <p className="mt-3 text-sm leading-relaxed text-sky-950">
                        {step.id === "start"
                          ? "Di tahap ini belum ada komitmen terhadap permutasi penyusun B. Bentuk kosong ini hanya menandai bahwa pencarian masih berada di titik awal."
                          : step.id === "sigma4"
                            ? "Begitu simbol maksimum dipilih, kita langsung tahu sebagian bentuk B*. Kalau pilihan ini salah, cabang pencarian bisa dihentikan lebih awal."
                            : step.id === "sigma3"
                              ? "Sekarang B* mulai punya struktur. Pemeriksaan level tinggi bekerja sebagai filter supaya kita tidak melanjutkan kandidat yang sudah jelas gagal."
                              : step.id === "sigma2"
                                ? "Pada tahap ini B* sudah hampir menjadi Latin square penuh. Tinggal satu simbol tersisa, tetapi konsistensi level tetap harus dijaga."
                                : "Begitu semua syarat lolos, kekosongan yang tersisa diisi otomatis. Kandidat parsial B* pun resmi menjadi Latin square B."}
                      </p>
                    </div>
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
