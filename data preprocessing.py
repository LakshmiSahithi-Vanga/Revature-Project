import pandas as pd

def fix_transposed_data(file_path, output_path):
    # Load dataset
    data = pd.read_csv(file_path)

    # Check if the first column contains financial metrics
    if 'unnamed:_0' in data.columns:
        data.set_index('unnamed:_0', inplace=True)  # Set first column as index
        data = data.transpose().reset_index()  # Transpose and reset index
        data.rename(columns={'index': 'date'}, inplace=True)  # Rename the index column

    # Standardize column names
    data.columns = [col.strip().lower().replace(" ", "_") for col in data.columns]

    # Print to verify new structure
    print("✅ Transformed Data Columns:", data.columns.tolist())
    print(data.head())

    # Save transformed dataset
    data.to_csv(output_path, index=False)
    print(f"✅ Fixed transposed data saved to {output_path}")

# Example usage
fix_transposed_data("./cleaned_data/cleaned_income_statement.csv", "./fixed_data/fixed_income_statement.csv")
fix_transposed_data("./cleaned_data/cleaned_cash_flow.csv", "./fixed_data/fixed_cash_flow.csv")
fix_transposed_data("./cleaned_data/cleaned_balance_sheet.csv", "./fixed_data/fixed_balance_sheet.csv")
fix_transposed_data("./cleaned_data/cleaned_stock_prices.csv", "./fixed_data/fixed_stock_prices.csv")