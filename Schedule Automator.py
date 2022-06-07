'''
    File name: Schedule Automator.py
    Author: Elian Manzueta
    Date created: 06/06/2022
    Date last modified: 06/06/2022
    Python Version: 3.10.2
'''
import gspread
import sys
import re

sys.stdout = open("/Users/elian/Desktop/Nexus/Schedule/Schedule.txt", 'w')
sa = gspread.service_account()

print("Hey Hannah, here are my hours: \n")
          
# Accessing the sheet.
sh = sa.open("ScheduleTest")

# Main function
def getSchedule(worksheet):
    wks = sh.worksheet(worksheet) # Selects the desired sheet.
    total = wks.acell('I10').value # Total hours.
    print(wks.acell('B2').value, '-', wks.acell('H2').value, '\n') # Pay Period
    days = (wks.get('B2:H2')) # Batch get of all values in B2:H2.
    hours = (wks.get('B10:H10')) # Batch get of all values in B10:H10.
    
    # wks.get() outputs a nested list, so we have to flatten it and convert it to a hashable data type.
    formatted_days = tuple([item for elem in days for item in elem])
    formatted_hours = tuple([item for elem in hours for item in elem])
    
    # Using zip() to combine formatted_days and formatted_hours into a dictionary.
    dictionary_values = dict(zip(formatted_days, formatted_hours)) 
    
    schedule = '' 
    for key, value in dictionary_values.items():
        # Checks if there's an entry for the date.
        if value != (''):
            # Formatting the dictionary into a string.
            schedule += key + ': ' + value + '\n' 
    print(schedule)

    # Total hours worked
    print(f"Total: {total} hours\n")

# Main program
getSchedule('Week 1')
getSchedule('Week 2') 
