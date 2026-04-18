import pandas as pd

def preprocess_data(df):
    print("🔄 Preprocessing started...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Standardize text
    df["Tool"] = df["Tool"].str.strip().str.title()
    df["Gender"] = df["Gender"].str.strip().str.title()

    # Convert data types
    df["Satisfaction"] = pd.to_numeric(df["Satisfaction"], errors="coerce")

    # Final clean
    df = df.dropna()

    print("✅ Preprocessing done!")

    return df