import csv
import matplotlib.pyplot as plt

file_path = 'Maharastra /Maharashtra.csv'

with open(file_path, newline='', encoding='iso-8859-1') as csvfile:
    Dataset = csv.DictReader(csvfile)

    Histogram = {'<= 1L': 0, '1L to 10L': 0, '10L to 1Cr': 0, '1Cr to 10Cr': 0, '> 10Cr': 0}

    for row in Dataset:
        val = float(row['AUTHORIZED_CAP'])
        if val <= 100000:
            Histogram['<= 1L'] += 1
        elif 100000 < val <= 1000000:
            Histogram['1L to 10L'] += 1
        elif 1000000 < val <= 10000000:
            Histogram['10L to 1Cr'] += 1
        elif 10000000 < val <= 100000000:
            Histogram['1Cr to 10Cr'] += 1
        else:
            Histogram['> 10Cr'] += 1

y_labels = list(Histogram.keys())
data = list(Histogram.values())

bin = len(y_labels)

plt.hist(y_labels,bins=bin,weights=data,edgecolor= 'red',color='skyblue')
plt.show()

