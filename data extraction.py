import yfinance as yf
import pandas as pd
import os
import kaggle

# Define the stock ticker symbol (Change this to any stock symbol you want)
ticker_symbol = "AAPL"  # Example: Apple Inc.

# Fetch data from Yahoo Finance
company = yf.Ticker(ticker_symbol)

# Fetch historical stock prices (Last 1 month)
stock_prices = company.history(period="1mo")

# Fetch financial statements
income_statement = company.financials  # Income Statement
balance_sheet = company.balance_sheet  # Balance Sheet
cash_flow = company.cashflow  # Cash Flow Statement

# Print sample outputs
print("Stock Prices:\n", stock_prices.head())
print("\nIncome Statement:\n", income_statement)
print("\nBalance Sheet:\n", balance_sheet)
print("\nCash Flow Statement:\n", cash_flow)

# Optional: Save data to CSV files
stock_prices.to_csv("./data/stock_prices.csv")
income_statement.to_csv("./data/income_statement.csv")
balance_sheet.to_csv("./data/balance_sheet.csv")
cash_flow.to_csv("./data/cash_flow.csv")


print("\nData successfully fetched and saved as CSV files!")

os.environ["KAGGLE_CONFIG_DIR"] = r"C:\Users\Satwik\.kaggle"
kaggle.api.authenticate()
kaggle.api.dataset_list()
kaggle.api.dataset_download_files('sahithii7/financial-data', path='./data', unzip=True)
dataincome_statements=pd.read_csv(r'C:\Users\Satwik\.kaggle\data\AAPL_income_statement.csv')
balance_sheets = pd.read_csv(r'C:\Users\Satwik\.kaggle\data\AAPL_balance_sheet.csv')
cash_flows = pd.read_csv(r'C:\Users\Satwik\.kaggle\data\AAPL_cashflow.csv')
companies = pd.read_csv(r'C:\Users\Satwik\.kaggle\data\AAPL_company_info.csv')
financial_stmts=pd.read_csv(r'C:\Users\Satwik\.kaggle\data\Financial Statements.csv')

print("Dataset loaded successfully!")