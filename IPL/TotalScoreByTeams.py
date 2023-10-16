import csv
import matplotlib.pyplot as plt

# Define the file path - update this to the correct location of your CSV file
file_path = r'/Users/ankitsharma/Desktop/Python/IPL/deliveries.csv'

# Create an empty dictionary to store the total runs for each team
team_scores = {}

# Open the CSV file and read its contents
with open(file_path, newline='') as csvfile:
    dataset = csv.DictReader(csvfile)
    for row in dataset:
        # Extract the batting team and total runs from each row
        batting_team = row['batting_team']
        total_runs = int(row['total_runs'])
        
        # Update the team's total runs in the dictionary
        if batting_team not in team_scores:
            team_scores[batting_team] = total_runs
        else:
            team_scores[batting_team] += total_runs

# Combine the scores of 'Rising Pune Supergiant' and 'Rising Pune Supergiants'
team_scores['Rising Pune Supergiant'] += team_scores.get('Rising Pune Supergiants', 0)
del team_scores['Rising Pune Supergiants']

# Define a list of team names and corresponding colors for the bar chart
teams = ['SRH', 'RCB', 'MI', 'RPS', 'GL', 'KKR', 'KXIP', 'DD', 'CSK', 'RR', 'DC', 'KTK', 'PW']
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink', 'Brown', 'Gray', 'Black', 'Indigo', 'Teal', 'Cyan']

# Create a bar chart to visualize the total runs for each team
plt.bar(teams, team_scores.values(), color=colors)
plt.xlabel('Teams')
plt.ylabel('Total Runs')
plt.title('Total Runs Scored by IPL Teams')
plt.xticks(rotation=45)
plt.show()
