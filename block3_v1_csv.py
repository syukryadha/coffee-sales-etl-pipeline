import pandas as pd
file_path = r"C:\Users\Putri Nuzul\Hello World\sales.csv"


def run_pipeline(file):
    df = pd.read_csv(file)
    df = df.dropna()
    df = df.drop_duplicates()
    df = df[df["quantity"] > 0]
    print(f"Rows after cleaning: {len(df)}")
    df.to_csv("clean_sales.csv", index=False)


run_pipeline(file_path)


def run_pipeline2(file):
    df = pd.read_csv(file)
    df = df.dropna()
    df = df.drop_duplicates()
    df = df[df["quantity"] > 0]
    print(f"Rows after cleaning: {len(df)}")
    df.to_csv("clean_file2.csv", index=False)


run_pipeline2(file_path)
