## Option 3: PyBoss

"""![Boss](Images/boss.jpg)

In this challenge, you get to be the _boss_. You oversee hundreds of employees across 
the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. 
Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided 
to purchase a new HR system, and unfortunately for you, the new system requires employee records 
be stored completely differently.

Your task is to help bridge the gap by creating a Python script able to convert your employee 
records to the required format. Your script will need to do the following:

* Import the `employee_data1.csv` and `employee_data2.csv` files, which currently holds 
employee records like the below:


```
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```

* Then convert and export the data to use the following format instead:


```
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
```

* In summary, the required conversions are as follows:

  * The `Name` column should be split into separate `First Name` and `Last Name` columns.

  * The `DOB` data should be re-written into `DD/MM/YYYY` format.

  * The `SSN` data should be re-written such that the first five numbers are hidden from view.

  * The `State` data should be re-written as simple two-letter abbreviations.

* Special Hint: You may find this link to be helpful—
[Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).

"""
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
        dob.append(row[2])
        for j in range(len(dob)):
                date_conversion = [j]
                date_conversion.appendstrftime('%m/%d/%Y')  
                date_conversion = []
        Social.append(row[3])
        State.append(row[4])
# date_reformat = range(.appendstrftime('%m/%d/%Y'))
  
print(first_Name, last_Name, date_conversion) 



"""
import os
import csv

# Path to collect data from the Resources folder
wrestlingCSV = os.path.join('..','Resources','WWE-Data-2016.csv')

# Define the function and have it accept the 'wrestlerData' as its sole parameter
def getPercentages(wrestlerData):
    
    # Total matches can be found by adding wins, losses, and draws together
    totalMatches = int(wrestlerData[1]) + int(wrestlerData[2]) + int(wrestlerData[3])
    wins = int(wrestlerData[1])
    losses = int(wrestlerData[2])
    draws = int(wrestlerData[3]) 
    # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    winPercent = (wins/totalMatches)*100

    # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    lossPercent = (losses/totalMatches)*100

    # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    drawPercent = (draws/totalMatches)*100

    # If the loss percentage is over 50, typeOfWrestler is "Jobber". Otherwise it is "Superstar".
    if(lossPercent > 50):
        typeOfWrestler = "Jobber"
    else:
        typeOfWrestler = "Superstar"

    # Print out the wrestler's name and their percentage stats
    print("Stats for " + wrestlerData[0])
    print("WIN PERCENT: " + str(winPercent))
    print("LOSS PERCENT: " + str(lossPercent))
    print("DRAW PERCENT: " + str(drawPercent))
    print(wrestlerData[0] + " is a " + typeOfWrestler)

# Read in the CSV file
with open(wrestlingCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    nameToCheck = input("What wrestler do you want to look for? ")
    
    # Loop through the data
    for row in csvreader:
        # If the wrestler's name in a row is equal to that which the user input, run the 'getPercentages()' function
        if(nameToCheck == row[0]):
            getPercentages(row)


# now = datetime.datetime.now()
# date_string = now.strftime('%Y-%m-%d')
# print(date_string)

"""