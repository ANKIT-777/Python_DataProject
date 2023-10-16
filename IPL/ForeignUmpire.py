import csv

Umpires = []

with open('IPL/matches.csv', newline='') as csvfile:
    Dataset = csv.DictReader(csvfile)

    for row in Dataset:
        umpire1 = row['umpire1']
        umpire2 = row['umpire2']
        umpire3 = row['umpire3']

        if umpire1 not in Umpires:
            Umpires.append(umpire1)
        if umpire2 not in Umpires:
            Umpires.append(umpire2)
        if umpire3 not in Umpires:
            Umpires.append(umpire3)

with open('IPL/umpires.csv', newline='') as csvfile:
    Nation = csv.DictReader(csvfile)

    for row in Nation:
        umpire = row['umpire']
        country = row[' country']

        for entry in Umpires:
            if entry == umpire and country != ' India':
                entry = country

print(Umpires)
