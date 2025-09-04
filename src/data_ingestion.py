import yaml
import os
import geopandas as gpd
import pandas as pd

def load_config(config_path='config/config.yaml'):
    """
    Load configuration from YAML file
    
    Parameters:
    config_path (str): Path to the configuration file
    
    Returns:
    dict: Configuration data
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(f"Error loading configuration: {e}")
        # Return default config if file not found
        return {
            'project_settings': {
                'default_crs': 'EPSG:4326'
            }
        }

def read_shapefile(file_path):
    """
    Read a shapefile using GeoPandas
    
    Parameters:
    file_path (str): Path to the shapefile
    
    Returns:
    geopandas.GeoDataFrame: Data from the shapefile
    """
    try:
        gdf = gpd.read_file(file_path)
        print(f"Successfully read shapefile: {file_path}")
        return gdf
    except Exception as e:
        print(f"Error reading shapefile: {e}")
        return None

def read_csv_with_pandas(file_path):
    """
    Read CSV file using pandas
    
    Parameters:
    file_path (str): Path to the CSV file
    
    Returns:
    pandas.DataFrame: Data from CSV file
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully read CSV file: {file_path}")
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None