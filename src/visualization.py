import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
import pandas as pd
import os

def create_interactive_map(gdf, color_column, title):
    """
    Create an interactive map using Plotly.
    
    Parameters:
    gdf (geopandas.GeoDataFrame): Input GeoDataFrame
    color_column (str): Column name to use for coloring
    title (str): Title of the map
    
    Returns:
    plotly.graph_objects.Figure: Interactive map figure
    """
    # Buat salinan dataframe untuk menghindari modifikasi original
    df_for_plot = gdf.copy()
    
    # Ekstrak koordinat dari geometri
    df_for_plot['longitude'] = df_for_plot.geometry.x
    df_for_plot['latitude'] = df_for_plot.geometry.y
    
    # Konversi ke DataFrame biasa (bukan GeoDataFrame)
    plot_df = pd.DataFrame(df_for_plot.drop(columns='geometry'))
    
    # Buat plot menggunakan DataFrame biasa
    fig = px.scatter_mapbox(
        plot_df,
        lat='latitude',
        lon='longitude',
        color=color_column,
        size_max=15,
        zoom=10,
        title=title,
        hover_data=plot_df.columns.tolist()
    )
    
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
    
    return fig

def save_plotly_figure(fig, file_path):
    """
    Save a Plotly figure to an HTML file.
    
    Parameters:
    fig (plotly.graph_objects.Figure): Figure to save
    file_path (str): Path to save the file
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Save the figure
    fig.write_html(file_path)
    print(f"Figure saved to {file_path}")

def create_static_map(gdf, value_column, title):
    """
    Create a static map using matplotlib as fallback
    
    Parameters:
    gdf (geopandas.GeoDataFrame): Input GeoDataFrame
    value_column (str): Column name with values
    title (str): Title of the map
    
    Returns:
    matplotlib.figure.Figure: Static map figure
    """
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(figsize=(10, 8))
    gdf.plot(column=value_column, ax=ax, legend=True, 
             cmap='viridis', markersize=50, alpha=0.7)
    ax.set_title(title)
    
    return fig