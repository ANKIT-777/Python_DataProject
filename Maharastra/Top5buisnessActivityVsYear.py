import csv
import matplotlib.pyplot as plt

with open('Maharastra /Maharashtra.csv', newline='', encoding='iso-8859-1') as csvfile:
    Dataset = csv.DictReader(csvfile)
    Activities = {}
    for row in Dataset:
        date = row['DATE_OF_REGISTRATION'][-2:]
        activity = row['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']

        # Check if date is 'NA' and skip this row
        if date == 'NA':
            continue

        if int(date) > 21:
            newdate = '19' + date
        else:
            newdate = '20' + date

        if 2000 <= int(newdate) <= 2010:
            if newdate not in Activities:
                Activities[newdate] = {}

            if activity not in Activities[newdate]:
                Activities[newdate][activity] = 1
            else:
                Activities[newdate][activity] += 1

sorted_data = {date: dict(sorted(data.items(), key=lambda item: item[1], reverse=True)) for date, data in Activities.items()}

years = list(sorted_data.keys())
activity_year = list(sorted_data.values())
top_activity_year = {}

for year_index, year_activities in enumerate(activity_year):
    top_activities = list(year_activities)[:5]
    if years[year_index] not in top_activity_year:
        top_activity_year[years[year_index]] = top_activities

# Prepare data for the grouped bar chart
all_activity_names = set()
for year in top_activity_year:
    for activity in top_activity_year[year]:
        all_activity_names.add(activity)

all_activity_names = sorted(all_activity_names)

bar_data = {}
for activity in all_activity_names:
    bar_data[activity] = []
    for year in top_activity_year:
        if activity in top_activity_year[year]:
            bar_data[activity].append(activity_year[years.index(year)][activity])
        else:
            bar_data[activity].append(0)

# Set the bar positions
x = list(range(len(top_activity_year)))

# Create a bar for each activity
width = 0.10
fig, ax = plt.subplots()

for i, activity in enumerate(bar_data):
    ax.bar([pos + width * i for pos in x], bar_data[activity], width=width, label=activity)

# Set the labels and title of the chart
ax.set_xticks([pos + width * 2 for pos in x])
ax.set_xticklabels(top_activity_year.keys())
ax.set_ylabel("Number of Companies")
ax.set_title("Top 5 Activities in Maharashtra by Number of Companies (2000-2010)")

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1, 1))

# Show the chart
plt.show()
