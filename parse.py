import pandas as pd
import numpy as np
import json

# Initializing the relative file path
file_path = 'Mess Menu Sample.xlsx'

# Reading the data from the excel file
xl_file = pd.ExcelFile(file_path)
data = xl_file.parse("Sheet1")

# Converting the data into a pandas dataframe
df = pd.DataFrame(data)

# Replaced the weird and empty strings from the data so that all inconsistent values have the same value
df.replace("**************", "", inplace=True)
df.replace("***************", "", inplace=True)

# One day where we get a special lunch so replacing it with the normal lunch not actually but only the name
df.replace(" SPE. LUNCH","LUNCH" , inplace=True)

# Converting this menu in the table orientation of json so that I can parse it later and serialize it better
df.to_json('mess_menu.json', orient='table')

# Load the JSON data
with open('mess_menu.json', 'r') as f:
    json_data = json.load(f)

# Transform the data to the desired format
myNewData = {}

# List of dictionaries to store the data
days = ['SATURDAY', 'SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY.1','SUNDAY.1', 'MONDAY.1', 'TUESDAY.1', 'WEDNESDAY.1', 'THURSDAY.1', 'FRIDAY.1', 'SATURDAY.2']

# Storing the list of dictionary which stores the date and the meals
record = json_data['data']
for i in range(len(days)-1):

    # Storing the date for which i will serialize further meals on that date
    date = record[0][days[i]]

    # Checking if no date key is present
    if date not in myNewData:
        myNewData[date] = {'BREAKFAST': [], 'LUNCH': [], 'DINNER': []}
    
    # As the name of the meals start from the jth index
    j = 2

    while j < len(record) and record[j][days[i]] != 'LUNCH':
        
        # Adding the condition as we did have some null values in our dataframe as the no of items in menu are not the same everyday or every meal
        if record[j][days[i]] is None or record[j][days[i]].upper() in days[:7] or record[j][days[i]].upper() in days[:7] or record[j][days[i]] == "" or record[j][days[i]].upper() in days[:7]:
            j = j+1
            continue

        # Adding each meal to the dictionary
        myNewData[date]['BREAKFAST'].append(record[j][days[i]])
        j = j+1

    j = j + 1  # Skip 'LUNCH' row

    while j < len(record) and record[j][days[i]] != 'DINNER':

        if record[j][days[i]] is None or record[j][days[i]].upper() in days[:7] or record[j][days[i]].upper() in days[:7] or record[j][days[i]] == "":
            j = j+1
            continue

        myNewData[date]['LUNCH'].append(record[j][days[i]])
        j = j+1

    j = j + 1  # Skip 'DINNER' row

    while j < len(record):

        if record[j][days[i]] is None or record[j][days[i]].upper() in days[:7] or record[j][days[i]].upper() in days[:7] or record[j][days[i]] == "" or record[j][days[i]] == "":
            j = j+1
            continue

        myNewData[date]['DINNER'].append(record[j][days[i]])
        j = j+1

# Save the transformed data back to a JSON file
with open('mess_menu_final.json', 'w') as f:
    json.dump(myNewData, f, indent=4)

# Tada you got the serialized file