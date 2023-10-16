import csv
from datetime import datetime
import matplotlib.pyplot as plt


with open('Maharastra /Maharashtra.csv', newline='',encoding='iso-8859-1') as csvfile:
    DataSheet = csv.DictReader(csvfile)
    
    Company_Dist = {}
    for row in DataSheet:
        pin = row['Registered_Office_Address'][-6:]
        date = row['DATE_OF_REGISTRATION']
        try:
            date_obj = datetime.strptime(date, "%d-%m-%y")
            year = date_obj.year
            if year == 2015 and pin not in Company_Dist and pin != '000000':
                
                    Company_Dist[pin] = 1
            elif year == 2015:

                    Company_Dist[pin] += 1
                    
        except ValueError:
            pass



with open('Maharastra /pincode.csv', newline='',encoding='iso-8859-1') as csvfile:
    PIN_CODE = csv.DictReader(csvfile)
    Comp_add = {}
    for row in PIN_CODE:
        pin = row['Pin Code']
        dist = row['District']
        
        if pin in Company_Dist:
            cnt = Company_Dist[pin]
            # Accumulate the counts for the same pin code
            if dist in Comp_add:
                Comp_add[dist] += cnt
            else:
                Comp_add[dist] = cnt



x = list(Comp_add.keys())
y = list(Comp_add.values())

plt.bar(x, y)
plt.xlabel('Districts')
plt.ylabel('Company Counts')
plt.title('Company Counts by District')
plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
plt.tight_layout()  # Adjust the layout for better presentation

plt.show()

