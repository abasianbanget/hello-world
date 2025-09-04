import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.data_ingestion import load_config, read_shapefile, save_as_parquet
from src.data_processing import clean_geospatial_data, calculate_area, filter_by_area
from src.visualization import create_interactive_map, create_histogram, save_plotly_figure

def run_pipeline():
    print("Memulai pipeline data lahan...")
    
    # Load config
    config = load_config()
    
    # Baca data
    print("1. Membaca data...")
    gdf = read_shapefile('data/raw/sample_land_data.shp')
    
    # Bersihkan data
    print("2. Membersihkan data...")
    gdf_clean = clean_geospatial_data(gdf, config['project_settings']['default_crs'])
    
    # Proses data
    print("3. Memproses data...")
    gdf_processed = calculate_area(gdf_clean)
    gdf_processed = filter_by_area(gdf_processed, min_area=0.1)
    
    # Simpan data terproses
    print("4. Menyimpan data terproses...")
    save_as_parquet(gdf_processed, 'data/processed/land_data_processed.parquet')
    
    # Buat visualisasi
    print("5. Membuat visualisasi...")
    fig_map = create_interactive_map(gdf_processed, 'value', 'Distribusi Nilai Lahan')
    fig_hist = create_histogram(gdf_processed, 'value', 'Distribusi Nilai Lahan')
    
    # Simpan visualisasi
    save_plotly_figure(fig_map, 'outputs/maps/land_value_distribution.html')
    save_plotly_figure(fig_hist, 'outputs/reports/value_histogram.html')
    
    print("6. Pipeline selesai!")
    print(f"   - Data diproses: {len(gdf_processed)} properti")
    print(f"   - Nilai rata-rata: {gdf_processed['value'].mean():.2f}")
    print(f"   - Area rata-rata: {gdf_processed['area_hectares'].mean():.2f} hektar")
    
    return gdf_processed

if __name__ == "__main__":
    run_pipeline()