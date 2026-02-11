# Simple Plotly Example - Interactive Chart
import plotly.graph_objects as go
import plotly.express as px

# Example 1: Simple line chart
x_data = [1, 2, 3, 4, 5]
y_data = [10, 15, 13, 17, 20]

fig = go.Figure(data=go.Scatter(x=x_data, y=y_data, mode='lines+markers'))
fig.update_layout(
    title='My First Plotly Chart',
    xaxis_title='X Axis',
    yaxis_title='Y Axis'
)

# This will open in your browser
fig.show()

print("Plotly chart opened in your browser!")

# Example 2: Bar chart with sample data
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [23, 45, 56, 78, 32]
}

fig2 = px.bar(data, x='Category', y='Values', title='Sample Bar Chart')
fig2.show()

print("Bar chart opened in your browser!")
