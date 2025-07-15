import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
x_values = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y_values = np.sin(x_values)  # Sine wave

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
ax.plot(x_values, y_values, 
        color='royalblue', 
        linewidth=2, 
        label='Sine Wave')

# Customize the plot
ax.set_title('Basic Line Plot of Sine Function', fontsize=14)
ax.set_xlabel('X Values', fontsize=12)
ax.set_ylabel('sin(X)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()