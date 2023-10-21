import csv
from datetime import datetime
import matplotlib.pyplot as plt

def load_company_data(file_path):
    company_data = {}
    with open(file_path, newline='', encoding='iso-8859-1') as csvfile:
        data_sheet = csv.DictReader(csvfile)
        for row in data_sheet:
            pin = row['Registered_Office_Address'][-6:]
            date = row['DATE_OF_REGISTRATION']
            try:
                date_obj = datetime.strptime(date, "%d-%m-%y")
                year = date_obj.year
                if year == 2015 and pin not in company_data and pin != '000000':
                    company_data[pin] = 1
                elif year == 2015:
                    company_data[pin] += 1
            except ValueError:
                pass
    return company_data

def load_pincode_data(file_path, company_data):
    comp_add = {}
    with open(file_path, newline='', encoding='iso-8859-1') as csvfile:
        pin_code_data = csv.DictReader(csvfile)
        for row in pin_code_data:
            pin = row['Pin Code']
            dist = row['District']
            if pin in company_data:
                count = company_data[pin]
                if dist in comp_add:
                    comp_add[dist] += count
                else:
                    comp_add[dist] = count
    return comp_add

def plot_company_counts(comp_add):
    x = list(comp_add.keys())
    y = list(comp_add.values())

    plt.bar(x, y)
    plt.xlabel('Districts')
    plt.ylabel('Company Counts')
    plt.title('Company Counts by District')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
    plt.tight_layout()  # Adjust the layout for better presentation
    plt.show()

if __name__ == '__main__':
    company_data = load_company_data('Maharastra /Maharashtra.csv')
    comp_add = load_pincode_data('Maharastra /pincode.csv', company_data)
    plot_company_counts(comp_add)
