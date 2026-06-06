import type { Metadata } from "next";
import { Plus_Jakarta_Sans, Libre_Baskerville } from "next/font/google";
import "katex/dist/katex.min.css";
import "./globals.css";

const plusJakarta = Plus_Jakarta_Sans({
  subsets: ["latin"],
  display: "swap",
  weight: ["400", "500", "600", "700"],
});

const libreBaskerville = Libre_Baskerville({
  subsets: ["latin"],
  variable: "--font-heading",
  display: "swap",
  weight: ["400", "700"],
});

export const metadata: Metadata = {
  title: "Latin Square Komutatif atas Aljabar Max-Plus - Pameran Tugas Akhir",
  description:
    "Eksplorasi interaktif tentang Sudoku, Latin Square, dan Aljabar Max-Plus untuk pameran tugas akhir matematika.",
  keywords: [
    "Latin Square",
    "Max-Plus Algebra",
    "Aljabar Max-Plus",
    "Sudoku",
    "Tugas Akhir",
    "Matematika",
    "Simulasi Interaktif",
  ],
  openGraph: {
    title: "Latin Square Komutatif atas Aljabar Max-Plus",
    description:
      "Eksplorasi interaktif tentang Sudoku, Latin Square, dan Aljabar Max-Plus.",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="id">
      <body
        className={`${plusJakarta.className} ${libreBaskerville.variable} min-h-dvh overflow-x-hidden bg-stone-50 text-stone-900`}
      >
        {children}
      </body>
    </html>
  );
}
