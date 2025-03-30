# 📈 StockViz-Pro: Real-Time Stock Market Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)

A **modern, interactive stock analytics dashboard** built with Streamlit to visualize real-time stock data, compare performance, and analyze market trends. Perfect for investors and data enthusiasts.

---

## 📦 Installation

### Prerequisites
- Python 3.8+
- `pip` package manager

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/StockViz-Pro.git
   cd StockViz-Pro
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**:
   ```bash
   streamlit run stockviz.py
   ```

---

## 🚀 Features

- **📊 Single Stock Analysis**  
  Track live prices, historical candlestick charts, and company details for any stock symbol (e.g., `AAPL`, `TSLA`).

- **🔗 Multi-Stock Comparison**  
  Compare up to 5 stocks with normalized price trends and correlation heatmaps over customizable timeframes (`1d` to `10y`).

- **🌐 Market Overview**  
  Monitor major indices like **S&P 500 (^GSPC)**, **NASDAQ (^IXIC)**, and **Dow Jones (^DJI)** in real time.

- **🎨 Dynamic UI**  
  Dark theme with animated gradients, hover effects, and responsive design.

---

## 🖥️ Usage

### Single Stock Analysis
1. Enter a stock symbol (e.g., `GOOGL`) in the input field.
2. View real-time metrics, candlestick charts, and company details.

### Stock Comparison
1. Enter comma-separated symbols (e.g., `MSFT,AMZN,NVDA`).
2. Adjust the time period slider and explore correlation heatmaps.

### Market Indices
- Scroll to the bottom to see live updates for major indices.

---

## 🛠️ Libraries Used

| Library    | Purpose                                      |
|------------|----------------------------------------------|
| Streamlit  | Build interactive web app interface        |
| yfinance   | Fetch real-time stock data                 |
| Plotly     | Render interactive charts                  |
| Pandas     | Clean and structure data                   |
| NumPy      | Normalize data for comparisons             |

---

## 🌍 Deployment

### Streamlit Cloud (Recommended)
1. Push the code to a GitHub repository.
2. Sign in to [Streamlit Cloud](https://share.streamlit.io/).
3. Deploy `stockviz.py` and add `requirements.txt` for dependencies.

---

## 📜 License
MIT License - See `LICENSE` for details.

---

## 🌟 Pro Tips
- Bookmark the dashboard for quick access to live market insights!
- 🐞 Report Issues: [GitHub Issues](https://github.com/your-username/StockViz-Pro/issues)

