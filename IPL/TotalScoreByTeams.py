import csv
import matplotlib.pyplot as plt

def extract_team_scores(file_path):
    team_scores = {}

    with open(file_path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            batting_team = row['batting_team']
            total_runs = int(row['total_runs'])

            if batting_team not in team_scores:
                team_scores[batting_team] = total_runs
            else:
                team_scores[batting_team] += total_runs

    # Combine the scores of 'Rising Pune Supergiant' and 'Rising Pune Supergiants'
    team_scores['Rising Pune Supergiant'] += team_scores.get('Rising Pune Supergiants', 0)
    del team_scores['Rising Pune Supergiants']

    return team_scores

def load_team_scores(team_scores):
    teams = list(team_scores.keys())
    runs = list(team_scores.values())
    
    # Define colors for the bar chart
    colors = ['Red', 'Green', 'Blue', 'Orange', 'Purple', 'Pink', 'Brown', 'Gray', 'Yellow', 'Black', 'Indigo', 'Teal', 'Cyan']

    plt.bar(teams, runs, color=colors)
    plt.xlabel('Teams')
    plt.ylabel('Total Runs')
    plt.title('Total Runs Scored by IPL Teams')
    plt.xticks(rotation=45)
    plt.show()

def main():
    file_path = 'IPL/deliveries.csv'
    team_scores = extract_team_scores(file_path)
    load_team_scores(team_scores)

if __name__ == '__main__':
    main()
