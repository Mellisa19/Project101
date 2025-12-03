import pandas as pd
import numpy as np
import sys

# Redirect stdout to a file
with open('analysis_output.txt', 'w') as f:
    sys.stdout = f
    
    # Load data
    try:
        df = pd.read_csv('dataset/safety_incidents.csv')
        print("Data Loaded Successfully")
        print("Shape:", df.shape)
        print("\n--- Info ---")
        df.info()
        print("\n--- Missing Values ---")
        print(df.isnull().sum())
        print("\n--- Head ---")
        print(df.head())
        print("\n--- Describe (Numerical) ---")
        print(df.describe())
        print("\n--- Describe (Categorical) ---")
        print(df.describe(include=['O']))
    except Exception as e:
        print(f"Error: {e}")
    
    sys.stdout = sys.__stdout__

