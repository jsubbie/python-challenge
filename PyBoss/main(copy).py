import os 
import csv 

pyboss_cvs = os.path.join("employee_data1.csv")

# list to store data 
EmpID = []
Name = []
Date_of_birth = []
Social = []
State = []

with open(pyboss_cvs, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    for row in csvreader:    
        EmpID.append(row[0])
        Name.append(row[1])
        new_length = row[1].split(" ")
        new_length.append(new_length[0])
        Date_of_birth.append(row[2]).appendstrftime('%m/%d/%Y')
        # date_reformat = range(.appendstrftime('%m/%d/%Y'))
        Social.append(row[3])
        State.append(row[4])

    print(EmpID)
    print(Name)
    print(Date_of_birth) 
    print(Social)
    print(State)