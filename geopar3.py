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

def calculate_gas_amount(distance, fuel_efficiency, gas_price):
    # Assuming fuel_efficiency is in km/l and gas_price is in currency per liter
    gas_amount = distance / fuel_efficiency
    cost = gas_amount * gas_price
    return gas_amount, cost

# Example usage
lat1, lon1 = 37.7749, -122.4194  # San Francisco, CA
lat2, lon2 = 34.0522, -118.2437  # Los Angeles, CA

lat3, lon3 = 40.7128, -74.0060  # New York City, USA
lat4, lon4 = 48.8566, 2.3522    # Paris, France
lat5, lon5 = -33.8688, 151.2093  # Sydney, Australia

# Assume a fuel efficiency of 10 km/l and gas price of $1.50 per liter
fuel_efficiency = 10.0  # km per liter
gas_price = 4.50  # dollars per liter

# Calculate distances
distance_1_2 = haversine_distance(lat1, lon1, lat2, lon2)
distance_1_3 = haversine_distance(lat1, lon1, lat3, lon3)
distance_1_4 = haversine_distance(lat1, lon1, lat4, lon4)
distance_1_5 = haversine_distance(lat1, lon1, lat5, lon5)

# Calculate gas amounts and costs
gas_amount_1_2, cost_1_2 = calculate_gas_amount(distance_1_2, fuel_efficiency, gas_price)
gas_amount_1_3, cost_1_3 = calculate_gas_amount(distance_1_3, fuel_efficiency, gas_price)
gas_amount_1_4, cost_1_4 = calculate_gas_amount(distance_1_4, fuel_efficiency, gas_price)
gas_amount_1_5, cost_1_5 = calculate_gas_amount(distance_1_5, fuel_efficiency, gas_price)

# Print results
print(f"Gas amount from San Francisco, CA to Los Angeles, CA: {gas_amount_1_2:.2f} liters, Cost: ${cost_1_2:.2f}")
print(f"Gas amount from San Francisco, CA to New York City, USA: {gas_amount_1_3:.2f} liters, Cost: ${cost_1_3:.2f}")
print(f"Gas amount from San Francisco, CA to Paris, France: {gas_amount_1_4:.2f} liters, Cost: ${cost_1_4:.2f}")
print(f"Gas amount from San Francisco, CA to Sydney, Australia: {gas_amount_1_5:.2f} liters, Cost: ${cost_1_5:.2f}")
