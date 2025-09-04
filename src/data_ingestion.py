# File: src/data_ingestion.py
import pandas as pd
import geopandas as gpd
import pyarrow as pa
import pyarrow.parquet as pq
import os
import yaml
from dotenv import load_dotenv

load_dotenv()

def load_config():
    with open('config/config.yaml', 'r') as f:
        return yaml.safe_load(f)

def read_csv_with_pandas(file_path):
    """Membaca file CSV menggunakan pandas"""
    return pd.read_csv(file_path)

def read_shapefile(file_path):
    """Membaca shapefile menggunakan geopandas"""
    return gpd.read_file(file_path)

def save_as_parquet(df, file_path):
    """Menyimpan DataFrame sebagai file Parquet"""
    table = pa.Table.from_pandas(df)
    pq.write_table(table, file_path)

def load_parquet(file_path):
    """Memuat file Parquet sebagai pandas DataFrame"""
    table = pq.read_table(file_path)
    return table.to_pandas()