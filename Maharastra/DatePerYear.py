import csv
from datetime import datetime
import matplotlib.pyplot as plt

file_path = 'Maharastra /Maharashtra.csv'

with open(file_path, newline='', encoding='iso-8859-1') as csvfile:
    Dataset = csv.DictReader(csvfile)

    Company = {}

    for row in Dataset:
        
        date = row['DATE_OF_REGISTRATION']

        try:
            date_obj = datetime.strptime(date, "%d-%m-%y")
            year = date_obj.year
            if year >2025:
                year = year - 100
        except ValueError:
            pass
        
        if year not in Company: 
            Company[year] = 1
        else:
            Company[year] += 1
            
            
           


sorted_dict = dict(sorted(Company.items()))

plt.bar(sorted_dict.keys(),sorted_dict.values())
plt.show()

