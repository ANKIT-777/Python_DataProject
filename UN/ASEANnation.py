import csv
import matplotlib.pyplot as plt

def extract_data(file_path, encoding):
    data = []
    with open(file_path, newline='', encoding=encoding) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)
    return data

def transform_data(data, target_year, target_countries):
    transformed_data = {}
    for row in data:
        year = int(row['Year'])
        nation = row['Region']
        population = float(row['Population'])
        if nation in target_countries and year == target_year:
            transformed_data[nation] = population
    return transformed_data

def create_bar_chart(data, x_label, y_label, title):
    countries = list(data.keys())
    population_values = list(data.values())
    plt.figure(figsize=(10, 6))
    plt.bar(countries, population_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # ETL Step 1: Extract
    source_file_path = 'UN/population-estimates_csv.csv'
    source_encoding = 'iso-8859-1'
    extracted_data = extract_data(source_file_path, source_encoding)
    
    # ETL Step 2: Transform
    asean_countries = ['Brunei', 'Cambodia', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam']
    target_year = 2014
    transformed_data = transform_data(extracted_data, target_year, asean_countries)
    
    # ETL Step 3: Load
    x_label = 'Countries'
    y_label = 'Population (millions)'
    chart_title = 'Population of ASEAN Countries in 2014'
    create_bar_chart(transformed_data, x_label, y_label, chart_title)

if __name__ == '__main__':
    main()
