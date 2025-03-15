import matplotlib.pyplot as plt
import pandas as pd

def plot_trades(data, outliers):
    plt.figure(figsize=(10, 6))
    plt.plot(data['timestamp'], data['price'], label="Normal Trades")
    plt.scatter(outliers['timestamp'], outliers['price'], color='red', label="Outliers")
    plt.xlabel("Timestamp")
    plt.ylabel("Price")
    plt.title("FX Trade Outlier Analysis")
    plt.legend()
    plt.show()

# Example usage
if __name__ == "__main__":
    from data_collection import load_data
    from outlier_detection import detect_outliers
    file_path = "../data/fx_trades.csv"
    fx_data = load_data(file_path)
    fx_data=fx_data.dropna()
    outliers = detect_outliers(fx_data, 'price')
    plot_trades(fx_data, outliers)