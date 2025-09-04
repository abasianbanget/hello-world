# File: scripts/create_sample_data.py
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import numpy as np
import os

# Buat direktori jika belum ada
os.makedirs('../data/raw', exist_ok=True)

# Buat data sample
np.random.seed(42)
n_points = 100

# Generate random points around a center (contoh: Jakarta)
lat_center, lon_center = -6.2, 106.8
lat_points = np.random.normal(lat_center, 0.1, n_points)
lon_points = np.random.normal(lon_center, 0.1, n_points)

# Create DataFrame
df = pd.DataFrame({
    'id': range(n_points),
    'latitude': lat_points,
    'longitude': lon_points,
    'value': np.random.randint(10, 100, n_points)
})

# Convert to GeoDataFrame
geometry = [Point(xy) for xy in zip(df.longitude, df.latitude)]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

# Save sample data
df.to_csv('../data/raw/sample_data.csv', index=False)
gdf.to_file('../data/raw/sample_data.shp')

print("Sample data created and saved to data/raw/")