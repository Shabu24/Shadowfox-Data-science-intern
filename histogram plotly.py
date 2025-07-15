import plotly.express as px
import numpy as np
x = np.random.randn(1000)
fig = px.histogram(x, nbins=30, title='Distribution')
fig.show()