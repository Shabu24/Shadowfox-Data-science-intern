# Shadowfox-Data-science-intern-beginner-task
📊 ShadowFox Data Science Beginner Task: Data Visualization
This repository contains my solutions for the beginner-level data visualization task from ShadowFox, focusing on Matplotlib and Plotly for static and interactive graphs.

🚀 Features
Matplotlib: Static plots (line, bar, scatter, histograms) with custom styling.
Plotly: Interactive visualizations (hover tools, animations, 3D plots).
Jupyter Notebooks: Step-by-step explanations with code and outputs.
Datasets: Sample data (CSV/JSON) used for demonstration.

🛠️ Setup
Clone the repository:

bash
git clone https://github.com/your-username/shadowfox-data-viz.git
cd shadowfox-data-viz
Install dependencies:

bash
pip install -r requirements.txt
(Example requirements.txt: numpy, pandas, matplotlib, plotly, jupyter)

Run Jupyter Notebook:

bash
jupyter notebook

Example Code Snippets
Matplotlib (Static Plot)
python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 1], label='Sample Line')
plt.xlabel('X-axis'); plt.ylabel('Y-axis')
plt.legend(); plt.savefig('output/line_plot.png')
Plotly (Interactive Plot)
python
import plotly.express as px
fig = px.scatter(px.data.iris(), x="sepal_width", y="sepal_length", color="species")
fig.write_html('output/interactive_plot.html')
