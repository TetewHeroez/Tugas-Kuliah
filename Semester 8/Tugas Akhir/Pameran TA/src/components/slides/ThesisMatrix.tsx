"use client";

interface ThesisMatrixProps {
  title: string;
  subtitle?: string;
  matrix: readonly (readonly number[])[];
  accent?: "stone" | "amber" | "sky" | "emerald" | "rose";
}

const accentMap = {
  stone: {
    frame: "border-stone-200 bg-white",
    title: "text-stone-800",
    cell: "border-stone-200/90",
  },
  amber: {
    frame: "border-amber-200 bg-amber-50/70",
    title: "text-amber-800",
    cell: "border-amber-100/80",
  },
  sky: {
    frame: "border-sky-200 bg-sky-50/70",
    title: "text-sky-800",
    cell: "border-sky-100/80",
  },
  emerald: {
    frame: "border-emerald-200 bg-emerald-50/70",
    title: "text-emerald-800",
    cell: "border-emerald-100/80",
  },
  rose: {
    frame: "border-rose-200 bg-rose-50/70",
    title: "text-rose-800",
    cell: "border-rose-100/80",
  },
} as const;

export default function ThesisMatrix({
  title,
  subtitle,
  matrix,
  accent = "stone",
}: ThesisMatrixProps) {
  const palette = accentMap[accent];

  return (
    <section className={`rounded-2xl border p-4 shadow-sm ${palette.frame}`}>
      <div className="mb-3">
        <h3 className={`text-sm font-bold uppercase tracking-[0.2em] ${palette.title}`}>
          {title}
        </h3>
        {subtitle ? (
          <p className="mt-1 text-sm leading-relaxed text-stone-600">
            {subtitle}
          </p>
        ) : null}
      </div>

      <div
        className="grid overflow-hidden rounded-xl border border-stone-300 bg-stone-50"
        style={{
          gridTemplateColumns: `repeat(${matrix[0]?.length ?? 1}, minmax(0, 1fr))`,
        }}
      >
        {matrix.flatMap((row, rowIndex) =>
          row.map((value, columnIndex) => (
            <div
              key={`${title}-${rowIndex}-${columnIndex}`}
              className={`flex aspect-square items-center justify-center border text-base font-semibold text-stone-900 sm:text-lg ${palette.cell}`}
            >
              {value}
            </div>
          )),
        )}
      </div>
    </section>
  );
}
