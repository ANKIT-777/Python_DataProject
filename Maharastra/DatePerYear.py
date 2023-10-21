import csv
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

file_path = 'Maharastra /Maharashtra.csv'


# Use a defaultdict for storing registration counts per year
Company = defaultdict(int)

with open(file_path, newline='', encoding='iso-8859-1') as csvfile:
    Dataset = csv.DictReader(csvfile)

    for row in Dataset:
        date = row['DATE_OF_REGISTRATION']

        try:
            date_obj = datetime.strptime(date, "%d-%m-%y")
            year = date_obj.year
            if year >= 2025:  # Subtract 100 for years greater than or equal to 2025
                year -= 100
        except ValueError:
            pass

        Company[year] += 1

# Sort the dictionary by year
sorted_dict = dict(sorted(Company.items()))

# Plotting the data
plt.bar(sorted_dict.keys(), sorted_dict.values())
plt.xlabel('Year')
plt.ylabel('Number of Registrations')
plt.title('Company Registrations in Maharashtra by Year')
plt.show()
