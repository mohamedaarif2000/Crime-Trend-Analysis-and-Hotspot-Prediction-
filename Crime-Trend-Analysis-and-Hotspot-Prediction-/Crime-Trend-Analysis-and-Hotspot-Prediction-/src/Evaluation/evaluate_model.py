import pandas as pd
import matplotlib.pyplot as plt

def evaluate():
    df = pd.read_csv("data/predictions.csv")

    # Save metrics
    metrics = {
        "Total Crimes": [len(df)],
        "Hotspots Identified": [df["hotspot"].nunique()]
    }
    metrics_df = pd.DataFrame(metrics)
    metrics_df.to_csv("tables/model_metrics.csv", index=False)

    # Plot hotspots
    plt.scatter(df["longitude"], df["latitude"], c=df["hotspot"])
    plt.title("Crime Hotspot Prediction")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.savefig("figures/crime_hotspots.png")

    print("Evaluation completed.")

if __name__ == "__main__":
    evaluate()
