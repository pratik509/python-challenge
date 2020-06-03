#In this challenge, you get to be the _boss_. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.

#Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:

#* Import the `employee_data.csv` file, which currently holds employee records like the below:

#```csv
#Emp ID,Name,DOB,SSN,State
#214,Sarah Simpson,1985-12-04,282-01-8166,Florida
#15,Samantha Lara,1993-09-08,848-80-7526,Colorado
#411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
#```

#* Then convert and export the data to use the following format instead:

#```csv
#Emp ID,First Name,Last Name,DOB,SSN,State
#214,Sarah,Simpson,12/04/1985,***-**-8166,FL
#15,Samantha,Lara,09/08/1993,***-**-7526,CO
#411,Stacy,Charles,12/20/1957,***-**-8526,PA
#```

#* In summary, the required conversions are as follows:

#  * The `Name` column should be split into separate `First Name` and `Last Name` columns.

#  * The `DOB` data should be re-written into `MM/DD/YYYY` format.

#  * The `SSN` data should be re-written such that the first five numbers are hidden from view.

#  * The `State` data should be re-written as simple two-letter abbreviations.

#* Special Hint: You may find this link to be helpful—[Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).
import os

import csv

#Creating State Dictionaries 
us_state_abbrev = {
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


#Setting CSV path

csvpath = os.path.join( 'Resources', 'employee_data.csv')

#Creating List to store Data 
emp_id = []
first_name = []
last_name = []
DOB= []
SSN = []
State = []


#Opening CSV file and keep the headers

with open(csvpath , 'r') as csvfile:
    reader= csv.DictReader (csvfile)

#Appending information in the list after being chnaged

    for row in reader:
        emp_id.append(row ['Emp ID'])
        first_name.append(row['Name'].split (" ")[0])
        last_name.append(row['Name'].split (" ")[1])
        DOB.append(row['DOB'].split('-')[1] + '/' + row['DOB'].split('-')[2] + '/' + row['DOB'].split('-')[0])
        SSN.append('***-**-' + row['SSN'].split('-')[2])
        State.append(us_state_abbrev[row['State']])

zipped_data = zip (emp_id, first_name, last_name,DOB, SSN, State)

#naming output file
output_file = os.path.join('Output', 'new_data.csv')

#open and writes to csv file to the above folder destination
with open(output_file, 'w') as csvwrite:
    cleanfile = csv.writer(csvwrite, delimiter = ",")
    cleanfile.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    cleanfile.writerows(zipped_data)