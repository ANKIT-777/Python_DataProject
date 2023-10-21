import csv
import matplotlib.pyplot as plt

def read_match_data(file_path):
    match_played = {}
    with open(file_path, newline='') as csvfile:
        dataset = csv.DictReader(csvfile)
        for row in dataset:
            season = row['season']
            team1 = row['team1']
            team2 = row['team2']

            if season not in match_played:
                match_played[season] = {}

            if team1 not in match_played[season]:
                match_played[season][team1] = 1
            else:
                match_played[season][team1] += 1

            if team2 not in match_played[season]:
                match_played[season][team2] = 1
            else:
                match_played[season][team2] += 1

    return match_played

def plot_matches_played_by_team(match_data):
    years = list(match_data.keys())
    teams = list(match_data[years[0]].keys())

    fig, ax = plt.subplots(figsize=(12, 6))
    bottom = [0] * len(years)

    for team in teams:
        team_values = [match_data[year].get(team, 0) for year in years]
        ax.bar(years, team_values, label=team, bottom=bottom)
        bottom = [b + v for b, v in zip(bottom, team_values)]

    ax.set(xlabel='Year', ylabel='Number of Matches', title='IPL Matches Played by Team (2008-2017)')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.tight_layout()
    plt.show()

def main():
    file_path = 'IPL/matches.csv'
    match_data = read_match_data(file_path)
    plot_matches_played_by_team(match_data)

if __name__ == '__main__':
    main()
