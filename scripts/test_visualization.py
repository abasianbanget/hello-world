import sys
import os

# Tambahkan path ke src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.visualization import create_interactive_map, save_plotly_figure
from src.data_ingestion import read_shapefile

# Test code Anda di sini