import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.arange(1, 11)
y1 = np.array([1, 3, 4, 6, 8, 9, 8, 7, 6, 7])
y2 = np.array([1, 2, 2, 3, 4, 5, 6, 7, 8, 9])
y3 = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Create stacked area
ax.stackplot(x, y1, y2, y3, 
             labels=['Product A', 'Product B', 'Product C'],
             colors=['#8dd3c7', '#ffffb3', '#bebada'],
             alpha=0.8)

# Customize
ax.set_title('Product Sales Over Time', fontsize=14)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales Volume', fontsize=12)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.3)
ax.set_xlim(1, 10)

plt.tight_layout()
plt.show()