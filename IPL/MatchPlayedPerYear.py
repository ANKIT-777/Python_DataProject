import csv
import matplotlib.pyplot as plt


Umpires = {}  # Initialize an empty dictionary

with open('IPL/matches.csv', newline='') as csvfile:

    Dataset = csv.DictReader(csvfile)

    for row in Dataset:
        umpire1 = row['umpire1']
        umpire2 = row['umpire2']
        umpire3 = row['umpire3']
        
        if umpire1 not in Umpires:
            Umpires[umpire1] = umpire1
        if umpire2 not in Umpires:
            Umpires[umpire2] = umpire2
        if umpire3 not in Umpires:
            Umpires[umpire3] = umpire3   
                        
            
with open('IPL/umpires.csv', newline='') as csvfile:  
    Nation = csv.DictReader(csvfile)  
    Count_Ump = {}      
    
    for row in Nation:
        umpire = row['umpire']
        country = row[' country']
        if country != ' India':
            if umpire in Umpires and country not in Count_Ump:
                Count_Ump[country] = 1
            else:
                Count_Ump[country] +=1    



x = list(Count_Ump.values())
lab = list(Count_Ump.keys())


plt.pie(x,labels=lab,startangle=90)
plt.show()





           