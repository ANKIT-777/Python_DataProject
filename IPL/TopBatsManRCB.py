import csv
import matplotlib.pyplot as plt


def extract_rcb_batters(file_path):

    rcb_batters = {}

    with open(file_path, newline='') as csvfile:
        dataset = csv.DictReader(csvfile)

        for row in dataset:
            if row['batting_team'] == 'Royal Challengers Bangalore' and row['batsman'] not in rcb_batters:
                rcb_batters[row['batsman']] = int(row['batsman_runs'])
            elif row['batting_team'] == 'Royal Challengers Bangalore':
                rcb_batters[row['batsman']] = rcb_batters[row['batsman']] + int(row['batsman_runs'])

    return rcb_batters


def transform_rcb_batters(rcb_batters):

    rcb_batters_list = []
    for batter, runs in rcb_batters.items():
        rcb_batters_list.append((batter, runs))

    return rcb_batters_list


def load_top_rcb_batters(rcb_batters_list):
    rcb_batters_list.sort(key=lambda item: item[1], reverse=True)

    # Unpack the sorted data into separate lists for plotting
    y = [item[1] for item in rcb_batters_list[:10]]  # Batsman names on the y-axis
    x = [item[0] for item in rcb_batters_list[:10]]  # Runs scored on the x-axis

    # Plotting
    plt.bar(x, y)  # Use barh for horizontal bar chart
    plt.xlabel('Runs Scored')
    plt.ylabel('Batsmen')
    plt.title('Top 10 RCB Batsmen by Runs Scored')
    plt.show()


def main():
    # Extract the RCB batters and their runs scored
    rcb_batters = extract_rcb_batters('IPL/deliveries.csv')

    # Transform the RCB batters dictionary
    rcb_batters_list = transform_rcb_batters(rcb_batters)

    # Plot the top 10 RCB batters by runs scored
    load_top_rcb_batters(rcb_batters_list)


if __name__ == '__main__':
    main()
