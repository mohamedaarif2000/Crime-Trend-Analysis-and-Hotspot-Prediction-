import pandas as pd


def clean_crime_data(df):
    # Convert date strings to datetime objects
    df['Date'] = pd.to_datetime(df['Date'])

    # Feature Engineering: Extract time-based features
    df['Hour'] = df['Date'].dt.hour
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['Month'] = df['Date'].dt.month

    # Handle missing spatial data
    df = df.dropna(subset=['Latitude', 'Longitude'])
    return df