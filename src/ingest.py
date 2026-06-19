import duckdb
import pandas as pd
from dotenv import load_dotenv
from fredapi import Fred
import os

load_dotenv()

fred = Fred(api_key=os.getenv("FRED_API_KEY"))

#pull weekly mortgage rate from FRED, manipulate df, and save to raw data folder
mortgage_rate = fred.get_series("MORTGAGE30US", observation_start = "2024-01-01", observation_end = "2024-12-31")
mortgage_df = pd.DataFrame(mortgage_rate)
mortgage_df = mortgage_df.reset_index()
mortgage_df.columns = ["date", "mortgage_rate_30yr"]
mortgage_df['year'] = 2024
mortgage_df.to_csv("data/raw/fred_mortgage_rate_2024.csv", index = False)

#pull monthly unemployment rate from FRED, manipulate df, and save to raw data folder
unemp_rate = fred.get_series("UNRATE", observation_start = "2024-01-01", observation_end = "2024-12-31")
unemp_df = pd.DataFrame(unemp_rate)
unemp_df = unemp_df.reset_index()
unemp_df.columns = ["date", "unemployment_rate",]
unemp_df['year'] = 2024
unemp_df.to_csv("data/raw/fred_unemployment_rate_2024.csv", index = False)

#pull monthly HPI from Fred, manipulate df, and save to raw data folder
hpi = fred.get_series("CSUSHPISA", observation_start = "2024-01-01", observation_end = "2024-12-31")
hpi_df = pd.DataFrame(hpi)
hpi_df = hpi_df.reset_index()
hpi_df.columns = ["date", "housing_price_index"]
hpi_df['year'] = 2024
hpi_df.to_csv("data/raw/fred_hpi_rate_2024.csv", index = False)

#setting up duckdb connections
con = duckdb.connect("data/hmda.duckdb")
con.execute("""
            CREATE TABLE IF NOT EXISTS hmda_raw AS
            SELECT * FROM read_csv_auto("data/raw/hmda_nc_va_2024.csv")
            """
)
row_count = con.execute("SELECT COUNT(*) FROM hmda_raw").fetchone()[0]
print(f"There are {row_count} rows in the hmda_raw table.")
con.close()

print("Ingest Complete!")

