import pandas as pd
from sklearn.cluster import KMeans

def train_model("C:\Users\Mohamedaarif\OneDrive\Crime Dataset New .csv"):
    df = pd.read_csv("C:\Users\Mohamedaarif\OneDrive\Crime Dataset New .csv")
    coords = df[["latitude", "longitude"]]
    model = KMeans(n_clusters=2, random_state=42)
    df["hotspot"] = model.fit_predict(coords)
    df.to_csv("data/predictions.csv", index=False)
    print("Model training completed.")

if __name__ == "__main__":
    train_model("data/features.csv")
