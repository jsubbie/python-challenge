import os 
import csv 
import datetime

pyboss_csv = os.path.join("employee_data1.csv")

# list to store data 
empid = []
name = []
name_split = []
first_name = []
last_name = []
dob = []
dob_reformat =[]
social = []
state = []

with open(pyboss_csv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        empid.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        social.append(row[3])
        state.append(row[4])

        for i in range(len(name)):
                name = name[i]
                name_split = name.split(" ")
                first_name.append(name_split[1])
                last_name.append(name_split[2])

        for j in range(len(dob)):
                dob = [j]
                date_reformat = range(dob.appendstrftime('%m/%d/%Y'))
                # date_reformat.appendstrftime('%m/%d/%Y')  
                date_reformat = [3]
        
        for h in range(len(social)):
                social = social[h]
                split_ssn = list(row["social"])
                split_ssn[0:3] = ("*", "*", "*")
                split_ssn[4:6] = ("*", "*")
                joined_ssn = "".join(split_ssn)

        for g in range(len(state))        
                state = state[g]
                state_abb = list(row[g])
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
                state_conversion = range(us_state_abbrev.append[4]))

print(empid, first_name, last_name, date_reformat, joined_ssn, state_conversion)                         
  