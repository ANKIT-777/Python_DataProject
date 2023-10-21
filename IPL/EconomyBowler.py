import csv
import matplotlib.pyplot as plt


def extract(file_path):
    with open(file_path, newline='') as csvfile:
        dataset = csv.DictReader(csvfile)
        return dataset


def transform(dataset):
    bowlers_data = {}
    bowlers_overs = {}

    for row in dataset:
        if 1 <= int(row['match_id']) <= 59:
            bowler = row['bowler']
            total_runs = int(row['total_runs'])

            # Check if the delivery is a valid delivery (not a no-ball or wide)
            if bowler not in bowlers_data:
                bowlers_data[bowler] = total_runs
                bowlers_overs[bowler] = 1
            else:
                bowlers_data[bowler] += total_runs
                bowlers_overs[bowler] += 1

    # Calculate the economy rate for each bowler
    for bowler in bowlers_data:
        bowlers_overs[bowler] = bowlers_overs[bowler] // 6 + bowlers_overs[bowler] % 6 / 10
        bowlers_data[bowler] = bowlers_data[bowler] / bowlers_overs[bowler]

    return bowlers_data, bowlers_overs


def load(bowlers_data, bowlers_overs):
    # Sort the bowlers data by economy rate
    sorted_bowlers = dict(sorted(bowlers_data.items(), key=lambda item: item[1]))
    # Get the top N bowlers and their economy values
    top_N = 10
    y = list(sorted_bowlers.values())[:top_N]  # Economy values on the y-axis
    x = list(sorted_bowlers.keys())[:top_N][::-1]      # Bowlers on the x-axis

    return x, y


def main():
    # Get the file path from the usera
    file_path = 'IPL/deliveries.csv'

    # Use a context manager to ensure that the dataset object is closed properly
    with open(file_path, newline='') as csvfile:
        dataset = csv.DictReader(csvfile)

        # Transform the data
        bowlers_data, bowlers_overs = transform(dataset)

        # Load the data
        x, y = load(bowlers_data, bowlers_overs)

    # Plot the top N bowlers by economy rate
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.barh(x, y, color='skyblue')
    plt.xlabel('Economy Rate')
    plt.ylabel('Bowler')
    plt.title('Top 10 Bowlers by Economy Rate')
    plt.gca().invert_yaxis()  # Invert the y-axis to show the best economy at the top

    # Display the economy rate on the bars
    for i, v in enumerate(y):
        plt.text(v, i, f'{v:.1f}', color='black', va='center')

    plt.show()


if __name__ == '__main__':
    main()
