"use client";

import { useState, useCallback, useEffect } from "react";
import { AnimatePresence, motion } from "framer-motion";
import LatinSquareDecompositionSlide from "@/components/slides/LatinSquareDecompositionSlide";
import LatinSquareProductReductionSlide from "@/components/slides/LatinSquareProductReductionSlide";
import SlideController from "@/components/SlideController";
import CommutativeSearchAlgorithmSlide from "@/components/slides/CommutativeSearchAlgorithmSlide";
import CommutativityCriteriaSlide from "@/components/slides/CommutativityCriteriaSlide";
import CommutativeExamplesSlide from "@/components/slides/CommutativeExamplesSlide";
import ThesisTakeawaysSlide from "@/components/slides/ThesisTakeawaysSlide";
import LatinSquareConceptSlide from "@/components/slides/LatinSquareConceptSlide";
import SudokuPuzzleSlide from "@/components/slides/SudokuPuzzleSlide";
import MatrixMultiplicationSlide from "@/components/slides/MatrixMultiplicationSlide";

const SLIDE_LABELS = [
  "Sudoku",
  "Latin Square",
  "Perkalian",
  "Dekomposisi",
  "Reduksi",
  "Kriteria",
  "Algoritma",
  "Contoh",
  "Manfaat",
];
const OPENING_STORAGE_KEY = "pameran-ta-opening-last-seen";
const CURRENT_SLIDE_STORAGE_KEY = "pameran-ta-current-slide";
const OPENING_EXPIRY_MS = 1000 * 60 * 60 * 24;

const headingClass = "font-[family:var(--font-heading)]";

const slideVariants = {
  enter: { opacity: 0, x: 60 },
  center: { opacity: 1, x: 0 },
  exit: { opacity: 0, x: -60 },
};

const identityRows = [
  "Latin Square Komutatif atas Aljabar Max-Plus",
  "Teosofi Hidayah Agung",
  "5002221132",
  "Muhammad Syifa'ul Mufid, S.Si., M.Si., D.Phil.",
];

function OpeningScreen({ onEnter }: { onEnter: () => void }) {
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setIsLoaded(true);
    }, 1600);

    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    if (!isLoaded) return;

    const onKeyDown = () => onEnter();
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [isLoaded, onEnter]);

  return (
    <motion.section
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      onClick={() => {
        if (isLoaded) onEnter();
      }}
      className="relative flex min-h-dvh items-center justify-center overflow-hidden bg-[radial-gradient(circle_at_top,rgba(251,191,36,0.18),transparent_32%),radial-gradient(circle_at_bottom,rgba(56,189,248,0.12),transparent_28%),linear-gradient(180deg,#fafaf9_0%,#f5f5f4_100%)] px-4 py-10"
    >
      <div className="absolute inset-0 opacity-45">
        <motion.div
          animate={{ y: [0, -18, 0], opacity: [0.25, 0.5, 0.25] }}
          transition={{ repeat: Infinity, duration: 5.2, ease: "easeInOut" }}
          className="absolute left-[12%] top-[18%] h-28 w-28 rounded-full border border-amber-300/60"
        />
        <motion.div
          animate={{ y: [0, 20, 0], opacity: [0.2, 0.45, 0.2] }}
          transition={{
            repeat: Infinity,
            duration: 6,
            ease: "easeInOut",
            delay: 0.4,
          }}
          className="absolute bottom-[14%] right-[10%] h-36 w-36 rounded-full border border-sky-200/70"
        />
      </div>

      <AnimatePresence mode="wait">
        {!isLoaded ? (
          <motion.div
            key="loading"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0, scale: 0.96 }}
            className="relative z-10 flex w-full max-w-md flex-col items-center gap-5"
          >
            <div className="space-y-2 text-center">
              <p className="text-xs font-bold uppercase tracking-[0.34em] text-amber-700">
                Memuat Presentasi
              </p>
              <p className="text-sm text-stone-500">
                Menyiapkan pameran tugas akhir
              </p>
            </div>
            <div className="h-1.5 w-full overflow-hidden rounded-full bg-stone-200">
              <motion.div
                animate={{ x: ["-100%", "220%"] }}
                transition={{
                  repeat: Infinity,
                  duration: 1.35,
                  ease: "easeInOut",
                }}
                className="h-full w-1/3 rounded-full bg-linear-to-r from-amber-400 via-amber-500 to-sky-400"
              />
            </div>
          </motion.div>
        ) : (
          <motion.div
            key="opening-card"
            initial={{ opacity: 0, scale: 0.88, y: 24 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.96 }}
            transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
            className="relative z-10 w-full max-w-4xl"
          >
            <div className="overflow-hidden rounded-4xl border border-stone-200/80 bg-white/82 px-6 py-10 shadow-[0_30px_90px_rgba(41,37,36,0.10)] backdrop-blur md:px-12 md:py-14">
              <div className="mx-auto flex max-w-3xl flex-col items-center text-center">
                <motion.div
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.15, duration: 0.7 }}
                  className="mb-6 inline-flex items-center gap-3 text-xs font-bold uppercase tracking-[0.34em] text-amber-700"
                >
                  <span className="h-px w-12 bg-amber-500" />
                  Tugas Akhir
                  <span className="h-px w-12 bg-amber-500" />
                </motion.div>

                <motion.h1
                  initial={{ opacity: 0, y: 18 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{
                    delay: 0.25,
                    duration: 0.95,
                    ease: [0.16, 1, 0.3, 1],
                  }}
                  className={`${headingClass} max-w-3xl text-4xl font-bold leading-tight text-stone-950 sm:text-5xl lg:text-6xl`}
                >
                  {identityRows[0]}
                </motion.h1>

                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.45, duration: 0.9 }}
                  className="mt-8 space-y-3"
                >
                  <p
                    className={`${headingClass} text-2xl italic text-stone-800 sm:text-3xl`}
                  >
                    {identityRows[1]}
                  </p>
                  <p className="text-sm uppercase tracking-[0.26em] text-stone-500 sm:text-base">
                    {identityRows[2]}
                  </p>
                  <p className="text-base text-stone-600 sm:text-lg">
                    Pembimbing:{" "}
                    <span className="font-semibold text-stone-800">
                      {identityRows[3]}
                    </span>
                  </p>
                </motion.div>

                <motion.p
                  animate={{ opacity: [0.3, 1, 0.3] }}
                  transition={{
                    repeat: Infinity,
                    duration: 1.35,
                    ease: "easeInOut",
                  }}
                  className="mt-10 text-xs font-semibold uppercase tracking-[0.3em] text-stone-500 sm:text-sm"
                >
                  Tekan apa saja untuk melanjutkan
                </motion.p>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.section>
  );
}

export default function Home() {
  const [showOpening, setShowOpening] = useState<boolean | null>(null);
  const [currentSlide, setCurrentSlide] = useState(0);
  useEffect(() => {
    const lastSeenRaw = localStorage.getItem(OPENING_STORAGE_KEY);
    const lastSeen = lastSeenRaw ? Number(lastSeenRaw) : 0;
    const savedSlideRaw = localStorage.getItem(CURRENT_SLIDE_STORAGE_KEY);
    const savedSlide = savedSlideRaw ? Number(savedSlideRaw) : 0;
    const shouldShowOpening =
      !lastSeen ||
      Number.isNaN(lastSeen) ||
      Date.now() - lastSeen > OPENING_EXPIRY_MS;
    const syncTimer = window.setTimeout(() => {
      setShowOpening(shouldShowOpening);

      if (
        !Number.isNaN(savedSlide) &&
        savedSlide >= 0 &&
        savedSlide < SLIDE_LABELS.length
      ) {
        setCurrentSlide(savedSlide);
      }
    }, 0);

    return () => window.clearTimeout(syncTimer);
  }, []);

  const [unlockedSlides, setUnlockedSlides] = useState(SLIDE_LABELS.length - 1);

  const handleSudokuSolved = useCallback(() => {
    setUnlockedSlides((prev) => Math.max(prev, SLIDE_LABELS.length - 1));
  }, []);

  const handleNavigate = useCallback((slideIndex: number) => {
    setCurrentSlide(slideIndex);
  }, []);

  useEffect(() => {
    window.localStorage.setItem(
      CURRENT_SLIDE_STORAGE_KEY,
      String(currentSlide),
    );
  }, [currentSlide]);

  const handleEnterPresentation = useCallback(() => {
    window.localStorage.setItem(OPENING_STORAGE_KEY, String(Date.now()));
    setShowOpening(false);
  }, []);

  const renderSlide = () => {
    switch (currentSlide) {
      case 0:
        return <SudokuPuzzleSlide onSolved={handleSudokuSolved} />;
      case 1:
        return <LatinSquareConceptSlide />;
      case 2:
        return <MatrixMultiplicationSlide />;
      case 3:
        return <LatinSquareDecompositionSlide />;
      case 4:
        return <LatinSquareProductReductionSlide />;
      case 5:
        return <CommutativityCriteriaSlide />;
      case 6:
        return <CommutativeSearchAlgorithmSlide />;
      case 7:
        return <CommutativeExamplesSlide />;
      case 8:
        return <ThesisTakeawaysSlide />;
      default:
        return null;
    }
  };

  return (
    <main className="relative h-dvh overflow-y-auto bg-stone-50 [scrollbar-width:none] [-ms-overflow-style:none] [&::-webkit-scrollbar]:hidden">
      {showOpening === null ? null : showOpening ? (
        <AnimatePresence mode="wait">
          <OpeningScreen key="opening" onEnter={handleEnterPresentation} />
        </AnimatePresence>
      ) : (
        <>
          <SlideController
            currentSlide={currentSlide}
            totalSlides={SLIDE_LABELS.length}
            unlockedSlides={unlockedSlides}
            onNavigate={handleNavigate}
            slideLabels={SLIDE_LABELS}
          />
          <AnimatePresence mode="wait">
            <motion.div
              key={`slide-${currentSlide}`}
              variants={slideVariants}
              initial="enter"
              animate="center"
              exit="exit"
              transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
            >
              {renderSlide()}
            </motion.div>
          </AnimatePresence>
        </>
      )}
    </main>
  );
}
