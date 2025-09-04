#!/usr/bin/env python3
"""
Script to create a Jupyter notebook for exploratory data analysis
"""

import nbformat as nbf
import os
from pathlib import Path

def create_exploration_notebook():
    """Create an exploration notebook for land case simulation"""
    
    # Get the current directory and project root
    current_dir = Path(__file__).parent
    project_root = current_dir.parent
    notebooks_dir = project_root / "notebooks"
    
    # Create notebooks directory if it doesn't exist
    notebooks_dir.mkdir(exist_ok=True)
    
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    cells = [
        nbf.v4.new_markdown_cell("""# Exploratory Data Analysis - Land Case Simulation

This notebook explores the land data for our simulation project."""),
        
        nbf.v4.new_code_cell("""# Import necessary libraries
import sys
import os
sys.path.append('../src')

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from data_ingestion import load_config, read_shapefile
from data_processing import clean_geospatial_data
from visualization import create_interactive_map

print("Libraries imported successfully!")"""),
        
        nbf.v4.new_code_cell("""# Load configuration and data
config = load_config()
print("Configuration loaded:", config)

# Read the shapefile
gdf = read_shapefile('../data/raw/sample_land_data.shp')
print(f"Data loaded with {len(gdf)} records")

# Clean the data
gdf_clean = clean_geospatial_data(gdf, config['project_settings']['default_crs'])
print("Data cleaned successfully")"""),
        
        nbf.v4.new_code_cell("""# Explore the data
print("Data columns:", gdf_clean.columns.tolist())
print("\\nData info:")
print(gdf_clean.info())
print("\\nFirst 5 rows:")
print(gdf_clean.head())

# Basic statistics
print("\\nValue statistics:")
print(gdf_clean['value'].describe())"""),
        
        nbf.v4.new_code_cell("""# Create visualizations
# Histogram of values
plt.figure(figsize=(10, 6))
plt.hist(gdf_clean['value'], bins=20, edgecolor='black')
plt.title('Distribution of Land Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Interactive map
fig = create_interactive_map(gdf_clean, 'value', 'Land Value Distribution')
fig.show()""")
    ]
    
    # Add all cells to the notebook
    nb.cells = cells
    
    # Save the notebook
    notebook_path = notebooks_dir / "exploration.ipynb"
    
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    
    print(f"Notebook created successfully at {notebook_path}")
    
    # Verify the file was created
    if notebook_path.exists():
        print("File verification: SUCCESS")
    else:
        print("File verification: FAILED")

if __name__ == "__main__":
    create_exploration_notebook()