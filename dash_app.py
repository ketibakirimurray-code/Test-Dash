# Simple Dash App - Interactive Dashboard
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Create sample data
df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [4000, 5000, 4500, 6000, 7000, 6500],
    'Expenses': [2000, 2500, 2200, 2800, 3000, 2900]
})

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1('My First Dash Dashboard', style={'textAlign': 'center', 'color': '#2c3e50'}),

    html.Div([
        html.Label('Select Metric:'),
        dcc.Dropdown(
            id='metric-dropdown',
            options=[
                {'label': 'Sales', 'value': 'Sales'},
                {'label': 'Expenses', 'value': 'Expenses'}
            ],
            value='Sales'
        )
    ], style={'width': '50%', 'margin': 'auto', 'padding': '20px'}),

    dcc.Graph(id='sales-graph'),

    html.Div([
        html.H3('Dashboard Stats', style={'textAlign': 'center'}),
        html.P(f'Total Sales: ${df["Sales"].sum():,}', style={'textAlign': 'center'}),
        html.P(f'Total Expenses: ${df["Expenses"].sum():,}', style={'textAlign': 'center'}),
        html.P(f'Profit: ${df["Sales"].sum() - df["Expenses"].sum():,}', style={'textAlign': 'center'})
    ], style={'backgroundColor': '#ecf0f1', 'padding': '20px', 'margin': '20px', 'borderRadius': '10px'})
])

# Callback to update graph based on dropdown selection
@app.callback(
    Output('sales-graph', 'figure'),
    Input('metric-dropdown', 'value')
)
def update_graph(selected_metric):
    fig = px.line(df, x='Month', y=selected_metric,
                  title=f'{selected_metric} Over Time',
                  markers=True)
    fig.update_layout(yaxis_title=selected_metric, xaxis_title='Month')
    return fig

# Run the app
if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Dash app is running!")
    print("📊 Open your browser and go to: http://127.0.0.1:8050/")
    print("⏹️  Press Ctrl+C to stop the server")
    print("="*50 + "\n")
    app.run(debug=True)
