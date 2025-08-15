import pandas as pd

# Extract function to read CSV data into a DataFrame
def extract(csv_path):
    
    # TODO: add error handling 

    return pd.read_csv(csv_path, parse_dates=['timestamp'])
    

