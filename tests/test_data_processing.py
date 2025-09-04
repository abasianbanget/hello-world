# File: tests/test_data_processing.py
import unittest
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from data_processing import clean_geospatial_data, create_buffer

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        # Setup data uji
        self.points = [Point(0, 0), Point(1, 1), Point(2, 2)]
        self.gdf = gpd.GeoDataFrame({
            'id': [1, 2, 3],
            'value': [10, 20, 30]
        }, geometry=self.points, crs='EPSG:4326')
    
    def test_clean_geospatial_data(self):
        result = clean_geospatial_data(self.gdf, 'EPSG:4326')
        self.assertEqual(len(result), 3)
    
    def test_create_buffer(self):
        buffered = create_buffer(self.gdf, 0.1)
        self.assertEqual(len(buffered), 3)

if __name__ == '__main__':
    unittest.main()