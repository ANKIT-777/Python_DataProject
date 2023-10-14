# Import necessary libraries
import csv
import matplotlib.pyplot as plt

# Open the CSV file 'population-estimates_csv.csv' with specified encoding
with open('UN/population-estimates_csv.csv', newline='', encoding='iso-8859-1') as csvfile:
    # Create a dictionary reader for the CSV file
    DataSet = csv.DictReader(csvfile)

    # Create an empty dictionary to store population data for India
    Population = {}

    # Iterate through each row in the CSV file
    for row in DataSet:
        # Extract the year from the 'Year' column and convert it to an integer
        year = int(row['Year'])
        
        # Extract the population from the 'Population' column and convert it to a float
        Pop_year = float(row['Population'])
        
        # Check if the 'Region' column value is 'India'
        if row['Region'] == 'India':
            # If it's India, store the population data in the Population dictionary
            Population[year] = int(Pop_year)
        else:
            # If it's not India, skip to the next row
            pass

# Create a bar chart using the data from the Population dictionary
plt.bar(list(Population.keys()), list(Population.values()))

# Display the bar chart
plt.show()
