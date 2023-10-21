import csv
import matplotlib.pyplot as plt

def process_and_plot_number_of_matches(matches_csv_path):
    number_of_matches = {}

    with open(matches_csv_path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            season = row['season']
            if season not in number_of_matches:
                number_of_matches[season] = 1
            else:
                number_of_matches[season] += 1

    return number_of_matches

def plot_number_of_matches(number_of_matches):
   
    seasons = sorted(number_of_matches.keys())
    match_counts = [number_of_matches[season] for season in seasons]
    
    plt.bar(seasons, match_counts)
    plt.xlabel('Season')
    plt.ylabel('Number of Matches')
    plt.title('Number of Matches Per Season')
    plt.xticks(rotation=45)
    plt.show()

def main():
    matches_csv_path = 'IPL/matches.csv'
    number_of_matches = process_and_plot_number_of_matches(matches_csv_path)
    plot_number_of_matches(number_of_matches)

if __name__ == '__main__':
    main()
