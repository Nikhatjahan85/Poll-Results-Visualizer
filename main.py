# main.py

from src.data_generator import generate_data
from src.analysis import load_data, analyze_data
from src.preprocessing import preprocess_data
from src.visualization import create_visuals

def main():
    print("🚀 Poll Results Visualizer Started...\n")

    # -----------------------------
    # Step 1: Generate Synthetic Data
    # -----------------------------
    print("📌 Step 1: Generating Data...")
    generate_data()

    # -----------------------------
    # Step 2: Load Data
    # -----------------------------
    print("\n📌 Step 2: Loading Data...")
    df = load_data()
    print(f"✅ Data Loaded: {df.shape[0]} rows")

    # -----------------------------
    # Step 3: Preprocessing
    # -----------------------------
    print("\n📌 Step 3: Preprocessing Data...")
    df = preprocess_data(df)
    print(f"✅ Clean Data: {df.shape[0]} rows")

    # -----------------------------
    # Step 4: Analysis
    # -----------------------------
    print("\n📌 Step 4: Analyzing Data...")
    counts, percentages = analyze_data(df)

    # -----------------------------
    # Step 5: Visualization
    # -----------------------------
    print("\n📌 Step 5: Creating Visualizations...")
    create_visuals(df, counts)
    print("✅ Charts saved in 'outputs/' folder")

    # -----------------------------
    # Step 6: Insights
    # -----------------------------
    print("\n📌 Step 6: Generating Insights...")

    top_tool = counts.idxmax()
    top_percentage = percentages.max()

    print("\n🏆 FINAL INSIGHT:")
    print(f"Most Preferred Tool: {top_tool}")
    print(f"Vote Share: {top_percentage:.2f}%")

    print("\n🎯 Project Completed Successfully!")

# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    main()