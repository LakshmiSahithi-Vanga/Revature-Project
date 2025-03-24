# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import mysql.connector

# # Load CSV Data
# def load_data():
#     df = pd.read_csv("final_financial_data.csv")
#     return df

# # Fetch Data from MySQL (Optional)
# def fetch_data_from_mysql():
#     connection = mysql.connector.connect(
#         host="127.0.0.1", user="root", password="Sahithi@123", database="financial_reporting"
#     )
#     query = "SELECT * FROM financial_data"  # Replace with your table
#     df = pd.read_sql(query, connection)
#     connection.close()
#     return df

# # Streamlit App
# st.title("📊 Financial Data Dashboard")

# # Load Data
# data_source = st.sidebar.radio("Select Data Source", ["CSV", "MySQL"])
# if data_source == "CSV":
#     df = load_data()
# else:
#     df = fetch_data_from_mysql()

# # Sidebar Filters
# company_list = df["company"].unique()
# selected_company = st.sidebar.selectbox("Select Company", company_list)
# year_list = sorted(df["year"].unique(), reverse=True)
# selected_year = st.sidebar.selectbox("Select Year", year_list)

# # Filtered Data
# df_filtered = df[(df["company"] == selected_company) & (df["year"] == selected_year)]

# # Display Financial Summary
# st.subheader(f"Financial Summary for {selected_company} in {selected_year}")
# st.dataframe(df_filtered)

# # Financial Metrics Comparison
# metrics = ["revenue", "net income_x", "ebitda_x", "earning per share", "roe"]
# selected_metric = st.sidebar.selectbox("Select Metric", metrics)

# st.subheader(f"{selected_metric} Over Time")
# fig, ax = plt.subplots(figsize=(10, 5))
# sns.lineplot(data=df[df["company"] == selected_company], x="year", y=selected_metric, marker='o', ax=ax)
# plt.xlabel("Year")
# plt.ylabel(selected_metric)
# plt.title(f"{selected_company} {selected_metric} Trend")
# st.pyplot(fig)

# st.write("Developed Sahithi")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

# Load CSV Data
def load_data():
    df = pd.read_csv("final_financial_data.csv")  
    return df

# Fetch Data from MySQL (Join Fact and Dimension Table)
def fetch_data_from_mysql():
    connection = mysql.connector.connect(
        host="127.0.0.1", user="root", password="Sahithi@123", database="financial_reporting"
    )
    
    # SQL query to join fact and dimension tables
    query = """
    SELECT f.*, d.company, y.year
    FROM financial_data f
    JOIN company_dim d ON f.company_id = d.company_id
    JOIN year_dim y ON f.year_id = y.year_id
    """
    
    df = pd.read_sql(query, connection)
      # Print columns to check the result
    connection.close()
    return df

# Streamlit App
st.title("📊 Financial Data Dashboard")

# Load Data
data_source = st.sidebar.radio("Select Data Source", ["CSV", "MySQL"])
if data_source == "CSV":
    df = load_data()
else:
    df = fetch_data_from_mysql()

# Check if the 'company' column exists
if 'company' not in df.columns:
    st.error("'company' column not found in the data. Please check the column names.")
else:
    # Sidebar Filters
    company_list = df["company"].unique()
    selected_company = st.sidebar.selectbox("Select Company", company_list)
    
    # Check if the 'year' column exists after joining tables
    if 'year' not in df.columns:
        st.error("'year' column not found. Please check your SQL query and column names.")
    else:
        year_list = sorted(df["year"].unique(), reverse=True)
        selected_year = st.sidebar.selectbox("Select Year", year_list)

        # Filtered Data
        df_filtered = df[(df["company"] == selected_company) & (df["year"] == selected_year)]

        # Display Financial Summary
        st.subheader(f"Financial Summary for {selected_company} in {selected_year}")
        st.dataframe(df_filtered)

        # Metrics selection based on the data source
        if data_source == "CSV":
            metrics = ["revenue", "net income_x", "ebitda_x", "earning per share", "roe"]  # Keep 'roe' and 'eps' for CSV
        else:
            metrics = ["revenue", "net income_x", "ebitda_x", "total expenses", "net profit margin"]  # Replace 'roe' and 'eps' with 'total expenses' and 'net profit margin' for MySQL

        selected_metric = st.sidebar.selectbox("Select Metric", metrics)

        st.subheader(f"{selected_metric} Over Time")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.lineplot(data=df[df["company"] == selected_company], x="year", y=selected_metric, marker='o', ax=ax)
        plt.xlabel("Year")
        plt.ylabel(selected_metric)
        plt.title(f"{selected_company} {selected_metric} Trend")
        st.pyplot(fig)

st.write("Developed by Sahithi")







# import streamlit as st
# import yfinance as yf
# import pandas as pd

# # Function to fetch financial data
# def fetch_financial_data(ticker, period="1y"):
#     try:
#         company = yf.Ticker(ticker)
#         return {
#             "Stock Prices": company.history(period=period),
#             "Income Statement": company.financials,
#             "Balance Sheet": company.balance_sheet,
#             "Cash Flow Statement": company.cashflow,
#         }
#     except Exception as e:
#         st.error(f"Error fetching data: {e}")
#         return None

# # Function to calculate financial ratios
# def calculate_financial_ratios(balance_sheet, income_statement):
#     ratios = {}
#     try:
#         ratios["Current Ratio"] = balance_sheet.loc["Total Current Assets"].iloc[0] / balance_sheet.loc["Total Current Liabilities"].iloc[0]
#         ratios["Debt-to-Equity Ratio"] = balance_sheet.loc["Total Liabilities"].iloc[0] / balance_sheet.loc["Total Stockholder Equity"].iloc[0]
#         ratios["Net Profit Margin"] = income_statement.loc["Net Income"].iloc[0] / income_statement.loc["Total Revenue"].iloc[0]
#     except Exception as e:
#         st.warning("Some financial ratios could not be calculated due to missing data.")
#     return ratios

# # Streamlit app layout
# def main():
#     st.title("📊 Financial Statement Generator")
    
#     # User input for company ticker and period
#     ticker = st.text_input("Enter Stock Ticker Symbol (e.g., AAPL, TSLA, MSFT)", "AAPL")
#     period = st.selectbox("Select Period", ["1mo", "3mo", "6mo", "1y", "2y"])
    
#     statement_type = st.selectbox("Select Financial Statement", ["Stock Prices", "Income Statement", "Balance Sheet", "Cash Flow Statement"])
    
#     if st.button("Generate Report"):
#         data = fetch_financial_data(ticker, period)
        
#         if data is not None and statement_type in data:
#             st.subheader(statement_type)
#             st.dataframe(data[statement_type])
            
#             if statement_type == "Stock Prices":
#                 st.line_chart(data[statement_type]["Close"])
            
#             if statement_type in ["Income Statement", "Balance Sheet"]:
#                 ratios = calculate_financial_ratios(data["Balance Sheet"], data["Income Statement"])
#                 st.subheader("📈 Key Financial Ratios")
#                 for key, value in ratios.items():
#                     st.write(f"*{key}:* {value:.2f}")
                
#             # Export functionality
#             csv = data[statement_type].to_csv()
#             st.download_button(
#                 label=f"📥 Download {statement_type} as CSV",
#                 data=csv,
#                 file_name=f"{statement_type.lower().replace(' ', '_')}.csv",
#                 mime='text/csv',
#             )
#         else:
#             st.error("Unable to fetch or display the selected data.")

# if __name__ == "__main__":
#     main()


