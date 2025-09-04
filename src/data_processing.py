# File: src/data_processing.py
import pandas as pd
import geopandas as gpd
import numpy as np
from shapely.geometry import Point, Polygon

def clean_geospatial_data(gdf, crs=None):
    """Membersihkan data geospatial"""
    if crs:
        gdf = gdf.to_crs(crs)
    
    # Hapus geometri yang tidak valid
    gdf = gdf[gdf.is_valid]
    
    return gdf

def create_buffer(gdf, distance):
    """Membuat buffer sekitar geometri"""
    return gdf.buffer(distance)

def spatial_join(gdf1, gdf2, how='inner'):
    """Melakukan spatial join antara dua GeoDataFrame"""
    return gpd.sjoin(gdf1, gdf2, how=how)