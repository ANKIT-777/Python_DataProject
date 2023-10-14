# Import necessary libraries
import csv
import matplotlib.pyplot as plt

# Define the file path for the CSV data
file_path = 'Maharastra /Maharashtra.csv'

# Open the CSV file with specified encoding
with open(file_path, newline='', encoding='iso-8859-1') as csvfile:
    Dataset = csv.DictReader(csvfile)

    # Create a histogram dictionary to categorize and count authorized capital ranges
    Histogram = {'<= 1L': 0, '1L to 10L': 0, '10L to 1Cr': 0, '1Cr to 10Cr': 0, '> 10Cr': 0}

    # Iterate through each row in the dataset
    for row in Dataset:
        val = float(row['AUTHORIZED_CAP'])
        
        # Categorize the authorized capital and increment the corresponding category count
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

# Extract labels and data for the histogram
y_labels = list(Histogram.keys())
data = list(Histogram.values())

# Set the number of bins for the histogram
bin = len(y_labels)

# Create the histogram plot
plt.hist(y_labels, bins=bin, weights=data, edgecolor='red', color='skyblue')

# Display the histogram
plt.show()
