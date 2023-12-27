from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Radius of the Earth in kilometers (adjust as needed)
    radius = 6371.0

    # Calculate the distance
    distance = radius * c

    return distance

# Example usage
lat1, lon1 = 37.7749, -122.4194  # San Francisco, CA
lat2, lon2 = 34.0522, -118.2437  # Los Angeles, CA

lat3, lon3 = 40.7128, -74.0060  # New York City, USA
lat4, lon4 = 48.8566, 2.3522    # Paris, France
lat5, lon5 = -33.8688, 151.2093  # Sydney, Australia

# Calculate distances
distance_1_2 = haversine_distance(lat1, lon1, lat2, lon2)
distance_1_3 = haversine_distance(lat1, lon1, lat3, lon3)
distance_1_4 = haversine_distance(lat1, lon1, lat4, lon4)
distance_1_5 = haversine_distance(lat1, lon1, lat5, lon5)

# Print results
print(f"Distance between San Francisco, CA and Los Angeles, CA: {distance_1_2:.2f} kilometers")
print(f"Distance between San Francisco, CA and New York City, USA: {distance_1_3:.2f} kilometers")
print(f"Distance between San Francisco, CA and Paris, France: {distance_1_4:.2f} kilometers")
print(f"Distance between San Francisco, CA and Sydney, Australia: {distance_1_5:.2f} kilometers")
