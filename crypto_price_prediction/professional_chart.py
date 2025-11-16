import matplotlib.pyplot as plt
import numpy as np

# Data
days = np.arange(1, 31)
prices = [95, 96, 96.5, 97, 98, 99, 99.5, 100, 99, 97, 
          98, 97, 98.5, 102, 103, 105, 107, 108, 109, 110,
          109, 108, 107, 109, 112, 113, 112, 113, 114, 115]

# Create chart
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10))

# === MAIN CHART ===
# Price line
ax1.plot(days, prices, 'o-', linewidth=4, markersize=8, 
         color='#2E86AB', markerfacecolor='#FF6B6B', 
         markeredgecolor='darkred', markeredgewidth=2,
         label='Daily Price', zorder=5)

# Colored phases
ax1.axvspan(1, 10, alpha=0.2, color='green', label='Gradual Rise')
ax1.axvspan(15, 20, alpha=0.2, color='orange', label='Strong Growth')
ax1.axvspan(21, 25, alpha=0.2, color='yellow', label='Volatility Phase')
ax1.axvspan(26, 30, alpha=0.2, color='purple', label='Consolidation')

# Key levels
ax1.axhline(y=100, color='red', linestyle='--', alpha=0.7, label='100 Level')
ax1.axhline(y=110, color='blue', linestyle='--', alpha=0.7, label='110 Level')

# Moving average
window = 3
ma = np.convolve(prices, np.ones(window)/window, mode='valid')
ax1.plot(days[window-1:], ma, color='red', linewidth=2.5, 
         label=f'{window}-Day Moving Average')

# === DAILY CHANGES CHART ===
changes = np.diff(prices)
colors = ['green' if x >= 0 else 'red' for x in changes]
ax2.bar(days[1:], changes, color=colors, alpha=0.8, edgecolor='white')
ax2.axhline(y=0, color='black', linewidth=1)

# === STYLING ===
# Titles and labels
ax1.set_title('📈 PROFESSIONAL PRICE ANALYSIS - NOVEMBER 2024', 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Price (USD)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Daily Change', fontsize=12, fontweight='bold')
ax2.set_xlabel('Day of Month', fontsize=12, fontweight='bold')

# Axis limits
ax1.set_xlim(0.5, 30.5)
ax1.set_ylim(90, 118)
ax2.set_ylim(-4, 4)

# Grid
ax1.grid(True, alpha=0.3)
ax2.grid(True, alpha=0.3)

# Ticks
ax1.set_xticks(range(1, 31, 2))
ax2.set_xticks(range(1, 31, 2))

# Legend
ax1.legend(loc='upper left', frameon=True, shadow=True)

# Statistics box
stats_text = f"""KEY STATISTICS:
• Min Price: {min(prices)} (Day 1)
• Max Price: {max(prices)} (Day 30)
• Average: {np.mean(prices):.1f}
• Total Growth: +{max(prices)-min(prices)} units
• Trend: BULLISH """

ax1.text(0.02, 0.02, stats_text, transform=ax1.transAxes, fontsize=11,
         bbox=dict(boxstyle="round,pad=0.8", facecolor="lightblue", alpha=0.8))

plt.tight_layout()

# high quality image
plt.savefig('professional_chart.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.show()

print("Chart generated successfully!")
print(" Image saved as 'professional_chart.png'")
