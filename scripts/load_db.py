import pandas as pd
import os
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

processed_folder = "data/processed"

for file in os.listdir(processed_folder):

    if file.endswith(".csv"):

        table_name = file.replace(".csv", "").lower()

        print(f"Loading {file} -> {table_name}")

        df = pd.read_csv(f"{processed_folder}/{file}")

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

print("Database loaded successfully!")