from scripts.data_collection import load_data
from scripts.outlier_detection import detect_outliers
import matplotlib.pyplot as plt
import streamlit as st

st.title("FX Trade Outlier Analysis")

# Load data
file_path = "data/fx_trades.csv"
fx_data = load_data(file_path)
fx_data=fx_data.dropna()

# Detect outliers
outliers = detect_outliers(fx_data, 'close')  # Use 'close' instead of 'price'

# Display results
st.write("### Outliers Detected")
st.write(outliers)

# Plot
st.write("### Trade Price Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(fx_data.index, fx_data['close'], label="Normal Trades")
ax.scatter(outliers.index, outliers['close'], color='red', label="Outliers")
ax.set_xlabel("Timestamp")
ax.set_ylabel("Close Price")
ax.set_title("FX Trade Outlier Analysis")
ax.legend()
st.pyplot(fig)