# Import necessary libraries
import csv
import matplotlib.pyplot as plt

# Open the CSV file 'population-estimates_csv.csv' with specified encoding
with open('UN/population-estimates_csv.csv', newline='', encoding='iso-8859-1') as csvfile:
    Datasheet = csv.DictReader(csvfile)

    # Define a list of SAARC countries
    SAARC = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']

    # Create an empty dictionary to store population data for SAARC countries
    SAARC_population = {}

    # Iterate through each row in the CSV file
    for row in Datasheet:
        nation = row['Region']
        year = row['Year']
        population = float(row['Population'])  # Corrected typo here

        # Check if the year is not in SAARC_population dictionary
        if year not in SAARC_population:
            SAARC_population[year] = 0  # Initialize the population for the year

        # Check if the nation is in the SAARC list
        if nation in SAARC:
            # If the nation is in SAARC, add the population to the respective year
            SAARC_population[year] += population

# Create a bar chart using the data from the SAARC_population dictionary
plt.bar(list(SAARC_population.keys()), list(SAARC_population.values()))

# Display the bar chart
plt.show()
