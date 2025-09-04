#!/usr/bin/env python3
"""
Main script for running land case simulation analysis
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from data_ingestion import load_config, read_shapefile
from data_processing import clean_geospatial_data
from visualization import create_interactive_map, save_plotly_figure

def main():
    print("Starting land case simulation analysis...")
    
    # Load configuration
    config = load_config()
    print("Configuration loaded")
    
    # Read data
    print("Reading data...")
    try:
        gdf = read_shapefile('data/raw/sample_land_data.shp')
        if gdf is None:
            print("Error: Failed to read data. Please run 'python scripts/create_sample_data.py' first.")
            return
        print(f"Read {len(gdf)} records")
    except Exception as e:
        print(f"Error reading data: {e}")
        print("Please run 'python scripts/create_sample_data.py' first to create sample data.")
        return
    
    # Process data
    print("Processing data...")
    try:
        gdf_clean = clean_geospatial_data(gdf, config['project_settings']['default_crs'])
        print("Data cleaned successfully")
    except Exception as e:
        print(f"Error processing data: {e}")
        return
    
    # Create visualization
    print("Creating visualization...")
    try:
        fig = create_interactive_map(
            gdf_clean, 
            'value', 
            'Sample Land Value Distribution'
        )
        
        # Save visualization
        os.makedirs('outputs/maps', exist_ok=True)
        save_plotly_figure(fig, 'outputs/maps/land_value_map.html')
        print("Map saved to outputs/maps/land_value_map.html")
        
        print("Analysis completed successfully!")
    except Exception as e:
        print(f"Error creating visualization: {e}")

if __name__ == "__main__":
    main()