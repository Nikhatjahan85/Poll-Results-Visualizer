import pandas as pd
import numpy as np
import os

def generate_data(file_path="data/poll_data.csv"):
    os.makedirs("data", exist_ok=True)

    data = {
        "Age": np.random.choice(["18-24", "25-34", "35-44"], 200),
        "Gender": np.random.choice(["Male", "Female"], 200),
        "Tool": np.random.choice(
            ["Python", "Excel", "R"],
            200,
            p=[0.5, 0.3, 0.2]   # realistic distribution
        ),
        "Satisfaction": np.random.randint(1, 6, 200)
    }

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

    print("✅ Synthetic poll data generated!")

if __name__ == "__main__":
    generate_data()