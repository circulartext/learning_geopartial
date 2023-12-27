Geospatial Fleet Travel Analysis
This Python script leverages geospatial calculations to simulate a year's worth of travel for a fleet of airplanes between various locations. The key functionalities include:

Haversine Distance Calculation:

The haversine_distance function computes the great-circle distance between two geographical points using their latitude and longitude coordinates.
Fuel Consumption and Cost Estimation:

The calculate_gas_amount function determines the fuel amount and cost based on the distance traveled, airplane fuel efficiency, and a predefined gas price.
Data Representation:

The fleet's data and locations are represented as Pandas DataFrames (fleet_df and locations_df), containing information such as airplane ID, fuel efficiency, location name, latitude, and longitude.
Simulation Loop:

The script simulates a year's worth of travel, iterating over each airplane and location combination to calculate gas consumption and costs.
Results Analysis:

The results are aggregated and analyzed, showcasing the total cost for each location and each airplane. Additionally, the total cost for the entire fleet in a day is calculated.
Results Export:

The final results are saved to a CSV file named fleet_travel_results.csv for further analysis and reference.
Instructions:
Ensure you have the required dependencies (math, geopandas, pandas) installed.
Adjust the fleet and location data as needed.
Run the script to perform the geospatial fleet travel analysis.
Feel free to explore the results, including the total costs per location, per airplane, and for the entire fleet.
