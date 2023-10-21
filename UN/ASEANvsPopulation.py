import csv
import matplotlib.pyplot as plt

def extract_data(file_path, encoding):
    data = {}
    with open(file_path, newline='', encoding=encoding) as csvfile:
        DataSet = csv.DictReader(csvfile)
        for row in DataSet:
            nation = row['Region']
            population = float(row['Population'])
            year = row['Year']
            
            if year not in data:
                data[year] = {}
            
            if nation in Asean:
                if nation not in data[year]:
                    data[year][nation] = 0
                data[year][nation] += population
    
    return data

def filter_data(data, start_year, end_year):
    return {year: data[year] for year in data if start_year <= int(year) <= end_year}

def create_grouped_bar_chart(data, x_label, y_label, title):
    years = list(data.keys())
    nations = Asean
    populations = {nation: [data[year][nation] if nation in data[year] else 0 for year in years] for nation in nations}
    
    plt.figure(figsize=(25, 6))
    width = 0.10
    x = range(len(years))
    
    for i, nation in enumerate(nations):
        plt.bar([pos + i * width for pos in x], populations[nation], width=width, label=nation)
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks([pos + 2.5 * width for pos in x], years)
    plt.legend(loc='upper right', title='Nations')
    
    plt.show()

def main():
    source_file_path = 'UN/population-estimates_csv.csv'
    source_encoding = 'iso-8859-1'
    
    data = extract_data(source_file_path, source_encoding)
    
    start_year = 2004
    end_year = 2014
    filtered_data = filter_data(data, start_year, end_year)
    
    x_label = 'Year'
    y_label = 'Population'
    title = 'Population of ASEAN Nations from {} to {}'.format(start_year, end_year)
    create_grouped_bar_chart(filtered_data, x_label, y_label, title)

if __name__ == '__main__':
    Asean = ['Brunei', 'Cambodia', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam']
    main()
