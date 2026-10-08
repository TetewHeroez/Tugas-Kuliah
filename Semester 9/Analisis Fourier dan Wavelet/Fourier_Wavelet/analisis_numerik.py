"""Hitung ulang tabel dan grafik laporan: python analisis_numerik.py.

Dependensi: numpy, scipy, matplotlib. Semua integral dihitung dengan
Simpson komposit; tidak menggunakan rumus transformasi Gaussian analitis.
"""

from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson

ROOT = Path(__file__).resolve().parent
FIGURES = ROOT / "Gambar"
RESULTS = ROOT / "hasil_numerik"
ORDERS = [5, 10, 20, 30, 40, 50, 60, 100]


def signal(t, epsilon=0.2):
    return np.exp(-t**2 / 2) * (
        np.cos(2 * t) + 0.5 * np.cos(5 * t) + epsilon * np.cos(50 * t)
    )


def fourier_series(intervals):
    t = np.linspace(-np.pi, np.pi, intervals + 1)
    values = signal(t)
    n = np.arange(101)
    phase = n[:, None] * t[None, :]
    # Manfaatkan simetri genap untuk koefisien kosinus.
    positive = t >= 0
    a = 2 * simpson(values[positive] * np.cos(phase[:, positive]),
                    x=t[positive], axis=1) / np.pi
    b = simpson(values * np.sin(phase), x=t, axis=1) / np.pi
    energy = float(simpson(values**2, x=t))
    partial = np.full_like(t, a[0] / 2)
    rows = []
    approximations = {}
    for k in range(1, 101):
        partial += a[k] * np.cos(k * t) + b[k] * np.sin(k * t)
        if k in ORDERS:
            error = float(np.sqrt(simpson((values - partial)**2, x=t)))
            spectral_energy = float(np.pi * (
                a[0]**2 / 2 + np.sum(a[1:k + 1]**2 + b[1:k + 1]**2)
            ))
            rows.append({"K": k, "error_L2": error,
                         "energy_series": spectral_energy,
                         "energy_gap": energy - spectral_energy,
                         "relative_gap": abs(energy - spectral_energy) / energy})
            approximations[k] = partial.copy()
    return t, values, a, b, energy, rows, approximations


def transform(omega, intervals=16384, limit=8.0, epsilon=0.2):
    # Sinyal real dan genap: integral sinus nol, integral kosinus dihitung
    # pada [0, limit] dan dikalikan dua. intervals merujuk [-limit, limit].
    t = np.linspace(0, limit, intervals // 2 + 1)
    values = np.exp(-t**2 / 2) if epsilon is None else signal(t, epsilon)
    result = np.empty(len(omega))
    for start in range(0, len(omega), 128):
        frequencies = omega[start:start + 128]
        result[start:start + len(frequencies)] = (
            2 / np.sqrt(2 * np.pi)
            * simpson(values * np.cos(frequencies[:, None] * t), x=t, axis=1)
        )
    return result


def plancherel(intervals, omega, limit=8.0):
    t = np.linspace(-limit, limit, intervals + 1)
    time_energy = float(simpson(signal(t)**2, x=t))
    spectrum = transform(omega, intervals, limit)
    frequency_energy = float(2 * simpson(abs(spectrum)**2, x=omega))
    return spectrum, {"N": intervals, "L": limit,
                      "delta_omega": float(omega[1] - omega[0]),
                      "energy_time": time_energy,
                      "energy_frequency": frequency_energy,
                      "absolute_gap": abs(time_energy - frequency_energy),
                      "relative_gap": abs(time_energy - frequency_energy) / time_energy}


def number(value, scientific=False):
    if scientific:
        mantissa, exponent = f"{value:.4e}".split("e")
        return rf"${mantissa}\times10^{{{int(exponent)}}}$"
    return f"{value:.10f}"


def write_table(name, rows):
    (RESULTS / name).write_text("\n".join(" & ".join(row) + r" \\" for row in rows)
                                + "\n\\hline\n", encoding="utf-8")


def save_figure(fig, name):
    fig.savefig(FIGURES / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(FIGURES / f"{name}.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def illustrate_simpson():
    """Ilustrasi pengenalan notasi, terpisah dari perhitungan sinyal tugas."""
    FIGURES.mkdir(exist_ok=True)
    nodes = np.linspace(0, 2, 5)
    node_values = nodes**2
    fig, (curve_ax, points_ax) = plt.subplots(
        2, 1, figsize=(8, 5), constrained_layout=True,
        gridspec_kw={"height_ratios": [3, 1.7]},
    )
    for start, color, label in [
        (0, "#377eb8", "Penerapan pertama: $t_0,t_1,t_2$"),
        (2, "#e1812c", "Penerapan kedua: $t_2,t_3,t_4$"),
    ]:
        panel_nodes = nodes[start:start + 3]
        panel_values = node_values[start:start + 3]
        panel_t = np.linspace(panel_nodes[0], panel_nodes[-1], 200)
        parabola = np.polyval(np.polyfit(panel_nodes, panel_values, 2), panel_t)
        curve_ax.fill_between(panel_t, 0, parabola, color=color, alpha=0.3, label=label)
    dense_t = np.linspace(0, 2, 400)
    curve_ax.plot(dense_t, dense_t**2, color="#173f6b", lw=1.7, label="$u(t)=t^2$")
    curve_ax.scatter(nodes, node_values, color="#173f6b", zorder=3)
    for j, (point_t, value) in enumerate(zip(nodes, node_values)):
        curve_ax.vlines(point_t, 0, value, color="gray", linestyle="--", alpha=0.65)
        curve_ax.annotate(
            f"$u(t_{j})={value:g}$", (point_t, value),
            xytext=(5 if j < 4 else -7, 9), textcoords="offset points",
            ha="left" if j < 4 else "right", fontsize=9,
        )
    curve_ax.set(xlim=(-0.12, 2.12), ylim=(-0.12, 4.75), ylabel="$u(t)$",
                 title="Contoh: $u(t)=t^2$, interval $[0,2]$, $N=4$, $h=0.5$")
    curve_ax.set_xticks(nodes)
    curve_ax.legend(loc="upper left", fontsize=9)
    curve_ax.grid(alpha=0.2)

    points_ax.plot([0, 2], [0.5, 0.5], color="black", lw=1)
    for j, point_t in enumerate(nodes):
        points_ax.plot([point_t, point_t], [0.44, 0.56], color="black")
        points_ax.text(point_t, 0.63, f"$t_{j}={point_t:g}$", ha="center", fontsize=10)
    for left, right in zip(nodes[:-1], nodes[1:]):
        points_ax.annotate("", xy=(right, 0.28), xytext=(left, 0.28),
                           arrowprops={"arrowstyle": "<->", "color": "gray"})
        points_ax.text((left + right) / 2, 0.08, "$h=0.5$", ha="center", fontsize=9)
    for left, right, color, label in [
        (0, 1, "#377eb8", "Simpson pertama\n$(t_0,t_1,t_2)$"),
        (1, 2, "#e1812c", "Simpson kedua\n$(t_2,t_3,t_4)$"),
    ]:
        points_ax.annotate("", xy=(right, -0.17), xytext=(left, -0.17),
                           arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.5})
        points_ax.text((left + right) / 2, -0.28, label, color=color,
                       ha="center", va="top", fontsize=10)
    points_ax.set(xlim=(-0.12, 2.12), ylim=(-0.7, 0.95),
                  title="Lima titik, empat subinterval, dua penerapan Simpson")
    points_ax.axis("off")
    save_figure(fig, "ilustrasi_simpson")


def main():
    FIGURES.mkdir(exist_ok=True)
    RESULTS.mkdir(exist_ok=True)
    illustrate_simpson()
    plt.rcParams.update({"font.size": 10, "axes.grid": True,
                         "grid.alpha": 0.25, "figure.constrained_layout.use": True})
    t, values, a, b, energy, rows, approximations = fourier_series(16384)
    _, _, a_coarse, _, energy_coarse, coarse_rows, _ = fourier_series(8192)
    omega = np.linspace(0, 60, 6001)
    spectrum, check = plancherel(16384, omega)
    _, coarse_check = plancherel(8192, omega[::2])
    # Uji perubahan batas waktu, terpisah dari penghalusan grid.
    _, shorter_check = plancherel(16384, omega, limit=6.0)
    # Periksa linearitas dan modulasi dengan transformasi Gaussian numerik.
    sample_omega = np.array([0.0, 2.0, 5.0, 50.0])
    modulation_values = np.zeros_like(sample_omega)
    for amplitude, center in [(1.0, 2), (0.5, 5), (0.2, 50)]:
        modulation_values += amplitude / 2 * (
            transform(sample_omega - center, epsilon=None)
            + transform(sample_omega + center, epsilon=None)
        )
    modulation_gap = float(np.max(abs(modulation_values - transform(sample_omega))))
    peaks = []
    for low, high in [(1, 3), (4, 6), (49, 51)]:
        indices = np.flatnonzero((omega >= low) & (omega <= high))
        idx = indices[np.argmax(abs(spectrum[indices]))]
        peaks.append({"omega": float(omega[idx]),
                      "magnitude": float(abs(spectrum[idx])),
                      "energy_density": float(abs(spectrum[idx])**2)})
    epsilon_rows = []
    for epsilon in [0.1, 0.2, 0.4]:
        value = float(abs(transform(np.array([50.0]), epsilon=epsilon)[0]))
        epsilon_rows.append({"epsilon": epsilon, "magnitude_at_50": value,
                             "energy_density_at_50": value**2})
    f3 = 0.2 * np.exp(-t**2 / 2) * np.cos(50 * t)
    idx = int(np.argmax(abs(f3)))
    high_frequency_time = float(t[idx])
    report = {
        "method": "Composite Simpson quadrature",
        "versions": {"numpy": np.__version__, "matplotlib": matplotlib.__version__},
        "series_intervals": 16384, "energy_interval": energy,
        "a": a.tolist(), "b": b.tolist(), "parseval": rows,
        "max_abs_b": float(np.max(abs(b[1:]))),
        "plancherel": check, "plancherel_coarse": coarse_check,
        "plancherel_L6": shorter_check, "positive_peaks": peaks,
        "modulation_check_max_gap": modulation_gap,
        "epsilon_effect": epsilon_rows,
        "high_frequency_time": high_frequency_time,
        "high_frequency_amplitude": float(abs(f3[idx])),
        "high_frequency_period": float(2 * np.pi / 50),
        "convergence": {"energy_interval_difference": abs(energy - energy_coarse),
                        "max_coefficient_difference": float(np.max(abs(a - a_coarse))),
                        "L2_at_60_difference": abs(rows[-2]["error_L2"]
                                                   - coarse_rows[-2]["error_L2"])}
    }
    (RESULTS / "ringkasan.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    np.savetxt(RESULTS / "koefisien.csv", np.column_stack([np.arange(101), a, b]),
               delimiter=",", header="n,a_n,b_n", comments="")
    np.savetxt(RESULTS / "spektrum.csv", np.column_stack([omega, spectrum, abs(spectrum)**2]),
               delimiter=",", header="omega,transform,energy_density", comments="")
    write_table("koefisien.tex", [[str(n), number(a[n])] for n in
                                 [0, 1, 2, 3, 4, 5, 6, 48, 49, 50, 51, 52, 60]])
    write_table("parseval.tex", [[str(row["K"]), number(row["error_L2"], True),
                                 number(row["energy_series"]), number(row["relative_gap"], True)]
                                for row in rows])
    write_table("galat.tex", [[str(row["K"]), number(row["error_L2"], True)] for row in rows])
    write_table("plancherel.tex", [[str(c["N"]), f'{c["delta_omega"]:.2f}',
                                   number(c["energy_time"]), number(c["energy_frequency"]),
                                   number(c["absolute_gap"], True)]
                                  for c in [coarse_check, check]])
    write_table("puncak.tex", [[f'{p["omega"]:.2f}', number(p["magnitude"]),
                               number(p["energy_density"])] for p in peaks])
    write_table("epsilon.tex", [[f'{r["epsilon"]:.1f}', number(r["magnitude_at_50"]),
                                number(r["energy_density_at_50"])] for r in epsilon_rows])
    macros = {"EnergiInterval": number(energy), "EnergiParseval": number(rows[-1]["energy_series"]),
              "GalatParseval": number(rows[-1]["energy_gap"], True),
              "EnergiWaktu": number(check["energy_time"]),
              "EnergiFrekuensi": number(check["energy_frequency"]),
              "GalatPlancherel": number(check["absolute_gap"], True),
              "GalatRelPlancherel": number(check["relative_gap"], True),
              "MaksSinus": number(report["max_abs_b"], True),
              "BedaKoefisien": number(report["convergence"]["max_coefficient_difference"], True),
              "BedaEnergiInterval": number(abs(energy - energy_coarse), True),
              "GalatModulasi": number(modulation_gap, True),
              "BedaBatasWaktu": number(abs(check["energy_time"] - shorter_check["energy_time"]), True),
              "BedaBatasSpektrum": number(abs(check["energy_frequency"] - shorter_check["energy_frequency"]), True)}
    (RESULTS / "nilai.tex").write_text("\n".join(
        rf"\newcommand{{\{name}}}{{{value}}}" for name, value in macros.items()) + "\n", encoding="utf-8")

    fig, axes = plt.subplots(2, 1, figsize=(8, 5.4))
    axes[0].plot(t, values, color="#1d4e89", lw=1.1, label="$f(t)$")
    axes[0].scatter([0], [signal(0)], color="#b12b32", zorder=3)
    axes[0].set(xlim=(-np.pi, np.pi), ylabel="$f(t)$", title="Sinyal pada interval pengamatan")
    axes[1].plot(t, f3, color="#b12b32", lw=1.3, label="$f_3(t)$")
    envelope = 0.2 * np.exp(-t**2 / 2)
    axes[1].plot(t, envelope, "--", color="gray", label="Selubung amplitudo")
    axes[1].plot(t, -envelope, "--", color="gray")
    axes[1].scatter([high_frequency_time], [f3[idx]], color="black", zorder=3,
                    label=f"Maksimum: t = {high_frequency_time:.0f}, |f3| = {abs(f3[idx]):.1f}")
    axes[1].set(xlim=(-0.5, 0.5), xlabel="$t$", ylabel="$f_3(t)$",
                title="Komponen frekuensi tertinggi, $\\omega_3 = 50$")
    axes[1].legend(loc="lower right", fontsize=8)
    save_figure(fig, "sinyal_numerik")

    fig, axes = plt.subplots(3, 1, figsize=(8, 7))
    for ax, k in zip(axes, [5, 10, 60]):
        ax.plot(t, values, color="#1d4e89", lw=1, label="$f(t)$")
        ax.plot(t, approximations[k], "--", color="#e1812c", lw=1.1, label=f"$S_{{{k}}}f(t)$")
        ax.set(xlim=(-np.pi, np.pi), ylabel="Amplitudo", title=f"Aproksimasi Fourier orde K = {k}")
        ax.legend(loc="upper right")
    axes[-1].set_xlabel("$t$")
    save_figure(fig, "aproksimasi_numerik")

    fig, axes = plt.subplots(1, 2, figsize=(8, 3.2))
    axes[0].stem(np.arange(61), a[:61], basefmt=" ")
    axes[0].set(xlabel="$n$", ylabel="$a_n$", title="Koefisien Fourier numerik")
    axes[1].semilogy([r["K"] for r in rows], [r["error_L2"] for r in rows], "o-", color="#1d4e89")
    axes[1].set(xlabel="$K$", ylabel="$\\|f-S_Kf\\|_2$", title="Galat aproksimasi")
    save_figure(fig, "koefisien_galat_numerik")

    signed_omega = np.concatenate([-omega[:0:-1], omega])
    signed_spectrum = np.concatenate([spectrum[:0:-1], spectrum])
    fig, axes = plt.subplots(2, 1, figsize=(8, 5.2))
    axes[0].plot(signed_omega, abs(signed_spectrum), color="#1d4e89")
    axes[0].set(ylabel="$|\\widehat f(\\omega)|$", title="Magnitudo transformasi Fourier numerik")
    axes[1].plot(signed_omega, abs(signed_spectrum)**2, color="#b12b32")
    axes[1].set(xlabel="$\\omega$", ylabel="$|\\widehat f(\\omega)|^2$", title="Kerapatan energi spektral numerik")
    for ax in axes:
        ax.set_xlim(-60, 60)
        ax.set_xticks([-50, -5, 0, 5, 50])
    save_figure(fig, "spektrum_numerik")

    fig, axes = plt.subplots(1, 2, figsize=(8, 3.2))
    epsilon_omega = np.linspace(45, 55, 1001)
    for epsilon in [0.1, 0.2, 0.4]:
        epsilon_spectrum = abs(transform(epsilon_omega, epsilon=epsilon))
        axes[0].plot(epsilon_omega, epsilon_spectrum, label=f"$\\varepsilon={epsilon}$")
        axes[1].plot(epsilon_omega, epsilon_spectrum**2, label=f"$\\varepsilon={epsilon}$")
    axes[0].set(xlabel="$\\omega$", ylabel="$|\\widehat f_\\varepsilon(\\omega)|$",
                title="Magnitudo dekat frekuensi 50")
    axes[1].set(xlabel="$\\omega$", ylabel="$|\\widehat f_\\varepsilon(\\omega)|^2$",
                title="Kerapatan energi dekat frekuensi 50")
    for ax in axes:
        ax.legend(fontsize=8)
    save_figure(fig, "epsilon_numerik")

    fig, axes = plt.subplots(1, 2, figsize=(8, 3.2))
    axes[0].plot(np.arange(101), np.pi * (a[0]**2 / 2 + np.concatenate(
        [[0], np.cumsum(a[1:]**2 + b[1:]**2)])), color="#1d4e89", label="$E_K$")
    axes[0].axhline(energy, color="#b12b32", ls="--", label="Energi domain waktu")
    axes[0].set(xlabel="$K$", ylabel="Energi", title="Pemeriksaan Parseval")
    axes[0].legend(fontsize=8)
    # Plancherel: tampilkan energi spektral kumulatif agar distribusi energi terlihat.
    from scipy.integrate import cumulative_simpson
    cumulative = 2 * cumulative_simpson(abs(spectrum)**2, x=omega, initial=0)
    axes[1].plot(omega, cumulative, color="#1d4e89", label="$\\int_{-W}^{W}|\\widehat f|^2\\,d\\omega$")
    axes[1].axhline(check["energy_time"], color="#b12b32", ls="--", label="Energi domain waktu")
    axes[1].set(xlabel="$W$", ylabel="Energi", title="Pemeriksaan Plancherel")
    axes[1].legend(fontsize=8)
    save_figure(fig, "energi_numerik")

    print(json.dumps({k: v for k, v in report.items() if k not in ["a", "b"]}, indent=2))


if __name__ == "__main__":
    main()
