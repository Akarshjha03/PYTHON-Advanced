'''A program that reads an Excel file and prints the data in a tabular format'''

import pandas as pd

def read_excel_and_print(file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Check if the DataFrame is empty
    if df.empty:
        print(f"Error: The Excel file at {file_path} is empty")
    else:
        # Print the data in tabular format
        print(df)

# Corrected file path with raw string
excel_file_path = r'C:\Users\akars\OneDrive\Documents\EXP5.xlsx'

# Call the function with the corrected file path
read_excel_and_print(excel_file_path)

