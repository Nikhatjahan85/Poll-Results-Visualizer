import pandas as pd

def load_data(file_path="data/poll_data.csv"):
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    df["Tool"] = df["Tool"].str.strip().str.title()
    return df

def analyze_data(df):
    counts = df["Tool"].value_counts()
    percentages = df["Tool"].value_counts(normalize=True) * 100

    print("\n📊 Tool Counts:\n", counts)
    print("\n📊 Percentage Share:\n", percentages)

    return counts, percentages