"""
Effort Profile Chart — Microsoft AI Platform Advisor

Renders a 2x2 quadrant chart plotting a project's technical complexity
against its risk score, with each quadrant labeled with planning guidance.

Usage in Copilot Studio's code interpreter:
    1. Replace the three input variables below with the values the agent
       collected during the discovery interview.
    2. Run the script. The chart is saved as effort_profile.png and
       displayed inline in the chat.

Inputs the agent must substitute:
    PROJECT_NAME       — string, from discovery Q1
    COMPLEXITY_SCORE   — integer 0–10, from Phase 3 sum
    RISK_SCORE         — integer 0–10, from Phase 4 sum
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ---- Inputs (agent substitutes these three lines) ----
PROJECT_NAME = "{{PROJECT_NAME}}"
COMPLEXITY_SCORE = {{COMPLEXITY_SCORE}}
RISK_SCORE = {{RISK_SCORE}}
# -------------------------------------------------------

fig, ax = plt.subplots(figsize=(11, 8))

# Quadrant background fills (soft colors)
ax.add_patch(Rectangle((0, 5), 5, 5, facecolor="#fdecea", alpha=0.5, zorder=0))   # top-left: low complexity, high risk
ax.add_patch(Rectangle((5, 5), 5, 5, facecolor="#f3e5f5", alpha=0.5, zorder=0))   # top-right: high complexity, high risk
ax.add_patch(Rectangle((0, 0), 5, 5, facecolor="#e8f5e9", alpha=0.5, zorder=0))   # bottom-left: low complexity, low risk
ax.add_patch(Rectangle((5, 0), 5, 5, facecolor="#e3f2fd", alpha=0.5, zorder=0))   # bottom-right: high complexity, low risk

# Quadrant labels (title + guidance underneath)
label_style = dict(ha="center", va="center", fontsize=10, wrap=True)

ax.text(2.5, 8.2, "GOVERN HARD, SHIP FAST",
        fontweight="bold", color="#c92a2a", fontsize=11, ha="center")
ax.text(2.5, 7.2, "Agent 365 blueprint + DLP\nfrom day one",
        color="#c92a2a", **label_style)

ax.text(7.5, 8.2, "PoC → PHASED ROLLOUT",
        fontweight="bold", color="#862e9c", fontsize=11, ha="center")
ax.text(7.5, 7.2, "Exec sponsor, dedicated ALM,\nevaluations before every release",
        color="#862e9c", **label_style)

ax.text(2.5, 3.2, "MOVE FAST, ITERATE",
        fontweight="bold", color="#2b8a3e", fontsize=11, ha="center")
ax.text(2.5, 2.2, "Pilot with one team,\nexpand quickly",
        color="#2b8a3e", **label_style)

ax.text(7.5, 3.2, "INVEST IN ENGINEERING",
        fontweight="bold", color="#1864ab", fontsize=11, ha="center")
ax.text(7.5, 2.2, "Foundry + evaluations,\nclear ALM environments",
        color="#1864ab", **label_style)

# Quadrant dividers (dashed)
ax.axhline(y=5, color="#a0a0a0", linestyle="--", linewidth=1, zorder=1)
ax.axvline(x=5, color="#a0a0a0", linestyle="--", linewidth=1, zorder=1)

# Plot the project point
ax.scatter([COMPLEXITY_SCORE], [RISK_SCORE],
           s=400, c="#ff922b", edgecolors="#1e1e1e", linewidths=2, zorder=5)
ax.annotate(f"  {PROJECT_NAME}\n  ({COMPLEXITY_SCORE}/10, {RISK_SCORE}/10)",
            xy=(COMPLEXITY_SCORE, RISK_SCORE),
            xytext=(10, 10), textcoords="offset points",
            fontsize=11, fontweight="bold", zorder=6,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                      edgecolor="#1e1e1e", linewidth=1))

# Axes formatting
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks(range(0, 11))
ax.set_yticks(range(0, 11))
ax.set_xlabel("Technical complexity  →", fontsize=13, fontweight="bold")
ax.set_ylabel("Risk  →", fontsize=13, fontweight="bold")
ax.set_title(f"{PROJECT_NAME} — Effort Profile",
             fontsize=16, fontweight="bold", pad=15)
ax.grid(True, alpha=0.2)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig("effort_profile.png", dpi=150, bbox_inches="tight")
plt.show()

print(f"Chart saved as effort_profile.png")
print(f"Complexity: {COMPLEXITY_SCORE}/10 | Risk: {RISK_SCORE}/10")
