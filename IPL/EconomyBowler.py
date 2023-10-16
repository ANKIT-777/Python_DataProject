import csv
import matplotlib.pyplot as plt
# Define the file path - update this to the correct location of your CSV file
file_path = r'/Users/ankitsharma/Desktop/Python/IPL/deliveries.csv'

with open(file_path, newline='') as csvfile:
    dataset = csv.DictReader(csvfile)
    
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




for bowler in bowlers_overs:
    total_deliveries = bowlers_overs[bowler]
    overs = total_deliveries // 6  # Calculate the number of complete overs
    balls = total_deliveries % 6  # Calculate the remaining balls
    overs += balls / 10  # Convert remaining balls to overs (1 ball = 0.1 overs)
    bowlers_overs[bowler] = overs
    
    


Economy = {}

for bowler in bowlers_data:
    if bowler in bowlers_overs:
        econ = float(bowlers_data[bowler] / bowlers_overs[bowler])
        Economy[bowler] = econ

    
sorted_bowlers = dict(sorted(Economy.items(), key=lambda item: item[1]))

# Get the top N bowlers and their economy values
top_N = 10
y = list(sorted_bowlers.values())[:top_N]  # Economy values on the y-axis
x = list(sorted_bowlers.keys())[:top_N][::-1]   
# Plotting

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


