import csv 
import matplotlib.pyplot as plt

with open('IPL/deliveries.csv', newline='') as csvfile:
    DataSet = csv.DictReader(csvfile)

    RCB_batters = {}

    for x in DataSet: 
        if x['batting_team'] == 'Royal Challengers Bangalore' and x['batsman'] not in RCB_batters:
            RCB_batters[x['batsman']] = int(x['batsman_runs'])
        elif x['batting_team'] == 'Royal Challengers Bangalore':
            RCB_batters[x['batsman']] = RCB_batters[x['batsman']] + int(x['batsman_runs'])

Top_batters = sorted(RCB_batters.items(), key=lambda item: item[1], reverse=True)

# Unpack the sorted data into separate lists for plotting
y = [item[1] for item in Top_batters[:10]]  # Batsman names on the y-axis
x = [item[0] for item in Top_batters[:10]]  # Runs scored on the x-axis

# Plotting
plt.barh(x, y)  # Use barh for horizontal bar chart
plt.xlabel('Runs Scored')
plt.ylabel('Batsmen')
plt.title('Top 10 RCB Batsmen by Runs Scored')
plt.show()
