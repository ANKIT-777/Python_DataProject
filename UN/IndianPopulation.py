import csv
import matplotlib.pyplot as plt

def extract_population_data(file_path, target_country):
    population_data = {}
    with open(file_path, newline='', encoding='iso-8859-1') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            year = int(row['Year'])
            country = row['Region']
            population = float(row['Population'])
            if country == target_country:
                population_data[year] = population
    return population_data

def create_population_bar_chart(data, country, x_label, y_label, title):
    years = list(data.keys())
    populations = list(data.values())
    
    plt.bar(years, populations)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)
    plt.show()

def main():
    source_file_path = 'UN/population-estimates_csv.csv'
    target_country = 'India'
    
    population_data = extract_population_data(source_file_path, target_country)
    
    x_label = 'Years'
    y_label = 'Population in numbers'
    title = f'{target_country} Population vs Years'
    
    create_population_bar_chart(population_data, target_country, x_label, y_label, title)

if __name__ == '__main__':
    main()
