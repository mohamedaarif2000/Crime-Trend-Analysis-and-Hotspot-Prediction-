import pandas as pd

def ingest_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df.to_csv(output_path, index=False)
    print("Data ingestion completed.")

if __name__ == "__main__":
    ingest_data("data/sample/crime_sample.csv", "data/ingested_data.csv")
