import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
np.random.seed(42)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]
labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

# Create figure
fig, ax = plt.subplots(figsize=(8, 6))

# Create boxplot
box = ax.boxplot(data, 
                 labels=labels,
                 patch_artist=True,
                 medianprops={'color': 'black', 'linewidth': 2})

# Customize colors
colors = ['lightblue', 'lightgreen', 'pink', 'wheat']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize plot
ax.set_title('Box Plot Example', fontsize=14)
ax.set_ylabel('Values', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()