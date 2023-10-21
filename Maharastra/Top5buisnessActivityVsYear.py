import csv
import matplotlib.pyplot as plt

def extract_data(file_path):
    # Extract data from the CSV file
    Activities = {}
    with open(file_path, newline='', encoding='iso-8859-1') as csvfile:
        Dataset = csv.DictReader(csvfile)
        for row in Dataset:
            date = row['DATE_OF_REGISTRATION'][-2:]
            activity = row['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']

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

    return Activities

def transform_data(Activities):
    # Transform data by selecting the top activities for each year
    sorted_data = {date: dict(sorted(data.items(), key=lambda item: item[1], reverse=True)) for date, data in Activities.items()}

    top_activity_year = {}
    for year, year_activities in sorted_data.items():
        top_activities = list(year_activities)[:5]
        top_activity_year[year] = top_activities

    return top_activity_year

def prepare_data_for_plot(top_activity_year):
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
                bar_data[activity].append(Activities[year][activity])
            else:
                bar_data[activity].append(0)

    return bar_data, top_activity_year

def plot_data(bar_data, top_activity_year):
    # Plot the data
    x = list(range(len(top_activity_year)))
    width = 0.10
    fig, ax = plt.subplots()

    for i, activity in enumerate(bar_data):
        ax.bar([pos + width * i for pos in x], bar_data[activity], width=width, label=activity)

    ax.set_xticks([pos + width * 2 for pos in x])
    ax.set_xticklabels(top_activity_year.keys())
    ax.set_ylabel("Number of Companies")
    ax.set_title("Top 5 Activities in Maharashtra by Number of Companies (2000-2010)")
    ax.legend(loc='upper right', bbox_to_anchor=(1, 1))
    plt.show()

if __name__ == '__main__':
    file_path = 'Maharastra /Maharashtra.csv'  # Adjust the file path

    # ETL Process
    Activities = extract_data(file_path)
    top_activity_year = transform_data(Activities)
    bar_data, top_activity_year = prepare_data_for_plot(top_activity_year)
    plot_data(bar_data, top_activity_year)
