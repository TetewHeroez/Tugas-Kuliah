"use client";

import { motion, AnimatePresence } from "framer-motion";

interface SlideControllerProps {
  currentSlide: number;
  totalSlides: number;
  unlockedSlides: number;
  onNavigate: (slideIndex: number) => void;
  slideLabels: string[];
}

export default function SlideController({
  currentSlide,
  totalSlides,
  unlockedSlides,
  onNavigate,
  slideLabels,
}: SlideControllerProps) {
  return (
    <>
      <motion.nav
        initial={{ y: -60, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
        className="fixed left-0 right-0 top-0 z-50 flex items-center justify-center border-b border-stone-200 bg-stone-50/85 px-6 py-4 backdrop-blur-lg"
      >
        <div className="flex items-center gap-2">
          {Array.from({ length: totalSlides }).map((_, i) => {
            const isActive = i === currentSlide;
            const isCompleted = i < unlockedSlides && i < currentSlide;
            const isLocked = i > unlockedSlides;
            const isUnlocked = i <= unlockedSlides;

            return (
              <div key={i} className="flex items-center gap-2">
                <button
                  onClick={() => isUnlocked && onNavigate(i)}
                  disabled={isLocked}
                  title={isLocked ? "Selesaikan slide sebelumnya" : slideLabels[i]}
                  className={[
                    "group relative h-3 w-3 rounded-full border-2 transition-all duration-300",
                    isActive
                      ? "scale-125 border-amber-400 bg-amber-400 shadow-lg shadow-amber-400/40"
                      : isCompleted
                        ? "border-emerald-500 bg-emerald-500"
                        : isLocked
                          ? "cursor-not-allowed border-stone-300 opacity-40"
                          : "cursor-pointer border-stone-300 hover:border-amber-400",
                  ].join(" ")}
                >
                  <span className="pointer-events-none absolute -bottom-8 left-1/2 -translate-x-1/2 whitespace-nowrap rounded-md bg-stone-50 px-2 py-1 text-xs font-medium text-stone-600 opacity-0 shadow-md transition-opacity group-hover:opacity-100">
                    {slideLabels[i]}
                  </span>
                </button>

                {i < totalSlides - 1 && (
                  <div
                    className={`h-0.5 w-8 transition-colors duration-300 ${
                      i < currentSlide ? "bg-emerald-500" : "bg-stone-200"
                    }`}
                  />
                )}
              </div>
            );
          })}
        </div>
      </motion.nav>

      <AnimatePresence mode="wait">
        <motion.div
          key={currentSlide}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -10 }}
          transition={{ duration: 0.3 }}
          className="fixed bottom-6 left-1/2 z-50 flex -translate-x-1/2 gap-3"
        >
          {currentSlide > 0 && (
            <button
              onClick={() => onNavigate(currentSlide - 1)}
              className="flex items-center gap-2 rounded-full border border-stone-300 bg-white px-5 py-2.5 text-sm font-semibold tracking-wide text-stone-700 shadow-sm transition-all duration-200 hover:-translate-y-0.5 hover:border-amber-400 hover:shadow-md active:scale-95"
            >
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
                <path d="M10 12L6 8L10 4" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
              Kembali
            </button>
          )}

          {currentSlide < totalSlides - 1 && currentSlide < unlockedSlides && (
            <button
              onClick={() => onNavigate(currentSlide + 1)}
              className="flex items-center gap-2 rounded-full bg-emerald-500 px-5 py-2.5 text-sm font-semibold tracking-wide text-white shadow-md transition-all duration-200 hover:-translate-y-0.5 hover:bg-emerald-600 hover:shadow-lg hover:shadow-emerald-500/20 active:scale-95"
            >
              Lanjut
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
                <path d="M6 12L10 8L6 4" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
            </button>
          )}
        </motion.div>
      </AnimatePresence>
    </>
  );
}
