import os
import numpy as np
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon

def create_sample_data():
    """Create sample geospatial data for testing"""
    # Create directories if they don't exist
    os.makedirs('data/raw', exist_ok=True)
    
    # Create sample point data
    np.random.seed(42)
    n_points = 100
    
    # Generate random points around a center
    center_lat, center_lon = -6.2, 106.8  # Jakarta coordinates
    points = []
    values = []
    
    for i in range(n_points):
        lat = center_lat + np.random.normal(0, 0.05)
        lon = center_lon + np.random.normal(0, 0.05)
        points.append(Point(lon, lat))
        values.append(np.random.uniform(100000, 5000000))  # Random property values
    
    # Create GeoDataFrame
    gdf = gpd.GeoDataFrame({
        'id': range(n_points),
        'value': values,
        'geometry': points
    })
    
    # Set CRS
    gdf.crs = 'EPSG:4326'
    
    # Save as shapefile
    gdf.to_file('data/raw/sample_land_data.shp')
    print(f"Created sample data with {n_points} points")
    
    # Also save as CSV for reference
    csv_data = pd.DataFrame({
        'id': range(n_points),
        'value': values,
        'longitude': [point.x for point in points],
        'latitude': [point.y for point in points]
    })
    csv_data.to_csv('data/raw/sample_land_data.csv', index=False)
    print("Sample data saved to data/raw/")

if __name__ == "__main__":
    create_sample_data()