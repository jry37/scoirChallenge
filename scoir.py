# J Yeager
# 12/9/2021
# Scoir Coding Challenge
# This is my python3 solution to the csv filter challenge for scoir.
#  
# Intructions:
# Create a command line application that parses a CSV file and filters the data per user input.
# The CSV will contain three fields: first_name, last_name, and dob. The dob field will be a date in YYYYMMDD format.
# The user should be prompted to filter by first_name, last_name, or birth year. The application should then accept a
# name or year and return all records that match the value for the provided filter.
# 
# Example input is included in the original repo. I have included the example file 'example.csv', which is a comma delimited csv file


# I will be writing a basic solution to this program in Python, that can be ran entirely from the command line.
# Just make sure that your file, with name filename.csv, is in the same directory as scoir.py.
#-----------------------------------------------------------------
# To run: > python3 scoir.py
#-----------------------------------------------------------------

import csv
if __name__ == "__main__":
    #dictionary of filter types and their abbreviations
    filterdict = {
        "f": "first_name",
        "l": "last_name",
        "d": "date_of_birth"
    }

    # Step 1: prompts user for name of their csv file then stores
    print("1. Please enter the name of your CSV file:")
    filename = str(input())
    print("Thank you. The CSV that will be parsed is: " + filename + "\n")
    
    # Step 2: prompts user for method of filtering then stores. 
    #   -note that this can be either first_name, last_name, or date of birth
    print("2. Now, please enter the category you would like to filter by.\nThe options are first_name (f), last_name (l), or date_of_birth (d). Please enter 'f', 'l', or 'd', to choose.")
    valid = False
    while (not valid):
        filterInput = str(input())
        if filterInput.lower() in filterdict:
            filterType = filterdict.get(filterInput)
            valid = True
        else:
            print(filterInput + " is not a valid input filter type. Please enter only 'f', 'l', or 'd'.")
    
    print("Thank you! You have chosen to filter by: " + filterType + "\n")


    # Step 3: prompt user for name or year to filter by then store
    print("Finally, please enter the actual term you would like to filter by: ")
    term = str(input())
    print("Thank you! You have chosen to search for records that contain the " + filterType + ": " + term)

    #Final print message that shows the file, filter, and search term.
    print("\nCurrently parsing the file: "+ filename + ", filtering by category: " + filterType + "; and searching for term: " + term + "\n")


    # Step 3.5: Assigning correct column to search based on filter type
    # Step 4: open the csv file for parsing and create a csv reader object to parse the given file
    # Step 5: parse the csv to find records matching the provided term
    if filterType == "first_name":
        col=0
    elif filterType =="last_name":
        col=1
    else:
        col=2
        
    with open(filename, 'r', encoding='utf-8-sig') as file:
        csvreader = csv.reader(file, delimiter=",")
        matching_records = []
        for row in csvreader:
           if term in row[col]:
                matching_records.append(row)
    
    # Step 6: Output the matching records to the user
    if len(matching_records) > 0:
        print("The following records match your search term: ")
        for record in matching_records:
            print(record)
    else:
        print("I'm very sorry. No records match your search filters.")
    

    print("\nTo search for more records with different filters, please run the program again! Thanks.")
    

   

   
    

    
        



    