# Import necessary libraries
import csv
import matplotlib.pyplot as plt

# Open the CSV file 'population-estimates_csv.csv' with specified encoding
with open('UN/population-estimates_csv.csv', newline='', encoding='iso-8859-1') as csvfile:
    # Create a dictionary reader for the CSV file
    DataSet = csv.DictReader(csvfile)

    # Define a list of ASEAN countries
    Asean = ['Brunei', 'Cambodia', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam']
    
    # Create an empty dictionary to store population data for ASEAN countries in 2014
    Population_ASEAN = {}
    
    # Iterate through each row in the CSV file
    for row in DataSet:
        # Extract the year from the 'Year' column and convert it to an integer
        year = int(row['Year'])
        
        # Extract the nation (country) from the 'Region' column
        nation = row['Region']
        
        # Extract the population from the 'Population' column and convert it to a float
        numbers = float(row['Population'])
        
        # Check if the nation is in the ASEAN list and the year is 2014
        if nation in Asean and year == 2014:
            # If the conditions are met, store the population data in the Population_ASEAN dictionary
            Population_ASEAN[nation] = numbers

# Create a bar chart using the data from the Population_ASEAN dictionary
plt.bar(list(Population_ASEAN.keys()), list(Population_ASEAN.values()))

# Display the bar chart
plt.show()
