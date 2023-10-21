import csv
import matplotlib.pyplot as plt

def load_data(file_path):
    histogram = {'<= 1L': 0, '1L to 10L': 0, '10L to 1Cr': 0, '1Cr to 10Cr': 0, '> 10Cr': 0}

    with open(file_path, newline='', encoding='iso-8859-1') as csvfile:
        data_reader = csv.DictReader(csvfile)

        for row in data_reader:
            val = float(row['AUTHORIZED_CAP'])
            if val <= 100000:
                histogram['<= 1L'] += 1
            elif 100000 < val <= 1000000:
                histogram['1L to 10L'] += 1
            elif 1000000 < val <= 10000000:
                histogram['10L to 1Cr'] += 1
            elif 10000000 < val <= 100000000:
                histogram['1Cr to 10Cr'] += 1
            else:
                histogram['> 10Cr'] += 1

    return histogram

def plot_histogram(histogram_data):
    categories = list(histogram_data.keys())
    counts = list(histogram_data.values())

    num_categories = len(categories)
    plt.bar(categories, counts, color='skyblue', edgecolor='red')
    plt.xlabel('Authorized Capital Ranges')
    plt.ylabel('Company Counts')
    plt.title('Company Counts by Authorized Capital Range')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.show()

if __name__ == '__main__':
    file_path = 'Maharastra /Maharashtra.csv'
    histogram_data = load_data(file_path)
    plot_histogram(histogram_data)
