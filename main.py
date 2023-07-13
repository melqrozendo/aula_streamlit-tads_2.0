import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import ta

# Título do app
st.title('Stock History App')

# Create a sidebar section for user input [BBAS3.SA / MSFT /]
st.sidebar.title("Selecione o stock:")
ticker_symbol = st.sidebar.text_input("Enter the stock symbol", value='AAPL', max_chars=10)

# Retrieve stock data using yfinance
data = yf.download(ticker_symbol, start="2020-01-01", end="2023-06-26")

# Calculate RSI
data['RSI'] = ta.momentum.RSIIndicator(data['Close']).rsi()

# Calculate IFM
data['IFM'] = ta.volume.force_index(data['Close'], data['Volume'])

# Calculate EMA
data['EMA'] = ta.trend.ema_indicator(data['Close'], window=20)

# Display the stock data in a dataframe
st.subheader("Stock History")
st.dataframe(data)

# Plot the closing price using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Closing Price'))
fig.update_layout(title=f"{ticker_symbol} Stock Price", xaxis_title="Date", yaxis_title="Price")
st.plotly_chart(fig)

# Plot RSI
fig_rsi = go.Figure()
fig_rsi.add_trace(go.Scatter(x=data.index, y=data['RSI'], name='RSI'))
fig_rsi.update_layout(title=f"{ticker_symbol} RSI", xaxis_title="Date", yaxis_title="RSI")
st.plotly_chart(fig_rsi)

# Plot IFM
fig_ifm = go.Figure()
fig_ifm.add_trace(go.Scatter(x=data.index, y=data['IFM'], name='IFM'))
fig_ifm.update_layout(title=f"{ticker_symbol} IFM", xaxis_title="Date", yaxis_title="IFM")
st.plotly_chart(fig_ifm)

# Plot EMA
fig_ema = go.Figure()
fig_ema.add_trace(go.Scatter(x=data.index, y=data['EMA'], name='EMA'))
fig_ema.update_layout(title=f"{ticker_symbol} EMA", xaxis_title="Date", yaxis_title="EMA")
st.plotly_chart(fig_ema)
