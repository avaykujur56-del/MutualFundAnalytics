import pandas as pd

files = [
    "HDFC_Top100.csv",
    "HDFC_Top100_NAV.csv",
    "Axis_Bluechip.csv"
]

for file in files:
    df = pd.read_csv(f"data/raw/{file}")
    print("\n", file)
    print(df.columns.tolist())