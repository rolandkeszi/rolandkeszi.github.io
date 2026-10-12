"""Figures for the LLM benchmark and US airline case studies (results as reported in the notebooks and study).

Run: python assets/make_figures_nlp.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent / "img"
INK, MUTED, GRID, ACCENT, SOFT = "#1d1d1f", "#6e6e73", "#e5e5ea", "#2a78d6", "#b9c6d6"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "text.color": INK,
    "axes.edgecolor": GRID, "axes.labelcolor": MUTED, "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.spines.top": False, "axes.spines.right": False, "axes.titlesize": 11,
    "axes.titleweight": "bold", "axes.titlelocation": "left", "savefig.dpi": 170,
    "savefig.bbox": "tight", "savefig.facecolor": "white",
})

# 1. Twelve-model accuracy on IMDb sentiment
groups = [
    ("Zero-shot LLMs", [("GPT-5.3 Instant", 96.9), ("Claude Haiku 4.5", 96.2), ("Claude Sonnet 4.6", 96.1),
                        ("GPT-4.1 mini", 95.8), ("Gemini 2.5 Flash-Lite", 94.5), ("Gemini 2.5 Flash*", 93.4)]),
    ("Fine-tuned transformer", [("BERT-base", 90.5)]),
    ("Neural networks + GloVe", [("LSTM", 86.8), ("CNN", 85.0), ("Simple NN", 74.6)]),
    ("Lexicon baselines", [("VADER", 69.9), ("TextBlob", 69.0)]),
]
labels, values, colors, ypos, heads = [], [], [], [], []
y = 0
for gi, (g, items) in enumerate(groups):
    heads.append((y - 0.15, g))
    y += 0.9
    for name, v in items:
        labels.append(name); values.append(v); ypos.append(y)
        colors.append(ACCENT if gi == 0 else SOFT)
        y += 1
    y += 0.5
fig, ax = plt.subplots(figsize=(8, 6.4))
ax.barh(ypos, values, color=colors, height=0.7)
for yy, v in zip(ypos, values):
    ax.text(v + 0.6, yy, f"{v:.1f}%", va="center", fontsize=9)
for yy, g in heads:
    ax.text(0, yy + 0.5, g.upper(), fontsize=8.5, color=MUTED, weight="bold", va="center")
ax.set_yticks(ypos, labels)
ax.invert_yaxis()
ax.set_xlim(0, 105)
ax.set_xlabel("Accuracy on IMDb movie reviews (%)")
ax.tick_params(axis="y", length=0)
ax.spines["left"].set_visible(False)
ax.xaxis.grid(True, color=GRID)
ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig(OUT / "llm_benchmark.png")

# 2. VADER on airline tweets: confusion matrix (counts reported in the study)
cm = np.array([[4563, 1905, 2710], [431, 1325, 1343], [89, 215, 2059]])
labs = ["negative", "neutral", "positive"]
share = cm / cm.sum(axis=1, keepdims=True)
fig, ax = plt.subplots(figsize=(5.2, 4.2))
ax.imshow(share, cmap="Blues", vmin=0, vmax=1)
for i in range(3):
    for j in range(3):
        ax.text(j, i, f"{cm[i, j]:,}\n{share[i, j]:.0%}", ha="center", va="center", fontsize=9,
                color="white" if share[i, j] > 0.55 else INK)
ax.set_xticks(range(3), labs)
ax.set_yticks(range(3), labs)
ax.set_xlabel("Predicted by VADER")
ax.set_ylabel("Human label")
for s in ax.spines.values():
    s.set_visible(False)
ax.set_title("VADER on 14,640 airline tweets (accuracy 54%)")
fig.tight_layout()
fig.savefig(OUT / "usair_vader_confusion.png")

# 3. Predicted vs actual class sizes
actual = [9178, 3099, 2363]
pred = [5083, 3445, 6112]
x = np.arange(3)
fig, ax = plt.subplots(figsize=(6, 3.2))
ax.bar(x - 0.18, actual, width=0.34, color=SOFT, label="Human label")
ax.bar(x + 0.18, pred, width=0.34, color=ACCENT, label="VADER prediction")
ax.set_xticks(x, labs)
ax.set_ylabel("Tweets")
ax.yaxis.grid(True, color=GRID)
ax.set_axisbelow(True)
ax.legend(frameon=False)
ax.set_title("VADER sees far more positive tweets than there are")
fig.tight_layout()
fig.savefig(OUT / "usair_vader_distribution.png")
print("done")
