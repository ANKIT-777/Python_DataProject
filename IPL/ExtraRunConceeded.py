import csv 
import matplotlib.pyplot as plt

with open('IPL/deliveries.csv') as csvfile:
    DataSet = csv.DictReader(csvfile)
    
    Extrarun = {}
    
    for row in DataSet:
        if 577 <= int(row['match_id']) <=636:
        # Get the bowling team and extra runs for the current row
            bowling_team = row['bowling_team']
            extra_runs = int(row['extra_runs'])

            # If the team is not in the dictionary, add it and set the extra runs to 0
            if bowling_team not in Extrarun:
                Extrarun[bowling_team] = 0

            # Add the extra runs for the current row to the total for the team
            Extrarun[bowling_team] += extra_runs
            
            
            
x = list(Extrarun.values())
y = list(Extrarun.keys())

plt.plot(y,x, marker = 'o')
plt.xticks(rotation=45)
plt.show()


