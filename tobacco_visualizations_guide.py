# ============================================================
# TOBACCO TAX VISUALIZATION CODE — Muhammad Salman Pasha
# Complete self-contained script to reproduce all 7 figures
# Requirements: pip install matplotlib numpy
# Run: python tobacco_visualizations_guide.py
# ============================================================

import matplotlib
matplotlib.use('Agg')           # Remove this line if running in Jupyter
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ============================================================
# SECTION 1 — SETUP & DATA
# All data confirmed from official government sources
# ============================================================

# --- Global Style ---
plt.rcParams.update({
    'font.family':        'DejaVu Serif',   # Change to 'Times New Roman' on Windows
    'axes.spines.top':    False,
    'axes.spines.right':  False,
    'axes.grid':          True,
    'grid.color':         '#e0e0e0',
    'grid.linestyle':     '--',
    'grid.linewidth':     0.6,
    'figure.dpi':         180,
    'savefig.dpi':        180,
    'savefig.bbox':       'tight',
    'savefig.facecolor':  'white',
})

# --- Colors ---
VA_BLUE  = '#185FA5'    # Virginia — blue
VA_LIGHT = '#A8C8E8'    # Virginia — light blue (OTP bars)
MD_GREEN = '#0F6E56'    # Maryland — green
MD_LIGHT = '#7DC4AD'    # Maryland — light green (OTP bars)
RED      = '#C00000'    # Policy events, declines
GRAY     = '#888888'    # Neutral

# --- Years ---
YEARS = ['FY2021', 'FY2022', 'FY2023', 'FY2024', 'FY2025']
X     = np.arange(len(YEARS))   # [0, 1, 2, 3, 4]

# --- Virginia Annual Data (Source: VA Dept of Taxation FY2025, Table 5.2) ---
va_cig   = [234.2, 219.8, 188.7, 169.9, 155.8]   # Cigarette Tax ($M)
va_otp   = [ 52.4,  58.8,  57.4,  55.1,  55.0]   # OTP Tax ($M)
va_total = [v + o for v, o in zip(va_cig, va_otp)]

# --- Maryland Annual Data (Source: MD ATCC Annual Reports FY2021-FY2025) ---
md_cig   = [322.2, 417.9, 390.5, 343.6, 390.4]   # Cigarette Stamps Net ($M)
md_otp   = [ 47.3,  55.6,  58.3,  61.4,  65.4]   # OTP Net ($M)
md_total = [v + o for v, o in zip(md_cig, md_otp)]

# --- Tax Rates ---
va_rate = [0.60, 0.60, 0.60, 0.60, 0.60]    # Virginia: stable $0.60/pack
md_rate = [3.75, 3.75, 3.75, 5.00, 5.00]    # Maryland: $3.75 then $5.00 Jul 2024

# --- Year-over-Year % Changes ---
va_yoy  = [None, -6.1, -14.2, -10.0,  -8.3]
md_yoy  = [None, 29.7,  -6.6, -12.0,  14.0]

# --- Maryland Monthly Cigarette Data ($M) ---
# Source: MD ATCC Annual Report FY2025, Tobacco Revenue page
MONTHS = ['July','August','September','October','November','December',
          'January','February','March','April','May','June']

md_monthly = {
    'July':      [ 1.19, 30.49, 35.27, 36.23, 39.91],
    'August':    [25.29, 37.87, 35.35, 27.78, 33.20],
    'September': [25.12, 36.26, 33.03, 32.98, 30.15],
    'October':   [31.36, 42.33, 37.84, 32.74, 37.57],
    'November':  [19.95, 37.75, 34.59, 27.90, 30.78],
    'December':  [30.47, 32.36, 27.89, 27.77, 26.99],
    'January':   [23.20, 34.25, 30.57, 23.18, 28.02],
    'February':  [19.83, 29.79, 28.01, 29.65, 34.52],
    'March':     [24.79, 34.24, 29.23, 22.20, 24.58],
    'April':     [25.80, 35.38, 29.49, 28.68, 30.96],
    'May':       [41.36, 31.24, 28.01, 33.22, 34.06],
    'June':      [53.81, 35.92, 41.10, 21.31, 39.71],
}

# --- Standard source note used on all figures ---
SOURCE_NOTE = ('Note. Sources: Virginia Department of Taxation Annual Report FY2025, Table 5.2; '
               'Maryland Alcohol, Tobacco, and Cannabis Commission Annual Reports FY2021–FY2025.')

# --- Helper: format y-axis as $XXM ---
def fmt_dollar(x, pos): return f'${x:.0f}M'

# --- Helper: add vertical policy event line ---
def add_policy_line(ax, x_pos, label, color=RED, y_pct=0.97):
    ax.axvline(x=x_pos, color=color, linestyle=':', linewidth=1.4, alpha=0.75)
    ax.text(x_pos + 0.06, y_pct, label,
            transform=ax.get_xaxis_transform(),
            fontsize=7.5, color=color, va='top', rotation=90, alpha=0.9)


# ============================================================
# FIGURE 1 — Cigarette Revenue Line Chart: VA vs MD
# ============================================================

fig, ax = plt.subplots(figsize=(9, 5))

# Plot lines
ax.plot(X, va_cig, color=VA_BLUE,  marker='o', linewidth=2.5, markersize=8, label='Virginia Cigarette Tax')
ax.plot(X, md_cig, color=MD_GREEN, marker='s', linewidth=2.5, markersize=8, label='Maryland Cigarette Stamps')

# Data labels
for i, (v, m) in enumerate(zip(va_cig, md_cig)):
    ax.annotate(f'${v:.1f}M', (i, v), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=8.5, color=VA_BLUE, fontweight='bold')
    ax.annotate(f'${m:.1f}M', (i, m), textcoords='offset points',
                xytext=(0, -18), ha='center', fontsize=8.5, color=MD_GREEN, fontweight='bold')

# Policy event markers
add_policy_line(ax, 1.0, 'MD $2.00→$3.75\n(Mar 2021)', MD_GREEN, 0.62)
add_policy_line(ax, 3.0, 'MD $3.75→$5.00\n(Jul 2024)', RED, 0.62)

# Formatting
ax.set_xticks(X)
ax.set_xticklabels(YEARS, fontsize=10)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmt_dollar))
ax.set_ylabel('Net Revenue (USD Millions)', fontsize=10)
ax.set_ylim(100, 480)
ax.set_title('Figure 1. Cigarette Tax Revenue: Virginia vs. Maryland (FY2021–FY2025)',
             fontsize=12, fontweight='bold', pad=14)
ax.legend(fontsize=9, loc='upper right')
fig.text(0.01, -0.03, SOURCE_NOTE, fontsize=7.5, color='#555555', style='italic')

plt.tight_layout()
plt.savefig('fig1_cigarette_revenue_comparison.png')
plt.show()  # Remove if running in script mode without display
plt.close()
print("Figure 1 saved.")


# ============================================================
# FIGURE 2 — OTP Revenue Line Chart: VA vs MD
# ============================================================

fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(X, va_otp, color=VA_BLUE,  marker='o', linewidth=2.5, markersize=8,
        linestyle='--', label='Virginia OTP Tax')
ax.plot(X, md_otp, color=MD_GREEN, marker='s', linewidth=2.5, markersize=8,
        linestyle='--', label='Maryland OTP Revenue')

# Shaded fill under each line
ax.fill_between(X, va_otp, alpha=0.10, color=VA_BLUE)
ax.fill_between(X, md_otp, alpha=0.10, color=MD_GREEN)

# Data labels
for i, (v, m) in enumerate(zip(va_otp, md_otp)):
    ax.annotate(f'${v:.1f}M', (i, v), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=8.5, color=VA_BLUE, fontweight='bold')
    ax.annotate(f'${m:.1f}M', (i, m), textcoords='offset points',
                xytext=(0, -18), ha='center', fontsize=8.5, color=MD_GREEN, fontweight='bold')

# Cumulative change annotations
ax.annotate('+38.3% (FY2021→FY2025)', xy=(4, 65.4), xytext=(3.1, 71),
            fontsize=9, color=MD_GREEN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=MD_GREEN))
ax.annotate('+4.9% (FY2021→FY2025)', xy=(4, 55.0), xytext=(3.1, 46),
            fontsize=9, color=VA_BLUE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=VA_BLUE))

ax.set_xticks(X)
ax.set_xticklabels(YEARS, fontsize=10)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmt_dollar))
ax.set_ylabel('Net Revenue (USD Millions)', fontsize=10)
ax.set_ylim(35, 82)
ax.set_title('Figure 2. Other Tobacco Products (OTP) Revenue: Virginia vs. Maryland (FY2021–FY2025)',
             fontsize=12, fontweight='bold', pad=14)
ax.legend(fontsize=9, loc='lower right')
fig.text(0.01, -0.03, SOURCE_NOTE, fontsize=7.5, color='#555555', style='italic')

plt.tight_layout()
plt.savefig('fig2_otp_revenue_comparison.png')
plt.show()
plt.close()
print("Figure 2 saved.")


# ============================================================
# FIGURE 3 — Grouped Bar Chart: Cigarette vs OTP per State
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
bar_w = 0.35

for ax, cig, otp, c1, c2, title in [
    (axes[0], va_cig, va_otp, VA_BLUE, VA_LIGHT, 'Virginia'),
    (axes[1], md_cig, md_otp, MD_GREEN, MD_LIGHT, 'Maryland'),
]:
    b1 = ax.bar(X - bar_w/2, cig, bar_w, color=c1, label='Cigarette Revenue', zorder=3)
    b2 = ax.bar(X + bar_w/2, otp, bar_w, color=c2, label='OTP Revenue',       zorder=3)

    # Value labels on bars
    for bar in b1:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f'${bar.get_height():.0f}M', ha='center', va='bottom', fontsize=7, color=c1)
    for bar in b2:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f'${bar.get_height():.0f}M', ha='center', va='bottom', fontsize=7, color=c2)

    ax.set_xticks(X)
    ax.set_xticklabels(YEARS, fontsize=9, rotation=15)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmt_dollar))
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.legend(fontsize=8)
    ax.set_ylabel('Revenue (USD Millions)', fontsize=9)

# Add policy markers to Maryland panel
add_policy_line(axes[1], 1.0, 'MD $3.75', MD_GREEN, 0.78)
add_policy_line(axes[1], 3.0, 'MD $5.00', RED,      0.78)

fig.suptitle('Figure 3. Cigarette vs. OTP Revenue by State (FY2021–FY2025)',
             fontsize=12, fontweight='bold', y=1.02)
fig.text(0.01, -0.05, SOURCE_NOTE, fontsize=7.5, color='#555555', style='italic')

plt.tight_layout()
plt.savefig('fig3_grouped_bar_cigarette_otp.png')
plt.show()
plt.close()
print("Figure 3 saved.")


# ============================================================
# FIGURE 4 — Tax Rate Differential: VA vs MD
# ============================================================

fig, ax = plt.subplots(figsize=(9, 5))

# Shaded gap between the two rates
ax.fill_between(X, va_rate, md_rate, alpha=0.15, color=RED, label='Tax Gap (MD−VA)')

# Rate lines
ax.plot(X, md_rate, color=MD_GREEN, marker='s', linewidth=2.5, markersize=9, label='Maryland Rate ($/pack)')
ax.plot(X, va_rate, color=VA_BLUE,  marker='o', linewidth=2.5, markersize=9, label='Virginia Rate ($/pack)')

# Gap annotations (midpoint of each year's gap)
gap_labels = ['$3.15 gap', '$3.15 gap', '$3.15 gap', '$4.40 gap', '$4.40 gap']
for i, (v, m, g) in enumerate(zip(va_rate, md_rate, gap_labels)):
    ax.annotate(g, xy=(i, (v + m) / 2), ha='center', fontsize=8.5,
                color=RED, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.25', facecolor='white',
                          edgecolor='#dddddd', alpha=0.9))

# Rate value labels
for i, (v, m) in enumerate(zip(va_rate, md_rate)):
    ax.annotate(f'${m:.2f}', (i, m), textcoords='offset points',
                xytext=(0, 9), ha='center', fontsize=8.5, color=MD_GREEN, fontweight='bold')
    ax.annotate(f'${v:.2f}', (i, v), textcoords='offset points',
                xytext=(0, -16), ha='center', fontsize=8.5, color=VA_BLUE, fontweight='bold')

ax.set_xticks(X)
ax.set_xticklabels(YEARS, fontsize=10)
ax.set_ylabel('Tax Rate ($ per pack of 20)', fontsize=10)
ax.set_ylim(-0.5, 6.5)
ax.set_title('Figure 4. Virginia vs. Maryland Cigarette Tax Rate Differential (FY2021–FY2025)',
             fontsize=12, fontweight='bold', pad=14)
ax.legend(fontsize=9)
fig.text(0.01, -0.04,
         'Note. MD rate: $2.00 (through Mar 13, 2021) → $3.75 (Mar 14, 2021) → $5.00 (Jul 1, 2024). '
         'VA rate stable at $0.60 throughout study period.',
         fontsize=7.5, color='#555555', style='italic')

plt.tight_layout()
plt.savefig('fig4_tax_rate_differential.png')
plt.show()
plt.close()
print("Figure 4 saved.")


# ============================================================
# FIGURE 5 — Year-over-Year % Change Bar Chart
# ============================================================

fig, ax = plt.subplots(figsize=(9, 5))

X2     = np.arange(1, len(YEARS))      # [1, 2, 3, 4]
labels = YEARS[1:]                     # ['FY2022', 'FY2023', 'FY2024', 'FY2025']
va_y   = [-6.1, -14.2, -10.0, -8.3]
md_y   = [29.7,  -6.6, -12.0, 14.0]
bar_w  = 0.35

b1 = ax.bar(X2 - bar_w/2, va_y, bar_w, color=VA_BLUE,  label='Virginia YoY %', zorder=3)
b2 = ax.bar(X2 + bar_w/2, md_y, bar_w, color=MD_GREEN, label='Maryland YoY %', zorder=3)

# Value labels
for bar, val in zip(b1, va_y):
    offset = -1.8 if val < 0 else 0.4
    ax.text(bar.get_x() + bar.get_width()/2, val + offset,
            f'{val:.1f}%', ha='center', fontsize=8.5, color=VA_BLUE, fontweight='bold')
for bar, val in zip(b2, md_y):
    offset = -1.8 if val < 0 else 0.4
    ax.text(bar.get_x() + bar.get_width()/2, val + offset,
            f'{val:.1f}%', ha='center', fontsize=8.5, color=MD_GREEN, fontweight='bold')

ax.axhline(y=0, color='black', linewidth=0.8)
ax.set_xticks(X2)
ax.set_xticklabels(labels, fontsize=10)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}%'))
ax.set_ylabel('Year-over-Year Change (%)', fontsize=10)
ax.set_title('Figure 5. Year-over-Year Cigarette Revenue Change: Virginia vs. Maryland',
             fontsize=12, fontweight='bold', pad=14)
ax.legend(fontsize=9)
fig.text(0.01, -0.03, SOURCE_NOTE, fontsize=7.5, color='#555555', style='italic')

plt.tight_layout()
plt.savefig('fig5_yoy_change.png')
plt.show()
plt.close()
print("Figure 5 saved.")


# ============================================================
# FIGURE 6 — Maryland Monthly Revenue Heatmap
# ============================================================

# Build matrix: rows = months, cols = years
data_matrix = np.array([md_monthly[m] for m in MONTHS])  # shape (12, 5)

fig, ax = plt.subplots(figsize=(10, 6))

im = ax.imshow(data_matrix, cmap='RdYlGn', aspect='auto', vmin=1, vmax=55)

# Axis labels
ax.set_xticks(range(5))
ax.set_xticklabels(['2021', '2022', '2023', '2024', '2025'], fontsize=10)
ax.set_yticks(range(12))
ax.set_yticklabels(MONTHS, fontsize=9)

# Cell value labels
for i in range(12):
    for j in range(5):
        val = data_matrix[i, j]
        text_color = 'white' if (val < 15 or val > 45) else 'black'
        ax.text(j, i, f'${val:.1f}M', ha='center', va='center',
                fontsize=7.5, color=text_color, fontweight='bold')

# Highlight July 2021 floor tax anomaly
ax.add_patch(plt.Rectangle((-0.5, -0.5), 1, 1,
             fill=False, edgecolor='red', linewidth=2.5))
ax.text(0, -1.1, 'Floor tax\nanomaly', ha='center',
        fontsize=7, color=RED, fontweight='bold')

# Highlight October 2022 (first full month after DC flavor ban Oct 1 2022)
ax.add_patch(plt.Rectangle((1.5, 2.5), 1, 1,
             fill=False, edgecolor='purple', linewidth=2.5))
ax.text(2.55, 3.0, '← DC flavor ban\n   Oct 2022',
        ha='left', fontsize=6.5, color='purple', fontweight='bold')

# Color bar
cbar = plt.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label('Revenue ($M)', fontsize=9)

ax.set_title('Figure 6. Maryland Monthly Cigarette Stamp Revenue Heatmap (FY2021–FY2025)',
             fontsize=12, fontweight='bold', pad=14)
fig.text(0.01, -0.03,
         'Note. Green = higher revenue; Red = lower revenue. '
         'July 2021 anomaly reflects floor tax transition period. '
         'Purple box = first full month after DC flavored tobacco ban effective Oct 1, 2022.',
         fontsize=7.5, color='#555555', style='italic')

plt.tight_layout()
plt.savefig('fig6_md_monthly_heatmap.png')
plt.show()
plt.close()
print("Figure 6 saved.")


# ============================================================
# FIGURE 7 — Stacked Area: Total Revenue Composition
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for ax, cig, otp, c1, c2, title in [
    (axes[0], va_cig, va_otp, VA_BLUE, VA_LIGHT, 'Virginia'),
    (axes[1], md_cig, md_otp, MD_GREEN, MD_LIGHT, 'Maryland'),
]:
    # Stacked area: OTP on bottom, Cigarette on top
    ax.stackplot(X, otp, cig, colors=[c2, c1],
                 labels=['OTP Revenue', 'Cigarette Revenue'], alpha=0.85)

    # Total line
    totals = [c + o for c, o in zip(cig, otp)]
    ax.plot(X, totals, color='#333333', linewidth=1.5, linestyle='--', label='Total')

    # Total labels
    for i, t in enumerate(totals):
        ax.annotate(f'${t:.0f}M', (i, t), textcoords='offset points',
                    xytext=(0, 7), ha='center', fontsize=8, fontweight='bold', color='#333333')

    ax.set_xticks(X)
    ax.set_xticklabels(YEARS, fontsize=9, rotation=10)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmt_dollar))
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.legend(fontsize=8, loc='upper right')
    ax.set_ylabel('Revenue (USD Millions)', fontsize=9)

fig.suptitle('Figure 7. Total Tobacco Revenue Composition: Cigarette vs. OTP (FY2021–FY2025)',
             fontsize=12, fontweight='bold', y=1.02)
fig.text(0.01, -0.04, SOURCE_NOTE, fontsize=7.5, color='#555555', style='italic')

plt.tight_layout()
plt.savefig('fig7_stacked_area_total_revenue.png')
plt.show()
plt.close()
print("Figure 7 saved.")


print("\n✅ All 7 figures saved successfully.")
print("Files created:")
for i, name in enumerate([
    'fig1_cigarette_revenue_comparison.png',
    'fig2_otp_revenue_comparison.png',
    'fig3_grouped_bar_cigarette_otp.png',
    'fig4_tax_rate_differential.png',
    'fig5_yoy_change.png',
    'fig6_md_monthly_heatmap.png',
    'fig7_stacked_area_total_revenue.png',
], 1):
    print(f"  Figure {i}: {name}")
