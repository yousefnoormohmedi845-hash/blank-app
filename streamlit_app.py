import streamlit as st
import pandas as pd
import requests
import ta
import plotly.graph_objects as go

st.set_page_config(page_title="SUN/USDT Dashboard", layout="wide")
st.title("SUN/USDT Technical Dashboard 📈")

def get_binance_data(symbol="SUNUSDT", interval="1h", limit=500):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
        data = requests.get(url).json()
            df = pd.DataFrame(data, columns=[
                    "timestamp", "open", "high", "low", "close", "volume",
                            "close_time", "quote_asset_volume", "number_of_trades",
                                    "taker_buy_base_volume", "taker_buy_quote_volume", "ignore"
                                        ])
                                            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
                                                df.set_index("timestamp", inplace=True)
                                                    df = df.astype(float)
                                                        return df

                                                        def add_indicators(df):
                                                            df["rsi"] = ta.momentum.RSIIndicator(close=df["close"]).rsi()
                                                                macd = ta.trend.MACD(close=df["close"])
                                                                    df["macd"] = macd.macd()
                                                                        df["macd_signal"] = macd.macd_signal()
                                                                            return df

                                                                            df = get_binance_data()
                                                                            df = add_indicators(df)

                                                                            fig = go.Figure()
                                                                            fig.add_trace(go.Candlestick(
                                                                                x=df.index,
                                                                                    open=df["open"],
                                                                                        high=df["high"],
                                                                                            low=df["low"],
                                                                                                close=df["close"],
                                                                                                    name="Candlestick"
                                                                                                    ))
                                                                                                    fig.update_layout(title="SUN/USDT Price Chart", xaxis_rangeslider_visible=False)
                                                                                                    st.plotly_chart(fig, use_container_width=True)

                                                                                                    st.subheader("RSI Indicator")
                                                                                                    st.line_chart(df["rsi"])

                                                                                                    st.subheader("MACD Indicator")
                                                                                                    st.line_chart(df[["macd", "macd_signal"]])
