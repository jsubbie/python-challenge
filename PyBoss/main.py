import os 
import csv 

pyboss_csv = os.path.join("employee_data1.csv")

# list to store data 
EmpID = []
name = []
name1 = []
first_Name = []
last_Name = []
dob = []
Social = []
State = []

with open(pyboss_csv, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:    
        EmpID.append(row[0])
        name.append(row[1])
        for i in range(len(name)):
                name = name[i]
                name1 = name.split(' ')
                first_Name.append(name1[0])
                last_Name.append(name1[1])
                name1 = []
        # dob.append(row[2])
        # for j in range(len(dob)):
        #         date_conversion = [j]
        #         date_conversion.appendstrftime('%m/%d/%Y')  
        #         date_conversion = []
        # Social.append(row[3])
        # State.append(row[4])
# date_reformat = range(.appendstrftime('%m/%d/%Y'))
  
print(first_Name, last_Name) 

# DOB        
#         dob.append(row[2])
# # social security conversion                
#         Social.append(row[3])
#         split_ssn = list(row["Social"])
#         split_ssn[0:3] = ("*", "*", "*")
#         split_ssn[4:6] = ("*", "*")
#         joined_ssn = "".join(split_ssn)
#         State.append(row[4])
# # date_reformat = range(.appendstrftime('%m/%d/%Y'))
#         date1 = datetime.datetime.strptime(dob, "%Y-%m-%d")
#         date_conversion = date1.strftime("%m/%d/%Y")
  