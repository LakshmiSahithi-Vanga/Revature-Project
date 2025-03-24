
import pandas as pd
import numpy as np

def clean_data(file_path, output_path):
    """
    Clean financial data by handling missing values, identifying outliers, and standardizing formats.
    :param file_path: Path to input CSV file
    :param output_path: Path to save cleaned CSV file
    """
    try:
        # Load data
        data = pd.read_csv(file_path)

        # Handle missing values
        data.fillna(0, inplace=True)  # Replace NaN with 0
        print("Missing values handled.")

        # Standardize column names
        data.columns = [col.strip().replace(" ", "_").lower() for col in data.columns]
        print("Column names standardized.")

        # Remove duplicate rows
        data.drop_duplicates(inplace=True)
        print("Duplicate rows removed.")

        # Identify outliers (example: Revenue outliers beyond 1.5*IQR)
        if 'revenue' in data.columns:
            Q1 = data['revenue'].quantile(0.25)
            Q3 = data['revenue'].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            data = data[(data['revenue'] >= lower_bound) & (data['revenue'] <= upper_bound)]
            print("Outliers in revenue removed.")

        # Ensure numeric columns are correctly formatted
        numeric_columns = ['revenue', 'net_income', 'total_assets', 'market_cap']
        for col in numeric_columns:
            if col in data.columns:
                data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0)
        print("Numeric columns formatted.")

        # Save cleaned data
        data.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
    
    except Exception as e:
        print(f"Error during data cleaning: {e}")

# Example usage
if __name__ == "__main__":
    clean_data("./data/income_statement.csv", "./cleaned_data/cleaned_income_statement.csv")
    clean_data("./data/balance_sheet.csv", "./cleaned_data/cleaned_balance_sheet.csv")
    clean_data("./data/cash_flow.csv", "./cleaned_data/cleaned_cash_flow.csv")
    clean_data("./data/AAPL_balance_sheet.csv", "./cleaned_data/cleaned_AAPL_balance_sheet.csv")
    clean_data("./data/AAPL_cashflow.csv", "./cleaned_data/cleaned_AAPL_cashflow.csv")
    clean_data("./data/AAPL_company_info.csv", "./cleaned_data/cleaned_AAPL_company_info.csv")
    clean_data("./data/AAPL_dividends.csv", "./cleaned_data/cleaned_AAPL_dividends.csv")
    clean_data("./data/AAPL_historical_data.csv", "./cleaned_data/cleaned_AAPL_historical_data.csv")
    clean_data("./data/AAPL_income_statements.csv", "./cleaned_data/cleaned_AAPL_income_statements.csv")
    clean_data("./data/stock_prices.csv", "./cleaned_data/cleaned_stock_prices.csv")
    clean_data("./data/Financial Statements.csv", "./cleaned_data/cleaned_Financial Statements.csv")