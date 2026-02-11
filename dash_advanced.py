# Advanced Dash App - Multi-Page Dashboard with Real-Time Updates
import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Initialize the app with custom styling
app = dash.Dash(__name__)

# Generate sample data
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
df_sales = pd.DataFrame({
    'Date': dates,
    'Sales': np.random.poisson(100, len(dates)) + np.sin(np.arange(len(dates)) * 2 * np.pi / 365) * 20,
    'Revenue': np.random.normal(5000, 1000, len(dates)),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], len(dates))
})

# Product data
products = pd.DataFrame({
    'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'Sales': [245, 320, 198, 275, 410],
    'Profit': [12000, 18000, 9000, 14000, 22000],
    'Category': ['Electronics', 'Clothing', 'Food', 'Electronics', 'Clothing']
})

# Custom CSS styling
app.layout = html.Div([
    # Header
    html.Div([
        html.H1('📊 Advanced Analytics Dashboard',
                style={'color': 'white', 'textAlign': 'center', 'margin': '0', 'padding': '20px'}),
        html.P('Real-time data visualization and interactive analytics',
               style={'color': 'white', 'textAlign': 'center', 'margin': '0', 'paddingBottom': '20px'})
    ], style={'backgroundColor': '#2c3e50'}),

    # Navigation Tabs
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='📈 Sales Overview', value='tab-1'),
        dcc.Tab(label='🏆 Product Analysis', value='tab-2'),
        dcc.Tab(label='🌍 Regional Insights', value='tab-3'),
    ], style={'fontSize': '16px'}),

    # Tab content
    html.Div(id='tabs-content', style={'padding': '20px'}),

    # Real-time update section
    html.Div([
        html.Hr(),
        html.H3('⚡ Live Data Simulation', style={'textAlign': 'center'}),
        html.Div([
            html.Button('Start Live Updates', id='start-button', n_clicks=0,
                       style={'backgroundColor': '#27ae60', 'color': 'white', 'padding': '10px 20px',
                              'border': 'none', 'borderRadius': '5px', 'fontSize': '16px', 'margin': '10px'}),
            html.Button('Stop Updates', id='stop-button', n_clicks=0,
                       style={'backgroundColor': '#e74c3c', 'color': 'white', 'padding': '10px 20px',
                              'border': 'none', 'borderRadius': '5px', 'fontSize': '16px', 'margin': '10px'}),
        ], style={'textAlign': 'center'}),

        dcc.Interval(id='interval-component', interval=2000, n_intervals=0, disabled=True),

        html.Div([
            html.Div(id='live-sales', style={'fontSize': '24px', 'fontWeight': 'bold', 'color': '#27ae60'}),
            dcc.Graph(id='live-graph')
        ], style={'textAlign': 'center', 'marginTop': '20px'})
    ], style={'backgroundColor': '#ecf0f1', 'padding': '20px', 'margin': '20px', 'borderRadius': '10px'})

], style={'fontFamily': 'Arial, sans-serif'})


# Callback for tab content
@app.callback(
    Output('tabs-content', 'children'),
    Input('tabs', 'value')
)
def render_content(tab):
    if tab == 'tab-1':
        # Sales Overview Tab
        return html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Sales', style={'color': '#3498db'}),
                    html.H2(f'{df_sales["Sales"].sum():,.0f}', style={'color': '#2c3e50'})
                ], style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px',
                         'boxShadow': '2px 2px 10px rgba(0,0,0,0.1)', 'flex': '1', 'margin': '10px'}),

                html.Div([
                    html.H3('Avg Revenue', style={'color': '#e74c3c'}),
                    html.H2(f'${df_sales["Revenue"].mean():,.0f}', style={'color': '#2c3e50'})
                ], style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px',
                         'boxShadow': '2px 2px 10px rgba(0,0,0,0.1)', 'flex': '1', 'margin': '10px'}),

                html.Div([
                    html.H3('Total Revenue', style={'color': '#27ae60'}),
                    html.H2(f'${df_sales["Revenue"].sum():,.0f}', style={'color': '#2c3e50'})
                ], style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px',
                         'boxShadow': '2px 2px 10px rgba(0,0,0,0.1)', 'flex': '1', 'margin': '10px'}),
            ], style={'display': 'flex', 'justifyContent': 'space-around'}),

            html.Div([
                dcc.Graph(
                    figure=px.line(df_sales, x='Date', y='Sales',
                                  title='Sales Trend Over Time')
                        .update_traces(line_color='#3498db', line_width=3)
                )
            ], style={'marginTop': '20px'}),

            html.Div([
                html.Label('Select Date Range:', style={'fontSize': '18px', 'fontWeight': 'bold'}),
                dcc.DatePickerRange(
                    id='date-picker-range',
                    start_date=df_sales['Date'].min(),
                    end_date=df_sales['Date'].max(),
                    display_format='YYYY-MM-DD'
                ),
                dcc.Graph(id='filtered-sales-graph')
            ], style={'marginTop': '20px'})
        ])

    elif tab == 'tab-2':
        # Product Analysis Tab
        return html.Div([
            html.Div([
                dcc.Graph(
                    figure=px.bar(products, x='Product', y='Sales', color='Category',
                                 title='Sales by Product',
                                 color_discrete_sequence=px.colors.qualitative.Set2)
                        .update_layout(showlegend=True)
                )
            ], style={'width': '48%', 'display': 'inline-block'}),

            html.Div([
                dcc.Graph(
                    figure=px.pie(products, values='Profit', names='Product',
                                 title='Profit Distribution by Product',
                                 hole=0.4)
                )
            ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'}),

            html.Div([
                dcc.Graph(
                    figure=px.scatter(products, x='Sales', y='Profit', size='Profit',
                                     color='Category', hover_name='Product',
                                     title='Sales vs Profit Analysis',
                                     size_max=60)
                )
            ], style={'marginTop': '20px'})
        ])

    elif tab == 'tab-3':
        # Regional Insights Tab
        regional_data = df_sales.groupby('Region').agg({
            'Sales': 'sum',
            'Revenue': 'sum'
        }).reset_index()

        return html.Div([
            html.Div([
                dcc.Graph(
                    figure=px.bar(regional_data, x='Region', y='Sales',
                                 title='Sales by Region',
                                 color='Sales',
                                 color_continuous_scale='Viridis')
                )
            ], style={'width': '48%', 'display': 'inline-block'}),

            html.Div([
                dcc.Graph(
                    figure=go.Figure(data=[go.Pie(
                        labels=regional_data['Region'],
                        values=regional_data['Revenue'],
                        pull=[0.1, 0, 0, 0]
                    )]).update_layout(title='Revenue Distribution by Region')
                )
            ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'}),

            html.Div([
                dcc.Graph(
                    figure=px.box(df_sales, x='Region', y='Sales',
                                 title='Sales Distribution by Region',
                                 color='Region')
                )
            ], style={'marginTop': '20px'})
        ])


# Callback for filtered sales graph
@app.callback(
    Output('filtered-sales-graph', 'figure'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date')
)
def update_filtered_graph(start_date, end_date):
    filtered_df = df_sales[(df_sales['Date'] >= start_date) & (df_sales['Date'] <= end_date)]
    fig = px.area(filtered_df, x='Date', y='Revenue',
                  title=f'Revenue from {start_date} to {end_date}')
    fig.update_traces(fill='tozeroy', line_color='#e74c3c')
    return fig


# Callbacks for live updates
@app.callback(
    Output('interval-component', 'disabled'),
    Input('start-button', 'n_clicks'),
    Input('stop-button', 'n_clicks'),
    State('interval-component', 'disabled')
)
def toggle_interval(start_clicks, stop_clicks, disabled):
    if start_clicks > stop_clicks:
        return False
    return True


@app.callback(
    Output('live-sales', 'children'),
    Output('live-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_live_data(n):
    # Simulate real-time data
    current_sales = np.random.randint(80, 150)

    # Generate last 20 data points
    time_points = list(range(max(0, n-19), n+1))
    sales_points = [np.random.randint(80, 150) for _ in time_points]

    fig = go.Figure(data=go.Scatter(
        x=time_points,
        y=sales_points,
        mode='lines+markers',
        line=dict(color='#27ae60', width=3),
        marker=dict(size=8)
    ))

    fig.update_layout(
        title='Live Sales Updates',
        xaxis_title='Time Interval',
        yaxis_title='Sales Count',
        height=400
    )

    return f'Current Sales: {current_sales} units', fig


if __name__ == '__main__':
    print("\n" + "="*70)
    print("Advanced Dash Dashboard is running!")
    print("="*70)
    print("\nFeatures:")
    print("   - Multiple interactive tabs (Sales, Products, Regional)")
    print("   - Date range filtering")
    print("   - Real-time data updates")
    print("   - Interactive charts and graphs")
    print("\nOpen your browser: http://127.0.0.1:8050/")
    print("Press Ctrl+C to stop\n")
    print("="*70 + "\n")
    app.run(debug=True)
