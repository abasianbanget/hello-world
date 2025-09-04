import sys
import os

# Tambahkan path ke src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from data_ingestion import load_config, read_csv_with_pandas, read_shapefile

# Load config
config = load_config()
print("Configuration loaded successfully")

# Test reading CSV
try:
    df = read_csv_with_pandas('../data/raw/sample_land_data.csv')
    print("CSV reading test: PASSED")
    print(f"Data shape: {df.shape}")
except Exception as e:
    print(f"CSV reading test: FAILED - {e}")

# Test reading shapefile
try:
    gdf = read_shapefile('../data/raw/sample_land_data.shp')
    print("Shapefile reading test: PASSED")
    print(f"Data shape: {gdf.shape}")
except Exception as e:
    print(f"Shapefile reading test: FAILED - {e}")