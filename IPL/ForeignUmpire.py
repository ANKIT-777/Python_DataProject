import csv
import matplotlib.pyplot as plt


def extract_umpires_from_matches(file_path):

    umpires = set()

    with open(file_path, newline='') as csvfile:
        dataset = csv.DictReader(csvfile)

        for row in dataset:
            umpire1 = row['umpire1']
            umpire2 = row['umpire2']
            umpire3 = row['umpire3']

            umpires.add(umpire1)
            umpires.add(umpire2)
            umpires.add(umpire3)

    return umpires


def transform_umpires_to_nationality_counts(umpires):

    umpires_nations = {}

    with open('IPL/umpires.csv', newline='') as csvfile:
        nation = csv.DictReader(csvfile)

        for row in nation:
            umpire = row['umpire']
            country = row[' country'].strip()  # Remove leading and trailing spaces

            if umpire in umpires and country != 'India':
                if country in umpires_nations:
                    umpires_nations[country] += 1
                else:
                    umpires_nations[country] = 1

    return umpires_nations


def load_umpire_nationality_counts(umpires_nations):

    plt.bar(list(umpires_nations.keys()), list(umpires_nations.values()))
    plt.xlabel('Country')
    plt.ylabel('Number of Umpires')
    plt.title('Number of Umpires per Country in IPL 2023')
    plt.show()


def main():
    # Extract the umpires from the IPL matches CSV file
    umpires = extract_umpires_from_matches('IPL/matches.csv')

    # Transform the umpires set into a dictionary of nationality counts
    umpires_nations = transform_umpires_to_nationality_counts(umpires)

    # Plot the number of umpires from each country in the IPL
    load_umpire_nationality_counts(umpires_nations)


if __name__ == '__main__':
    main()
