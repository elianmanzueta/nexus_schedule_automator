'''
    File name: Schedule Automator.py
    Author: Elian Manzueta
    Date created: 06/06/2022
    Date last modified: 06/06/2022
    Python Version: 3.10.2
'''
import gspread
import sys

sys.stdout = open("/Users/elian/Desktop/Nexus/Schedule/Schedule.txt", 'w')
sa = gspread.service_account()

def getSchedule():
    total = wks.acell('I10').value # Total hours
    print(wks.acell('B2').value, '-', wks.acell('H2').value, '\n') # Pay Period
    days = ((wks.get('B2:H2'))) # Batch get of all values in B2:H2
    hours = ((wks.get('B10:H10'))) # Batch get of all values in B10:H10
    
    # wks.get() outputs a nested list, so we have to flatten them into one for it to be turned into a dictionary.
    formatted_days = tuple([item for elem in days for item in elem])
    formatted_hours = tuple([item for elem in hours for item in elem])
    
    # Using zip() to combine formatted_days and formatted_hours into a dictionary
    dictionary_values = dict(zip(formatted_days, formatted_hours)) 
    
    schedule = '' 
    for key, value in dictionary_values.items():
        # Iterating through the dictionary to insert it into the schedule string. 
        if value != '':  
            schedule += key + ': ' + value + '\n' 
    print(schedule)

    # Total hours worked
    print(f"Total: {total}hrs\n")

print("Hey Hannah, here are my hours: \n")
                 
# Accessing the sheet
sh = sa.open("ScheduleTest")

# Changing to Sheet 1
wks = sh.worksheet("Week 1")

getSchedule() 
   
# Changing to Sheet 2 
wks = sh.worksheet("Week 2")

getSchedule() 

# End