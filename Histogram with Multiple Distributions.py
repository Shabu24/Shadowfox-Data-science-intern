import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
data1 = np.random.normal(50, 10, 1000)
data2 = np.random.normal(70, 15, 800)
data3 = np.random.normal(30, 5, 1200)

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot histograms
ax.hist(data1, bins=30, alpha=0.6, label='Group A', color='skyblue')
ax.hist(data2, bins=30, alpha=0.6, label='Group B', color='salmon')
ax.hist(data3, bins=30, alpha=0.6, label='Group C', color='lightgreen')

# Customize
ax.set_title('Distribution Comparison', fontsize=14)
ax.set_xlabel('Values', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.3)
ax.legend(fontsize=10)

# Add mean lines
for data, color in zip([data1, data2, data3], ['blue', 'red', 'green']):
    ax.axvline(data.mean(), color=color, linestyle='dashed', linewidth=2)

plt.tight_layout()
plt.show()