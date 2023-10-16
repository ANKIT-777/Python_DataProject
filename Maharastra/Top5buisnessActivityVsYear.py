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

# Extract the top 10 activities for the first year (change this as needed)
top_activities = list(activity_year[0].keys())[:5]

# Prepare data for the plot
x = range(len(years))
width = 0.15

plt.figure(figsize=(15, 6))

for i, activity in enumerate(top_activities):
    activity_counts = [data.get(activity, 0) for data in activity_year]
    plt.bar([pos + i * width for pos in x], activity_counts, width=width, label=activity)

plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Top Business Activities in Maharashtra from 2000 to 2010')
plt.xticks([pos + width * (len(top_activities) / 2) for pos in x], years)
plt.legend(loc='best', title='Activities',)

plt.show()
