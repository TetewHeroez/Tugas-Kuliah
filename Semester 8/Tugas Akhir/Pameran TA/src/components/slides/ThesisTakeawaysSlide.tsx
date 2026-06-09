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

const panels = [
  {
    id: "tujuan",
    label: "Tujuan",
    title:
      "Arah besarnya adalah menyiapkan fondasi aljabar untuk skema mirip Diffie-Hellman Key Exchange.",
    items: [
      "Pada pertukaran kunci, dua pihak butuh operasi yang bisa dijalankan dari sisi masing-masing tetapi tetap bertemu pada hasil bersama.",
      "Di sini elemen yang ingin dioperasikan bukan bilangan biasa, melainkan Latin square dengan operasi perkalian max-plus.",
      "Karena itu, persoalan utamanya bukan sekadar membuat Latin square, tetapi mencari pasangan yang komutatif agar mekanisme pertukaran kuncinya masuk akal.",
    ],
  },
  {
    id: "kontribusi",
    label: "Kontribusi",
    title:
      "Kontribusi TA ini adalah memberi cara sistematis untuk membangun dan memeriksa pasangan Latin square komutatif.",
    items: [
      "Dekomposisi ke matriks permutasi max-plus membuat struktur Latin square lebih mudah dibaca dan dimanipulasi.",
      "Syarat perlu, syarat cukup, dan uji superlevel memperkecil ruang pencarian kandidat komutatif.",
      "Prosedur konstruksi memberi jalur praktis dari A menuju kandidat B, jadi pencarian tidak lagi murni brute force.",
    ],
  },
  {
    id: "manfaat",
    label: "Manfaat",
    title:
      "Kalau diteruskan, hasil ini bisa jadi batu pijakan untuk desain protokol berbasis struktur max-plus.",
    items: [
      "Ia memberi bahasa dan alat awal untuk merancang operasi pertukaran kunci dengan objek Latin square, bukan hanya matriks numerik biasa.",
      "Ia menunjukkan kapan komutativitas bisa diharapkan, yang penting kalau dua pihak ingin sampai ke shared key yang sama.",
      "Penelitian lanjut bisa masuk ke implementasi algoritmik, efisiensi komputasi, dan perumusan skema Diffie-Hellman yang benar-benar operasional.",
    ],
  },
] as const;

export default function ThesisTakeawaysSlide() {
  const [activePanel, setActivePanel] = useState("kontribusi");

  const currentPanel = useMemo(
    () => panels.find((panel) => panel.id === activePanel) ?? panels[0],
    [activePanel],
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
            Penutup
          </p>
          <h2
            className={`${headingClass} text-3xl font-bold text-stone-900 sm:text-4xl`}
          >
            Kontribusi Masa Depan?
          </h2>
          <p className="mx-auto max-w-4xl text-left text-sm leading-relaxed text-stone-600">
            Jadi penutupnya bukan cuma rangkuman. Di sini pengunjung diajak
            lihat bahwa komutativitas yang kamu bangun itu relevan kalau nanti
            Latin square dipakai sebagai elemen dalam skema mirip Diffie-Hellman
            Key Exchange.
          </p>
        </motion.div>

        <motion.div variants={item} className="flex flex-wrap gap-3">
          {panels.map((panel) => {
            const isActive = panel.id === activePanel;
            return (
              <button
                key={panel.id}
                type="button"
                onClick={() => setActivePanel(panel.id)}
                className={[
                  "rounded-full border px-4 py-2 text-sm font-semibold transition-colors",
                  isActive
                    ? "border-stone-900 bg-stone-900 text-white"
                    : "border-stone-300 bg-white text-stone-700 hover:border-stone-500 hover:text-stone-950",
                ].join(" ")}
              >
                {panel.label}
              </button>
            );
          })}
        </motion.div>

        <motion.div
          variants={item}
          key={currentPanel.id}
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
          className="grid gap-6 lg:grid-cols-[0.46fr_0.54fr]"
        >
          <div className="rounded-[1.75rem] border border-stone-200 bg-white p-6 shadow-sm sm:p-8">
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-stone-500">
              Fokus aktif
            </p>
            <h3
              className={`${headingClass} mt-4 text-3xl font-bold text-stone-950`}
            >
              {currentPanel.title}
            </h3>
          </div>

          <div className="grid gap-4">
            {currentPanel.items.map((item) => (
              <div
                key={item}
                className="rounded-3xl border border-stone-200 bg-white p-5 shadow-sm"
              >
                <p className="text-sm leading-relaxed text-stone-700 sm:text-base">
                  {item}
                </p>
              </div>
            ))}
          </div>
        </motion.div>
      </motion.div>
    </div>
  );
}
