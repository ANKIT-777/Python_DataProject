import csv
import matplotlib.pyplot as plt


def plot_extra_runs(file_path):
    extra_runs = {}

    with open(file_path, newline='') as csvfile:
        dataset = csv.DictReader(csvfile)

        for row in dataset:
            if 577 <= int(row['match_id']) <= 636:
                bowling_team = row['bowling_team']
                extra_runs[bowling_team] = extra_runs.get(bowling_team, 0) + int(row['extra_runs'])

    x, y = extra_runs.keys(), extra_runs.values()

    plt.plot(x, y, marker='o')
    plt.xticks(rotation=45)
    plt.xlabel('Bowling Team')
    plt.ylabel('Extra Runs')
    plt.title('Extra Runs per Bowling Team in IPL 2023')
    plt.show()


if __name__ == '__main__':
    plot_extra_runs('IPL/deliveries.csv')
