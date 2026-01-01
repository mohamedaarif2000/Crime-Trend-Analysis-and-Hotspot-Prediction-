import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df.dropna(inplace=True)
    df["date"] = pd.to_datetime(df["date"])
    df.to_csv(output_path, index=False)
    print("Data cleaning completed.")

if __name__ == "__main__":
    clean_data("data/ingested_data.csv", "data/cleaned_data.csv")
