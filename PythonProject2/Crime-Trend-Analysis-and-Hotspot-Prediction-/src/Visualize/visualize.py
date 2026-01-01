import pandas as pd
import folium
from folium.plugins import HeatMap


def generate_crime_heatmap(csv_pat"C:\Users\Mohamedaarif\Downloads\archive.zip", output_name="crime_hotspots.html"):

    df = pd.read_csv("C:\Users\Mohamedaarif\Downloads\archive.zip")

    df = df.dropna(subset=['Latitude', 'Longitude'])

    map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
    crime_map = folium.Map(location=map_center, zoom_start=12, tiles='CartoDB positron')

    heat_data = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]

    HeatMap(heat_data, radius=15, blur=10, max_zoom=1).add_to(crime_map)

    crime_map.save(output_name)
    print(f"✅ Success! Heatmap saved as {output_name}")

