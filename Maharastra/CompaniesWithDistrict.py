# Import necessary libraries
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Open the CSV file 'Maharashtra.csv' containing company registration data
with open('Maharastra /Maharashtra.csv', newline='', encoding='iso-8859-1') as csvfile:
    DataSheet = csv.DictReader(csvfile)
    
    # Create a dictionary to store the count of companies for each PIN code
    Company_Dist = {}
    
    # Iterate through each row in the data
    for row in DataSheet:
        # Extract the last 6 characters of the 'Registered_Office_Address' as the PIN code
        pin = row['Registered_Office_Address'][-6:]
        
        # Extract the date of registration
        date = row['DATE_OF_REGISTRATION']
        
        try:
            # Parse the date into a datetime object
            date_obj = datetime.strptime(date, "%d-%m-%y")
            year = date_obj.year
            
            # Check if the year is 2015 and the PIN code is not '000000'
            if year == 2015 and pin not in Company_Dist and pin != '000000':
                Company_Dist[pin] = 1
            elif year == 2015:
                Company_Dist[pin] += 1
        except ValueError:
            # Handle parsing errors in case the date is not in the expected format
            pass

# Open the 'pincode.csv' file, which contains PIN code to district mapping
with open('Maharastra /pincode.csv', newline='', encoding='iso-8859-1') as csvfile:
    PIN_CODE = csv.DictReader(csvfile)
    
    # Create a dictionary to store the count of companies for each district
    Comp_add = {}
    
    # Iterate through each row in the PIN code data
    for row in PIN_CODE:
        pin = row['Pin Code']
        dist = row['District']
        
        # Check if the PIN code from the registration data exists in Company_Dist
        if pin in Company_Dist:
            cnt = Company_Dist[pin]
            
            # Accumulate the counts for the same PIN code and district
            if dist in Comp_add:
                Comp_add[dist] += cnt
            else:
                Comp_add[dist] = cnt

# Extract x and y values for the bar chart
x = list(Comp_add.keys())
y = list(Comp_add.values())

# Create and customize the bar chart
plt.bar(x, y)
plt.xlabel('Districts')
plt.ylabel('Company Counts')
plt.title('Company Counts by District')
plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
plt.tight_layout()  # Adjust the layout for better presentation

# Display the bar chart
plt.show()
