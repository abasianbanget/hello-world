# File: scripts/run_analysis.py
import sys
sys.path.append('../src')

from data_ingestion import load_config, read_csv_with_pandas, read_shapefile
from data_processing import clean_geospatial_data
from visualization import create_interactive_map, save_plotly_figure

def main():
    print("Memulai analisis data lahan...")
    
    # Load konfigurasi
    config = load_config()
    
    # Baca data
    print("Membaca data...")
    # gdf = read_shapefile('../data/raw/sample_data.shp')
    
    # Proses data
    print("Memproses data...")
    # gdf_clean = clean_geospatial_data(gdf, config['project_settings']['default_crs'])
    
    # Visualisasi
    print("Membuat visualisasi...")
    # fig = create_interactive_map(gdf_clean, 'value', 'Peta Sample Data Lahan')
    # save_plotly_figure(fig, '../outputs/maps/sample_map.html')
    
    print("Analisis selesai!")

if __name__ == "__main__":
    main()