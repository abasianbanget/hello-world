# File: src/visualization.py
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import geopandas as gpd

def create_interactive_map(gdf, color_column, title="Peta Interaktif"):
    """Membuat peta interaktif menggunakan Plotly"""
    fig = px.choropleth_mapbox(
        gdf,
        geojson=gdf.geometry,
        locations=gdf.index,
        color=color_column,
        color_continuous_scale="Viridis",
        range_color=(gdf[color_column].min(), gdf[color_column].max()),
        mapbox_style="carto-positron",
        zoom=10,
        center={"lat": gdf.geometry.centroid.y.mean(), 
                "lon": gdf.geometry.centroid.x.mean()},
        opacity=0.5,
        title=title
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

def save_plotly_figure(fig, file_path):
    """Menyimpan figur Plotly sebagai HTML"""
    fig.write_html(file_path)