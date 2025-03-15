import pandas as pd

# Load data from CSV
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Example usage
if __name__ == "__main__":
    file_path = "../data/fx_trades.csv"
    fx_data = load_data(file_path)
    fx_data=fx_data.dropna()
    print(fx_data.head())