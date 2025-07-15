import matplotlib.pyplot as plt

# Sample data
categories = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Pears']
quantities = [23, 45, 37, 28, 19]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Create bar chart
bars = ax.bar(categories, quantities, color=colors)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height}',
            ha='center', va='bottom')

# Customize the chart
ax.set_title('Fruit Inventory', fontsize=14, pad=20)
ax.set_ylabel('Quantity', fontsize=12)
ax.set_ylim(0, 50)
ax.grid(axis='y', linestyle='--', alpha=0.4)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()