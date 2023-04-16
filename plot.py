
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# Import the shapefile of the geographic distribution of the Egyptian fruit bat
fruit_bat_map = gpd.read_file('data_0.shp')

# Import the CSV file containing the Marburg data
marburg_data = pd.read_csv('CDC_marburg_data.csv')

marburg_data['cases'] = pd.to_numeric(marburg_data['cases'], errors='coerce')

marburg_data = gpd.GeoDataFrame(
    marburg_data, geometry=gpd.points_from_xy(marburg_data.longitude, marburg_data.latitude), crs='EPSG:4326'
)

# Import the shapefile of the world map
world_map = gpd.read_file('world-administrative-boundaries.shp')

fig, ax = plt.subplots(figsize=(12, 8))


world_map.plot(color='lightblue', edgecolor='white', ax=ax)
fruit_bat_map.plot(color='green', edgecolor='darkgreen', ax=ax, )
marburg_data.plot(ax=ax, color='red', markersize=marburg_data['cases'],)


# formatting and legends
plt.title('Geographic Distribution of the Egyptian Fruit Bat and Marburg Virus Outbreaks')


# Plot the Egyptian fruit bat distribution with a custom green handle
fruit_bat_handle = Line2D([0], [0], marker='o', color='w', label='Egyptian Fruit Bat Distribution',
                          markerfacecolor='green', markersize=10)
fruit_bat_map.plot(color='green', edgecolor='darkgreen', ax=ax)

# Plot the Marburg cases with a custom red handle
marburg_handle = Line2D([0], [0], marker='o', color='w', label='Marburg Virus Cases',
                        markerfacecolor='red', markersize=10)
marburg_data.plot(ax=ax, color='red', markersize=marburg_data['cases'])

# Add the legend with custom handles and labels
legend_handles = [fruit_bat_handle, marburg_handle]
legend_labels = [h.get_label() for h in legend_handles]

legend = ax.legend(handles=legend_handles, labels=legend_labels, loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=True, fontsize='x-large')


# display plot
plt.show()

