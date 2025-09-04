import geopandas as gpd
import pandas as pd
from shapely.geometry import shape

def clean_geospatial_data(gdf, target_crs):
    """
    Clean geospatial data by handling missing values, invalid geometries,
    and reprojecting to the target CRS.
    
    Parameters:
    gdf (geopandas.GeoDataFrame): Input GeoDataFrame
    target_crs (str): Target CRS (e.g., 'EPSG:4326')
    
    Returns:
    geopandas.GeoDataFrame: Cleaned GeoDataFrame
    """
    # Make a copy to avoid modifying the original
    cleaned_gdf = gdf.copy()
    
    # Handle missing values in geometry
    cleaned_gdf = cleaned_gdf.dropna(subset=['geometry'])
    
    # Remove invalid geometries
    cleaned_gdf = cleaned_gdf[cleaned_gdf.is_valid]
    
    # Reproject to target CRS if needed
    if cleaned_gdf.crs is not None and str(cleaned_gdf.crs) != target_crs:
        cleaned_gdf = cleaned_gdf.to_crs(target_crs)
    elif cleaned_gdf.crs is None:
        cleaned_gdf.set_crs(target_crs, inplace=True)
    
    # Reset index
    cleaned_gdf.reset_index(drop=True, inplace=True)
    
    print(f"Cleaned data: {len(cleaned_gdf)} records")
    return cleaned_gdf

def create_buffer(gdf, distance):
    """
    Create a buffer around geometries.
    
    Parameters:
    gdf (geopandas.GeoDataFrame): Input GeoDataFrame
    distance (float): Buffer distance in meters
    
    Returns:
    geopandas.GeoDataFrame: Buffered GeoDataFrame
    """
    buffered_gdf = gdf.copy()
    buffered_gdf['geometry'] = buffered_gdf.buffer(distance)
    return buffered_gdf

def spatial_join(gdf1, gdf2, how='inner', predicate='intersects'):
    """
    Perform a spatial join between two GeoDataFrames.
    
    Parameters:
    gdf1 (geopandas.GeoDataFrame): Left GeoDataFrame
    gdf2 (geopandas.GeoDataFrame): Right GeoDataFrame
    how (str): Type of join ('left', 'right', 'inner')
    predicate (str): Spatial predicate ('intersects', 'contains', etc.)
    
    Returns:
    geopandas.GeoDataFrame: Joined GeoDataFrame
    """
    return gpd.sjoin(gdf1, gdf2, how=how, predicate=predicate)