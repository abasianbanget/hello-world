import sys
import os

# Tambahkan path ke src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.data_processing import clean_geospatial_data, create_buffer, spatial_join
from src.data_ingestion import read_shapefile

# Test code Anda di sini