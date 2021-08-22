# Import Dependencies 
import os, csv
from itertools import zip_longest

# Input file path 
employeedata = os.path.join("Python-challenge", "PyBoss", "employee_data.csv")
employeedata = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\Python-Challenge\PyBoss\employee_data.csv'

# Set empty lists)
employeeid = []
fullname = []
firstname = []
lastname = []
birthday = []
DOB = []
ssn = []
hiddenssn = []
stateabbrev = []

# Dictionary containing states names as keys and abbreviations as values (provided) 
usstateabbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Open CSV in read mode with context manager
with open(employeedata) as csvfile:
    csvreader = csv.reader(csvfile) 

    # Skip the header 
    header = next(csvreader)     
    
    # Iterate through each row stored in csvreader
    for row in csvreader:

        # Append employee id's into list, no formatting changes needed
        employeeid.append(row[0])


        # Split full name into first name and last name lists 
        # No middle names in this data
        fullname = row[1].split(" ")   
        firstname.append(fullname[0])
        lastname.append(fullname[1])

        # Split date of birth by "-", we have three lists indexed and stored in date_of_birth
        # Append and format date of birth into d_o_b list
        birthday = row[2].split("/")
        DOB.append(birthday[1]+ "/" + birthday[0] + "/" + birthday[2])
         
        

        # Split the SSN by "-"
        # Append and format ssn into ssn_private list 
        ssn = row[3].split("-")
        hiddenssn.append("***-**-" + ssn[2])

        # Match the state list item to a dictionary value, if they match, append dictionary key to list abbrev
        stateabbrev.append(usstateabbrev[row[4]])

# Set output file path
converteddata = os.path.join("Python-Challenge", "PyBoss", "converted_data.csv")

converteddata = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\Python-Challenge\PyBoss\converted_data.csv'

Rows = [employeeid, firstname, lastname, DOB, hiddenssn, stateabbrev]

exportdata = zip_longest(*Rows, fillvalue = '')

with open(converteddata,"w", newline = '', encoding='utf-8') as file:

    # Initialize csv.writer
    csvwriter = csv.writer(file)

    # Write the first row (headers)
    csvwriter.writerow(["Employee Id", "First Name", "Last Name", "DOB", "SSN", "State"])
    
    # Write the second and the rest
    csvwriter.writerows(exportdata)