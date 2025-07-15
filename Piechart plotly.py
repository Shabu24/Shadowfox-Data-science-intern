import plotly.express as px
data = {'Category': ['A', 'B', 'C'], 'Value': [25, 40, 35]}
fig = px.pie(data, values='Value', names='Category', hole=0.3)
fig.show()