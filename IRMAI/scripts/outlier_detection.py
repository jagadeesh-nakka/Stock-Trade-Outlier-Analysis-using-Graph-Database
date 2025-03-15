import numpy as np
from scipy.stats import zscore

def detect_outliers(data, column):
    """
    Detect outliers in the data using the Z-score method.
    Args:
        data (pd.DataFrame): Input data.
        column (str): Column to analyze for outliers.
    Returns:
        pd.DataFrame: DataFrame containing outliers.
    """
    print(data,column) 
    try:
        # Calculate Z-scores
        data['zscore'] = zscore(data[column])
        
        # Identify outliers (Z-score > 3 or < -3)
        print(data['zscore'])
        outliers = data[(data['zscore'] > 1) | (data['zscore'] < -1)]
        print(outliers)
        return outliers
    except KeyError:
        print(f"Error: Column '{column}' not found in the data.")
        return None