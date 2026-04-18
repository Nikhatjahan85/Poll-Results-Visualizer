import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visuals(df, counts):
    os.makedirs("outputs", exist_ok=True)

    # -----------------------------
    # Bar Chart
    # -----------------------------
    plt.figure()
    sns.countplot(x="Tool", data=df)
    plt.title("Tool Preference")
    plt.savefig("outputs/bar_chart.png")
    plt.close()

    # -----------------------------
    # Pie Chart
    # -----------------------------
    plt.figure()
    counts.plot.pie(autopct='%1.1f%%')
    plt.title("Tool Share")
    plt.ylabel("")
    plt.savefig("outputs/pie_chart.png")
    plt.close()

    # -----------------------------
    # Histogram (FIXED)
    # -----------------------------
    plt.figure()
    sns.histplot(df["Satisfaction"], bins=5, kde=True)
    plt.title("Satisfaction Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.savefig("outputs/histogram.png")
    plt.close()

    print("✅ All charts (Bar, Pie, Histogram) saved in outputs/")