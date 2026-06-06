"use client";

import katex from "katex";
import { useMemo } from "react";

interface MathBlockProps {
  /** LaTeX expression */
  tex: string;
  /** Display mode (block) vs inline */
  display?: boolean;
  className?: string;
}

export default function MathBlock({
  tex,
  display = false,
  className = "",
}: MathBlockProps) {
  const html = useMemo(() => {
    try {
      return katex.renderToString(tex, {
        displayMode: display,
        throwOnError: false,
        trust: true,
      });
    } catch {
      return tex;
    }
  }, [tex, display]);

  if (display) {
    return (
      <div
        className={`katex-display ${className}`}
        dangerouslySetInnerHTML={{ __html: html }}
      />
    );
  }

  return (
    <span
      className={className}
      dangerouslySetInnerHTML={{ __html: html }}
    />
  );
}
