import geopandas as gpd
from shapely.geometry import Point, LineString
import matplotlib.pyplot as plt

# Create a GeoDataFrame for road segments
roads_data = {
    'road_id': [1, 2, 3],
    'geometry': [LineString([(0, 0), (2, 2)]), LineString([(1, 1), (3, 3)]), LineString([(2, 2), (4, 4)])]
}
roads_gdf = gpd.GeoDataFrame(roads_data, crs="epsg:4326")

# Create a GeoDataFrame for points of interest (POIs)
pois_data = {
    'poi_id': [101, 102, 103],
    'geometry': [Point(1, 1), Point(3, 3), Point(5, 5)]
}
pois_gdf = gpd.GeoDataFrame(pois_data, crs="epsg:4326")

# Plot the road network and POIs
fig, ax = plt.subplots()
roads_gdf.plot(ax=ax, color='gray', label='Roads')
pois_gdf.plot(ax=ax, color='red', marker='o', label='POIs')

# Find the nearest POI for each road segment
nearest_pois = gpd.tools.sjoin_nearest(roads_gdf, pois_gdf, distance_col="nearest_distance", lsuffix="left", rsuffix="right")

# Print the result
print(nearest_pois[['road_id', 'poi_id', 'nearest_distance']])

# Display the plot
plt.legend()
plt.show()
