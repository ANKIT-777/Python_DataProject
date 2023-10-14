# Import necessary libraries
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Define the file path for the CSV data
file_path = 'Maharastra /Maharashtra.csv'

# Open the CSV file with specified encoding
with open(file_path, newline='', encoding='iso-8859-1') as csvfile:
    Dataset = csv.DictReader(csvfile)

    # Create a dictionary to store the count of companies registered by year
    Company = {}

    # Iterate through each row in the dataset
    for row in Dataset:
        # Extract the date of registration
        date = row['DATE_OF_REGISTRATION']

        try:
            # Parse the date into a datetime object
            date_obj = datetime.strptime(date, "%d-%m-%y")
            year = date_obj.year
            
            # If the year is greater than 2025, subtract 100 to account for two-digit year representation
            if year > 2025:
                year = year - 100
        except ValueError:
            # Handle parsing errors in case the date is not in the expected format
            pass
        
        # Check if the year is in the Company dictionary
        if year not in Company: 
            Company[year] = 1
        else:
            # If the year already exists in the dictionary, increment the count
            Company[year] += 1

# Sort the dictionary by year
sorted_dict = dict(sorted(Company.items()))

# Create a bar chart using the sorted data
plt.bar(sorted_dict.keys(), sorted_dict.values())

# Display the bar chart
plt.show()
