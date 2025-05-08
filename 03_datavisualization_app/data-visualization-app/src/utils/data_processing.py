import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """Clean the data for plotting."""
    # Example cleaning steps
    data.dropna(inplace=True)  # Remove missing values
    # Additional cleaning steps can be added here
    return data