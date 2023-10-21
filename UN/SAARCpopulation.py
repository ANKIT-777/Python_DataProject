import csv
import matplotlib.pyplot as plt

def extract_saarc_population_data(file_path, encoding):
    saarc_population_data = {}
    with open(file_path, newline='', encoding=encoding) as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            nation = row['Region']
            year = row['Year']
            population = float(row['Population'])
            
            if year not in saarc_population_data:
                saarc_population_data[year] = 0
            
            if nation in SAARC:
                saarc_population_data[year] += population
    return saarc_population_data

def create_saarc_population_bar_chart(data, x_label, y_label, title):
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
    source_encoding = 'iso-8859-1'
    
    saarc_population_data = extract_saarc_population_data(source_file_path, source_encoding)
    
    x_label = 'Years'
    y_label = 'Population in numbers'
    title = 'SAARC COUNTRIES Population Over Years'
    
    create_saarc_population_bar_chart(saarc_population_data, x_label, y_label, title)

if __name__ == '__main__':
    SAARC = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']
    main()
