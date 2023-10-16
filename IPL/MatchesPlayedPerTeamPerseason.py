import csv
import matplotlib.pyplot as plt
with open('IPL/matches.csv') as csvfile:
    DataSet = csv.DictReader(csvfile)

    match_played = {}

    for row in DataSet:
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


years = list(match_played.keys())
teams = list(match_played[years[0]].keys())

# Create a bar chart
fig, ax = plt.subplots(figsize=(12, 6))
bottom = [0] * len(years)

for team in teams:
    # Get the number of matches played by the team for each year
    team_values = [match_played[year].get(team, 0) for year in years]
    ax.bar(years, team_values, label=team, bottom=bottom)
    bottom = [b + v for b, v in zip(bottom, team_values)]

# Customize the plot
ax.set(xlabel='Year', ylabel='Number of Matches', title='IPL Matches Played by Team (2008-2017)')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.tight_layout()

# Display the plot
plt.show()

