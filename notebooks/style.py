"""Shared plotting style for the Silesia geohazards course notebooks.

Usage in any notebook:
    from style import apply_style, COLORS, save_figure
    apply_style()
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Course colour palette (kept small and colour-blind friendly).
COLORS = {
    "rock":    "#4A4A4A",
    "soil":    "#A0522D",
    "water":   "#1F77B4",
    "fail":    "#D62728",
    "safe":    "#2CA02C",
    "accent":  "#FF7F0E",
    "neutral": "#7F7F7F",
    "grid":    "#CCCCCC",
}


def apply_style():
    """Apply a consistent matplotlib style across all course notebooks."""
    rcParams.update({
        "figure.figsize":     (7.0, 5.0),
        "figure.dpi":         110,
        "savefig.dpi":        200,
        "savefig.bbox":       "tight",
        "savefig.transparent": False,   # white background; safe on dark slides
        "savefig.facecolor":  "white",
        "figure.facecolor":   "white",
        "axes.facecolor":     "white",
        "font.family":        "serif",
        "font.size":          13,
        "axes.titlesize":     15,
        "axes.labelsize":     14,
        "axes.spines.top":    False,
        "axes.spines.right":  False,
        "axes.grid":          True,
        "grid.color":         COLORS["grid"],
        "grid.linewidth":     0.6,
        "grid.alpha":         0.7,
        "lines.linewidth":    2.0,
        "mathtext.fontset":   "cm",
        "legend.frameon":     False,
        "legend.fontsize":    12,
    })


def save_figure(fig, name, formats=("svg", "png"), folder="figures"):
    """Save a figure for both web (PNG) and PowerPoint (SVG).

    SVG is vector and scales perfectly when pasted into PowerPoint.
    Filenames will be ``<folder>/<name>.<fmt>``.
    """
    out = Path(folder)
    out.mkdir(exist_ok=True)
    for fmt in formats:
        fig.savefig(out / f"{name}.{fmt}")
    return out / f"{name}.svg"
