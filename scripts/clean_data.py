import pandas as pd
import os

input_folder = "data/raw"
output_folder = "data/processed"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):

    if file.endswith(".csv"):

        print(f"Cleaning {file}...")

        df = pd.read_csv(f"{input_folder}/{file}")

        # Convert date
        df["date"] = pd.to_datetime(df["date"])

        # Sort by date
        df = df.sort_values("date")

        # Remove duplicates
        df = df.drop_duplicates()

        # Remove invalid NAV values
        df = df[df["nav"] > 0]

        # Save cleaned file
        output_file = f"{output_folder}/{file}"
        df.to_csv(output_file, index=False)

        print(f"Saved -> {output_file}")

print("All files cleaned successfully!")