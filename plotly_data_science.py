# Data Science Focused Plotly Examples
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
from scipy import stats

print("Creating data science visualizations...\n")

# Example 1: Statistical Distribution Analysis
print("1. Creating statistical distribution plots...")
np.random.seed(42)
normal_data = np.random.normal(100, 15, 1000)
exponential_data = np.random.exponential(2, 1000)
uniform_data = np.random.uniform(0, 100, 1000)

fig1 = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Normal Distribution', 'Exponential Distribution',
                   'Uniform Distribution', 'Q-Q Plot'),
    specs=[[{'type': 'histogram'}, {'type': 'histogram'}],
           [{'type': 'histogram'}, {'type': 'scatter'}]]
)

# Normal distribution
fig1.add_trace(go.Histogram(x=normal_data, name='Normal', nbinsx=50,
                            marker_color='lightblue'), row=1, col=1)

# Exponential distribution
fig1.add_trace(go.Histogram(x=exponential_data, name='Exponential', nbinsx=50,
                            marker_color='lightcoral'), row=1, col=2)

# Uniform distribution
fig1.add_trace(go.Histogram(x=uniform_data, name='Uniform', nbinsx=50,
                            marker_color='lightgreen'), row=2, col=1)

# Q-Q Plot
sorted_data = np.sort(normal_data)
theoretical_quantiles = stats.norm.ppf(np.linspace(0.01, 0.99, len(sorted_data)))
fig1.add_trace(go.Scatter(x=theoretical_quantiles, y=sorted_data, mode='markers',
                         name='Q-Q Plot', marker_color='purple'), row=2, col=2)
fig1.add_trace(go.Scatter(x=theoretical_quantiles, y=theoretical_quantiles,
                         mode='lines', name='Reference Line',
                         line=dict(color='red', dash='dash')), row=2, col=2)

fig1.update_layout(height=800, showlegend=True,
                  title_text="Statistical Distribution Analysis")
fig1.show()

# Example 2: Time Series Decomposition
print("2. Creating time series decomposition...")
# Generate time series with trend, seasonality, and noise
time = np.arange(0, 365)
trend = 0.1 * time + 50
seasonal = 10 * np.sin(2 * np.pi * time / 30)
noise = np.random.normal(0, 2, len(time))
ts_data = trend + seasonal + noise

fig2 = make_subplots(
    rows=4, cols=1,
    subplot_titles=('Original Time Series', 'Trend', 'Seasonality', 'Residuals'),
    vertical_spacing=0.08
)

fig2.add_trace(go.Scatter(x=time, y=ts_data, mode='lines', name='Original',
                         line=dict(color='blue')), row=1, col=1)
fig2.add_trace(go.Scatter(x=time, y=trend, mode='lines', name='Trend',
                         line=dict(color='red', width=3)), row=2, col=1)
fig2.add_trace(go.Scatter(x=time, y=seasonal, mode='lines', name='Seasonal',
                         line=dict(color='green')), row=3, col=1)
fig2.add_trace(go.Scatter(x=time, y=noise, mode='lines', name='Residuals',
                         line=dict(color='orange')), row=4, col=1)

fig2.update_layout(height=1000, title_text="Time Series Decomposition", showlegend=True)
fig2.show()

# Example 3: Correlation and Scatter Matrix
print("3. Creating scatter matrix...")
# Generate correlated variables
n = 200
x1 = np.random.randn(n)
x2 = x1 + np.random.randn(n) * 0.5
x3 = -x1 + np.random.randn(n) * 0.8
x4 = np.random.randn(n)

df = pd.DataFrame({
    'Feature 1': x1,
    'Feature 2': x2,
    'Feature 3': x3,
    'Feature 4': x4,
    'Category': np.random.choice(['A', 'B', 'C'], n)
})

fig3 = px.scatter_matrix(df, dimensions=['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4'],
                         color='Category', title='Scatter Matrix with Correlations',
                         height=900)
fig3.show()

# Example 4: Box Plot for Outlier Detection
print("4. Creating box plots for outlier detection...")
# Generate data with outliers
categories = ['Group A', 'Group B', 'Group C', 'Group D']
data_with_outliers = []
for i in range(4):
    group_data = np.random.normal(50 + i*10, 10, 100)
    # Add some outliers
    outliers = np.random.normal(50 + i*10, 30, 5)
    data_with_outliers.append(np.concatenate([group_data, outliers]))

fig4 = go.Figure()
for i, cat in enumerate(categories):
    fig4.add_trace(go.Box(y=data_with_outliers[i], name=cat, boxmean='sd'))

fig4.update_layout(
    title='Box Plot Analysis - Outlier Detection',
    yaxis_title='Values',
    showlegend=True,
    height=600
)
fig4.show()

# Example 5: Regression Analysis Visualization
print("5. Creating regression analysis plot...")
# Generate data for regression
x_reg = np.linspace(0, 10, 50)
y_true = 2.5 * x_reg + 5
y_noise = y_true + np.random.normal(0, 3, len(x_reg))

# Fit polynomial regressions
poly1 = np.polyfit(x_reg, y_noise, 1)
poly3 = np.polyfit(x_reg, y_noise, 3)

y_pred1 = np.polyval(poly1, x_reg)
y_pred3 = np.polyval(poly3, x_reg)

fig5 = go.Figure()

# Scatter plot
fig5.add_trace(go.Scatter(x=x_reg, y=y_noise, mode='markers',
                         name='Data Points', marker=dict(size=8, color='blue')))

# True line
fig5.add_trace(go.Scatter(x=x_reg, y=y_true, mode='lines',
                         name='True Relationship',
                         line=dict(color='green', dash='dash', width=2)))

# Linear regression
fig5.add_trace(go.Scatter(x=x_reg, y=y_pred1, mode='lines',
                         name='Linear Fit', line=dict(color='red', width=2)))

# Polynomial regression
fig5.add_trace(go.Scatter(x=x_reg, y=y_pred3, mode='lines',
                         name='Polynomial Fit (degree 3)',
                         line=dict(color='purple', width=2)))

# Add residuals
for i in range(0, len(x_reg), 3):
    fig5.add_trace(go.Scatter(x=[x_reg[i], x_reg[i]],
                             y=[y_noise[i], y_pred1[i]],
                             mode='lines', line=dict(color='gray', width=1, dash='dot'),
                             showlegend=False))

fig5.update_layout(
    title='Regression Analysis with Residuals',
    xaxis_title='X Variable',
    yaxis_title='Y Variable',
    height=600,
    hovermode='closest'
)
fig5.show()

# Example 6: Violin Plot for Distribution Comparison
print("6. Creating violin plots...")
categories_violin = ['Method A', 'Method B', 'Method C']
violin_data = [
    np.random.normal(100, 15, 200),
    np.random.gamma(5, 10, 200) + 50,
    np.concatenate([np.random.normal(80, 10, 100), np.random.normal(120, 10, 100)])
]

fig6 = go.Figure()
for i, cat in enumerate(categories_violin):
    fig6.add_trace(go.Violin(y=violin_data[i], name=cat, box_visible=True,
                            meanline_visible=True))

fig6.update_layout(
    title='Violin Plot - Distribution Comparison',
    yaxis_title='Values',
    height=600
)
fig6.show()

print("\n✅ All 6 data science visualizations opened in your browser!")
print("   - Statistical distributions with Q-Q plot")
print("   - Time series decomposition")
print("   - Scatter matrix with correlations")
print("   - Box plots for outlier detection")
print("   - Regression analysis with residuals")
print("   - Violin plots for distribution comparison")
