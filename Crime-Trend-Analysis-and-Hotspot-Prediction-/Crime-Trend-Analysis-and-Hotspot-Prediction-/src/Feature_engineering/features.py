import pandas as pd

def create_features(input_path, output_path):
    df = pd.read_csv(input_path)
    df["day"] = pd.to_datetime(df["date"]).dt.day
    df["month"] = pd.to_datetime(df["date"]).dt.month
    df.to_csv(output_path, index=False)
    print("Feature engineering completed.")

if __name__ == "__main__":
    create_features("data/cleaned_data.csv", "data/features.csv")
