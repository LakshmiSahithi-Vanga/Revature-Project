import pandas as pd
import os

def transform_data(file_path, output_path):
    try:
        # Load data
        data = pd.read_csv(file_path)
        print(f"✅ Loaded data from {file_path}: {data.shape}")

        # Standardize column names
        data.columns = [col.strip().replace(" ", "_").lower() for col in data.columns]
        
        # Convert date columns to proper format
        if 'date' in data.columns:
            data['date'] = pd.to_datetime(data['date'], errors='coerce')
        
        # Reshape data (Convert wide format to long format)
        if any(col.startswith("20") for col in data.columns):
            data = data.melt(id_vars=[data.columns[0]], var_name="date", value_name="value")

        # Compute additional financial ratios
        if 'net_income' in data.columns and 'total_revenue' in data.columns:
            data['profit_margin'] = data['net_income'] / data['total_revenue']
        if 'total_liabilities' in data.columns and 'total_equity' in data.columns:
            data['debt_to_equity'] = data['total_liabilities'] / data['total_equity']

        # Save transformed data to the specified output path
        data.to_csv(output_path, index=False)
        print(f"✅ Transformed data saved to {output_path}")

    except Exception as e:
        print(f"❌ Error during data transformation: {e}")

# List of input files
file_paths = [
    "./cleaned_data/cleaned_income_statement.csv",
    "./cleaned_data/cleaned_balance_sheet.csv",
    "./cleaned_data/cleaned_cash_flow.csv",
    "./cleaned_data/cleaned_stock_prices.csv",
    "./cleaned_data/cleaned_AAPL_cashflow.csv",
    "./cleaned_data/cleaned_AAPL_company_info.csv",
    "./cleaned_data/cleaned_AAPL_dividends.csv",
    "./cleaned_data/cleaned_AAPL_historical_data.csv",
    "./cleaned_data/cleaned_AAPL_balance_sheet.csv"
    "./cleaned_data/cleaned_Financial Statements.csv"

]

# Ensure output directory exists
os.makedirs("./transformed_data", exist_ok=True)

# Process each file and save in the new folder
for file in file_paths:
    # Generate the output file path in the transformed_data directory
    output_file = file.replace("cleaned_data", "transformed_data")
    transform_data(file, output_file)
