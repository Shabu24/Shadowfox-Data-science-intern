import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Rent', 'Food', 'Transport', 'Entertainment', 'Savings']
sizes = [30, 25, 15, 10, 20]
explode = (0.05, 0, 0, 0, 0)  # "Explode" the first slice
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#DAB3FF']

# Create figure
fig, ax = plt.subplots(figsize=(8, 8))

# Create pie chart
wedges, texts, autotexts = ax.pie(sizes, 
                                  explode=explode, 
                                  labels=labels, 
                                  colors=colors,
                                  autopct='%1.1f%%',
                                  startangle=90,
                                  shadow=True,
                                  textprops={'fontsize': 12})

# Equal aspect ratio ensures pie is drawn as a circle
ax.axis('equal')  
ax.set_title('Monthly Budget Distribution', fontsize=14, pad=20)

# Make the percentage texts white and bold
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

plt.tight_layout()
plt.show()