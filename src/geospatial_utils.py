import geopandas as gpd
from shapely.geometry import Point

def convert_to_geodataframe(df, lat_col, lon_col, crs="EPSG:4326"):
    geometry = [Point(xy) for xy in zip(df[lon_col], df[lat_col])]
    return gpd.GeoDataFrame(df, geometry=geometry, crs=crs)

# Fungsi geospatial lainnya