# Advanced Plotly Examples - Multiple Chart Types
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd

print("Creating advanced Plotly visualizations...\n")

# Example 1: Multiple Subplots Dashboard
print("1. Creating multi-subplot dashboard...")
fig1 = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Line Plot', 'Bar Chart', 'Scatter Plot', 'Pie Chart'),
    specs=[[{'type': 'scatter'}, {'type': 'bar'}],
           [{'type': 'scatter'}, {'type': 'pie'}]]
)

# Line plot
x = np.linspace(0, 10, 100)
fig1.add_trace(go.Scatter(x=x, y=np.sin(x), name='sin(x)'), row=1, col=1)
fig1.add_trace(go.Scatter(x=x, y=np.cos(x), name='cos(x)'), row=1, col=1)

# Bar chart
categories = ['Product A', 'Product B', 'Product C', 'Product D']
values = [45, 60, 38, 52]
fig1.add_trace(go.Bar(x=categories, y=values, name='Revenue'), row=1, col=2)

# Scatter plot
np.random.seed(42)
fig1.add_trace(go.Scatter(
    x=np.random.randn(50),
    y=np.random.randn(50),
    mode='markers',
    marker=dict(size=10, color=np.random.randn(50), colorscale='Viridis', showscale=True),
    name='Random Data'
), row=2, col=1)

# Pie chart
fig1.add_trace(go.Pie(labels=['A', 'B', 'C', 'D'], values=[30, 25, 20, 25]), row=2, col=2)

fig1.update_layout(height=800, title_text="Multi-Chart Dashboard", showlegend=True)
fig1.show()

# Example 2: 3D Surface Plot
print("2. Creating 3D surface plot...")
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig2 = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])
fig2.update_layout(
    title='3D Surface Plot: sin(√(x² + y²))',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ),
    width=900,
    height=700
)
fig2.show()

# Example 3: Animated Scatter Plot
print("3. Creating animated scatter plot...")
# Create sample data for animation
np.random.seed(42)
n_frames = 20
df_anim = pd.DataFrame()

for frame in range(n_frames):
    temp_df = pd.DataFrame({
        'x': np.random.randn(30) + frame * 0.3,
        'y': np.random.randn(30) + frame * 0.2,
        'size': np.random.randint(10, 50, 30),
        'frame': frame
    })
    df_anim = pd.concat([df_anim, temp_df])

fig3 = px.scatter(df_anim, x='x', y='y', animation_frame='frame',
                  size='size', color='size',
                  range_x=[-5, 15], range_y=[-5, 12],
                  title='Animated Scatter Plot')
fig3.show()

# Example 4: Advanced Stock-like Candlestick Chart
print("4. Creating candlestick chart...")
dates = pd.date_range('2024-01-01', periods=30, freq='D')
np.random.seed(42)
open_prices = 100 + np.cumsum(np.random.randn(30))
high_prices = open_prices + np.random.uniform(1, 5, 30)
low_prices = open_prices - np.random.uniform(1, 5, 30)
close_prices = open_prices + np.random.randn(30) * 2

fig4 = go.Figure(data=[go.Candlestick(
    x=dates,
    open=open_prices,
    high=high_prices,
    low=low_prices,
    close=close_prices
)])

fig4.update_layout(
    title='Stock Price Candlestick Chart',
    yaxis_title='Price ($)',
    xaxis_title='Date',
    height=600
)
fig4.show()

# Example 5: Heatmap with Correlation Matrix
print("5. Creating correlation heatmap...")
# Generate correlated data
data = np.random.randn(100, 5)
df_corr = pd.DataFrame(data, columns=['Var A', 'Var B', 'Var C', 'Var D', 'Var E'])
correlation_matrix = df_corr.corr()

fig5 = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    colorscale='RdBu',
    zmid=0,
    text=correlation_matrix.values.round(2),
    texttemplate='%{text}',
    textfont={"size": 12}
))

fig5.update_layout(
    title='Correlation Heatmap',
    width=700,
    height=700
)
fig5.show()

print("\n✅ All 5 advanced Plotly visualizations opened in your browser!")
print("   - Multi-subplot dashboard")
print("   - 3D surface plot")
print("   - Animated scatter plot")
print("   - Candlestick chart")
print("   - Correlation heatmap")
