import csv
import matplotlib.pyplot as plt

def load_data(filename):
    data = {}
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            season = row['season']
            winner = row['winner']
            if season not in data:
                data[season] = {}
            if winner not in data[season]:
                data[season][winner] = 1
            else:
                data[season][winner] += 1
    return data

def prepare_data(data):
    sorted_data = dict(sorted(data.items(), key=lambda x: x[0]))
    teams = list(set(winner for season_data in sorted_data.values() for winner in season_data.keys()))
    team_wins = {team: [year_data.get(team, 0) for year_data in sorted_data.values()] for team in teams}
    return teams, team_wins

def plot_bar_chart(teams, team_wins):
    positions = [str(year) for year in range(2008, 2018)]
    color_codes = [
        "#3366FF", "#FFFF33", "#FF5733", "#33FF57", "#FF33FF", "#33FFFF", "#FF9933", "#9933FF",
        "#33FF99", "#FF33CC", "#33CCFF", "#FFCC33", "#33FFCC", "#CC33FF", "#33CC99"
    ]
    plt.figure(figsize=(10, 5))
    bottom = [0] * len(positions)
    for i, team in enumerate(teams):
        plt.bar(positions, team_wins[team], color=color_codes[i], label=team, bottom=bottom)
        bottom = [bottom[j] + team_wins[team][j] for j in range(len(positions))]
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlabel('Season')
    plt.ylabel('Wins')
    plt.title('IPL Team Wins Over Seasons')
    plt.show()

if __name__ == '__main__':
    data = load_data('IPL/matches.csv')
    teams, team_wins = prepare_data(data)
    plot_bar_chart(teams, team_wins)
