import csv
import matplotlib.pyplot as plt

with open('UN/population-estimates_csv.csv', newline='', encoding='iso-8859-1') as csvfile:
    DataSet = csv.DictReader(csvfile)

    Groupped = {}
    Asean = ['Brunei', 'Cambodia', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam']

    for row in DataSet:
        nation = row['Region']
        population = float(row['Population'])
        year = row['Year']

        # Check if the year exists in Groupped
        if year not in Groupped:
            Groupped[year] = {}

        # Check if the nation is in the Asean list
        if nation in Asean:
            # Initialize the population for the nation if it doesn't exist
            if nation not in Groupped[year]:
                Groupped[year][nation] = 0

            # Accumulate the population for the nation for the given year
            Groupped[year][nation] += population

# Filter the years to include only those in the range 2004-2014
years = [year for year in Groupped if 2004 <= int(year) <= 2014]
nations = Asean

populations = {nation: [Groupped[year][nation] if nation in Groupped[year] else 0 for year in years] for nation in nations}

# Create the grouped bar chart
plt.figure(figsize=(12, 6))
width = 0.15
x = range(len(years))

for i, nation in enumerate(nations):
    plt.bar([pos + i * width for pos in x], populations[nation], width=width, label=nation)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population of ASEAN Nations from 2004 to 2014')
plt.xticks([pos + 2.5 * width for pos in x], years)
plt.legend(loc='upper right', title='Nations')

plt.show()
