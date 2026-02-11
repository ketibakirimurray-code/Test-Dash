# Plotly & Dash Visualization Examples

A collection of interactive data visualization examples using Plotly and Dash.

> 📚 **New to this?** Check out our [Simple Beginner's Guide](HOW_WE_MADE_THIS.md) - written so anyone can understand it!

## 📊 What's Included

### Basic Examples
- **plotly_example.py** - Simple line and bar charts to get started
- **dash_app.py** - Basic interactive dashboard with dropdown filters

### Advanced Plotly Examples
- **plotly_advanced.py** - 5 advanced visualizations:
  - Multi-subplot dashboard
  - 3D surface plot
  - Animated scatter plot
  - Candlestick chart
  - Correlation heatmap

### Data Science Examples
- **plotly_data_science.py** - 6 statistical visualizations:
  - Statistical distributions with Q-Q plots
  - Time series decomposition
  - Scatter matrix with correlations
  - Box plots for outlier detection
  - Regression analysis with residuals
  - Violin plots

### Advanced Dashboard
- **dash_advanced.py** - Multi-page interactive dashboard featuring:
  - 3 tabs: Sales Overview, Product Analysis, Regional Insights
  - Interactive date range filtering
  - Real-time data updates
  - KPI cards and multiple chart types
  - Professional styling

### Banking & Finance Application
- **raroc_bank_model.py** - RAROC Model for Commercial Term Loan Pricing:
  - Phase 1: Cash flow analysis and present value calculations
  - Calculate Interest Income/Expense with FTP (Funds Transfer Pricing)
  - Non-Interest Income/Expense tracking
  - Full amortization schedule (P&I calculations)
  - Present value discounting
  - PD (Probability of Default) scale: 1-13
  - LGD (Loss Given Default) scale: A-H
  - Manual entry or CSV file upload
  - Interactive visualizations and export to CSV
  - **Sample data:** `sample_loan_data.csv`

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd Keti
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Running the Examples

**Run Plotly examples** (opens charts in browser):
```bash
python plotly_example.py
python plotly_advanced.py
python plotly_data_science.py
```

**Run Dash apps** (starts web server):
```bash
python dash_app.py
# Then open http://127.0.0.1:8050/ in your browser

# Or run the advanced dashboard:
python dash_advanced.py

# Or run the RAROC banking model:
python raroc_bank_model.py
```

## 📦 Dependencies

- plotly
- dash
- pandas
- numpy
- scipy

See `requirements.txt` for specific versions.

## 🤝 Contributing

Feel free to fork this project and add your own visualization examples!

## 📝 License

This project is open source and available for educational purposes.
