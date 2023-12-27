import math
from math import radians, sin, cos, sqrt, atan2
import geopandas as gpd
import pandas as pd

def haversine_distance(lat1, lon1, lat2, lon2):
    radius = 6371.0  # Earth's radius in kilometers
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = radius * c
    return distance

def calculate_gas_amount(distance, fuel_efficiency, gas_price):
    gas_amount = distance / fuel_efficiency
    cost = gas_amount * gas_price
    return gas_amount, cost

fleet_data = {
    'airplane_id': [1, 2, 3, 4, 5, 6],
    'fuel_efficiency': [8.0, 10.0, 12.0, 18.0, 20.0, 22.0],
}
fleet_df = pd.DataFrame(fleet_data)

locations_data = {
    'location_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'location_name': [
        'San Francisco', 'Los Angeles', 'New York', 'Paris', 'Sydney',
        'Tokyo', 'Rio de Janeiro', 'Berlin', 'Cape Town', 'Vancouver'
    ],
    'latitude': [
        37.7749, 34.0522, 40.7128, 48.8566, -33.8688,
        35.6895, -22.9068, 52.5200, -33.9180, 49.2827
    ],
    'longitude': [
        -122.4194, -118.2437, -74.0060, 2.3522, 151.2093,
        139.6917, -43.1729, 13.4050, 18.4233, -123.1207
    ],
}
locations_df = pd.DataFrame(locations_data)

gas_price = 5.50

results_data = {'airplane_id': [], 'location_id': [], 'location_name': [], 'gas_amount': [], 'cost': []}
results_df = pd.DataFrame(results_data)

for day in range(3):  # Simulate a year's worth of travel
    for _, airplane_row in fleet_df.iterrows():
        for _, location_row in locations_df.iterrows():
            distance = haversine_distance(
                location_row['latitude'], location_row['longitude'],
                locations_df.iloc[0]['latitude'], locations_df.iloc[0]['longitude']
            )

            gas_amount, cost = calculate_gas_amount(
                distance, airplane_row['fuel_efficiency'], gas_price
            )

            new_row = pd.DataFrame({
                'airplane_id': [airplane_row['airplane_id']],
                'location_id': [location_row['location_id']],
                'location_name': [location_row['location_name']],
                'gas_amount': [gas_amount],
                'cost': [cost],
            })
            results_df = pd.concat([results_df, new_row], ignore_index=True)

print(results_df)

total_cost_per_location = results_df.groupby(['location_id', 'location_name'])['cost'].sum()
print("Total cost for each location:")
print(total_cost_per_location)

total_cost_per_airplane = results_df.groupby('airplane_id')['cost'].sum()
print("Total cost for each airplane:")
print(total_cost_per_airplane)

total_cost_for_fleet = results_df.groupby('airplane_id')['cost'].sum().sum()
print(f"Total cost for the entire fleet in a day: ${total_cost_for_fleet:.2f}")

# Save the results to a CSV file
results_df.to_csv('fleet_travel_results.csv', index=False)
print("Results saved to fleet_travel_results.csv")
