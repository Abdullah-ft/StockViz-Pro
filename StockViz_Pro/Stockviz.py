import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import time
import numpy as np
import os

# Page configuration
st.set_page_config(
    page_title="Stock Market Dashboard 📈",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
with open(os.path.join(os.path.dirname(__file__), 'styles.css')) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize session state
if 'current_section' not in st.session_state:
    st.session_state.current_section = 'single_stock'
if 'search_query' not in st.session_state:
    st.session_state.search_query = ''
if 'comparison_time_period' not in st.session_state:
    st.session_state.comparison_time_period = '1y'



# Sidebar
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <h2 class="animated-heading">📈 Stock Market Dashboard</h2>
        </div>
        <div class="sidebar-info">
            <ul class="sidebar-list">
                <li>🚀 Real-time stock data updates</li>
                <li>📊 Visualize historical stock trends</li>
                <li>🔎 Search and analyze any stock</li>
                <li>📅 Compare stock performance over time</li>
                <li>💡 Get insights and predictions</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)



# Main Content

# Additional Professional Heading Update
st.markdown("""
    <div class="dynamic-header">
        <div class="header-symbol">⚡</div>
        <h1 class="header-title">StockViz Pro</h1>
    </div>
""", unsafe_allow_html=True)

try:
    # Single Stock Section
    st.markdown("<div id='single-stock' class='section animate-fade-in'>", unsafe_allow_html=True)
    st.markdown("""
        <div class="section-header">
            <span class="section-symbol">⚡</span>
            <h2 class="section-title">Single Stock Analysis</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Single stock input
    single_stock = st.text_input("Enter Stock Symbol (e.g., AAPL)", "AAPL").upper()
    
    if single_stock:
        stock = yf.Ticker(single_stock)
        info = stock.info
        hist = stock.history(period="1y")
        
        # Stock Info Card
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                label="Current Price",
                value=f"${info.get('currentPrice', 'N/A'):,.2f}",
                delta=f"{info.get('regularMarketChangePercent', 0):.2f}%"
            )
        with col2:
            st.metric(
                label="Market Cap",
                value=f"${info.get('marketCap', 0)/1e9:,.2f}B",
                delta=None
            )
        with col3:
            st.metric(
                label="Volume",
                value=f"{info.get('volume', 0):,}",
                delta=None
            )
        
        # Stock Price Chart
        st.subheader("Stock Price Trend")
        fig = go.Figure(data=[go.Candlestick(
            x=hist.index,
            open=hist['Open'],
            high=hist['High'],
            low=hist['Low'],
            close=hist['Close']
        )])
        
        fig.update_layout(
            template='plotly_dark',
            xaxis_title="Date",
            yaxis_title="Price",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Company Information
        st.subheader("Company Information")
        company_info = pd.DataFrame({
            'Metric': ['Name', 'Sector', 'Industry', 'Country', 'Website'],
            'Value': [
                info.get('longName', 'N/A'),
                info.get('sector', 'N/A'),
                info.get('industry', 'N/A'),
                info.get('country', 'N/A'),
                info.get('website', 'N/A')
            ]
        })
        st.dataframe(company_info, hide_index=True)
    
    # Stock Comparison Section
    st.markdown("<div id='stock-comparison' class='section animate-fade-in'>", unsafe_allow_html=True)
    st.markdown("""
        <div class="section-header">
            <span class="section-symbol">⚡</span>
            <h2 class="section-title">Stock Comparison</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Time period selection for comparison with slider styling injected via CSS below
    time_period = st.select_slider(
        "Select Time Period",
        options=['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'],
        value=st.session_state.comparison_time_period,
        key='comparison_time_period'
    )
    
    # Multiple stocks input
    stock_symbols = st.text_input(
        "Enter Stock Symbols (comma-separated, e.g., AAPL,MSFT,GOOGL)", 
        "AAPL,MSFT,GOOGL"
    ).upper().split(',')
    stock_symbols = [symbol.strip() for symbol in stock_symbols]
    
    if len(stock_symbols) > 1:
        # Fetch data for all stocks
        stocks_data = {}
        for symbol in stock_symbols:
            stock = yf.Ticker(symbol)
            info = stock.info
            hist = stock.history(period=time_period)
            stocks_data[symbol] = {
                'info': info,
                'history': hist
            }
        
        # Display metrics for each stock
        st.subheader("Stock Metrics Comparison")
        metrics_cols = st.columns(len(stock_symbols))
        
        for idx, symbol in enumerate(stock_symbols):
            with metrics_cols[idx]:
                st.markdown(f"""
                    <div class="metric-card animate-slide-in" style="animation-delay: {idx * 0.1}s">
                        <h3>{symbol}</h3>
                        <p>Current Price: ${stocks_data[symbol]['info'].get('currentPrice', 'N/A'):,.2f}</p>
                        <p>Change: {stocks_data[symbol]['info'].get('regularMarketChangePercent', 0):.2f}%</p>
                    </div>
                """, unsafe_allow_html=True)
        
        # Comparison Price Chart
        st.subheader("Stock Price Comparison")
        comparison_fig = go.Figure()
        
        for symbol in stock_symbols:
            hist = stocks_data[symbol]['history']
            if not hist.empty:
                first_price = hist['Close'].iloc[0]
                normalized_prices = (hist['Close'] - first_price) / first_price * 100
                
                comparison_fig.add_trace(go.Scatter(
                    x=hist.index,
                    y=normalized_prices,
                    name=symbol,
                    mode='lines',
                    line=dict(width=2)
                ))
        
        comparison_fig.update_layout(
            template='plotly_dark',
            xaxis_title="Date",
            yaxis_title="Price Change (%)",
            height=500,
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01
            )
        )
        
        st.plotly_chart(comparison_fig, use_container_width=True)
        
        # Correlation Matrix
        st.subheader("Stock Correlation Matrix")
        close_prices = pd.DataFrame({
            symbol: stocks_data[symbol]['history']['Close']
            for symbol in stock_symbols
        })
        
        correlation_matrix = close_prices.corr()
        correlation_fig = go.Figure(data=go.Heatmap(
            z=correlation_matrix.values,
            x=correlation_matrix.columns,
            y=correlation_matrix.columns,
            colorscale='RdBu',
            zmid=0,
            text=np.round(correlation_matrix.values, 2),
            texttemplate='%{text}',
            textfont={"size": 10}
        ))
        
        correlation_fig.update_layout(
            template='plotly_dark',
            title='Stock Price Correlation Matrix',
            height=500,
            width=800
        )
        
        st.plotly_chart(correlation_fig, use_container_width=True)
    
    # Market Overview Section
    st.markdown("<div id='market-overview' class='section animate-fade-in'>", unsafe_allow_html=True)
    st.markdown("""
        <div class="section-header">
            <span class="section-symbol">⚡</span>
            <h2 class="section-title">Market Overview</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Add market indices
    indices = {
        "^GSPC": "S&P 500",
        "^DJI": "Dow Jones",
        "^IXIC": "NASDAQ",
        "^FTSE": "FTSE 100"
    }
    
    for symbol, name in indices.items():
        try:
            index = yf.Ticker(symbol)
            info = index.info
            st.metric(
                label=name,
                value=f"{info.get('regularMarketPrice', 'N/A'):,.2f}",
                delta=f"{info.get('regularMarketChangePercent', 0):.2f}%"
            )
        except:
            st.warning(f"Unable to fetch data for {name}")

except Exception as e:
    st.error("Error fetching data. Please check the symbols and try again.")
    st.error(str(e))

# Custom Slider CSS Injection for blue slider with shadows
st.sidebar.markdown("""
    <style>
    .stSlider > div > div > div > div {
        background-color: #4a4eff !important;
        box-shadow: 0px 0px 5px rgba(0, 0, 255, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

