# csv-filter-challenge-public
# Instructions
1. Click "Use this template" to create a copy of this repository in your personal github account.  
1. Using technology of your choice, complete assignment listed below.
1. Update the README in your new repo with:
    * a `How-To` section containing any instructions needed to execute your program.
    * an `Assumptions` section containing documentation on any assumptions made while interpreting the requirements.
1. Send an email to Scoir (andrew@scoir.com) with a link to your newly created repo containing the completed exercise.

## Expectations
1. This exercise is meant to drive a conversation. 
1. Please invest only enough time needed to demonstrate your approach to problem solving, code design, etc.
1. Within reason, treat your solution as if it would become a production system.

## Assignment
Create a command line application that parses a CSV file and filters the data per user input.

The CSV will contain three fields: `first_name`, `last_name`, and `dob`. The `dob` field will be a date in YYYYMMDD format.

The user should be prompted to filter by `first_name`, `last_name`, or birth year. The application should then accept a name or year and return all records that match the value for the provided filter. 

Example input:
```
first_name,last_name,dob
Bobby,Tables,19700101
Ken,Thompson,19430204
Rob,Pike,19560101
Robert,Griesemer,19640609
```
## How-To
Ensure that the scoir.py file and the desired csv file are in the same directory.
Then, from the command line, simply run python3 scoir.py
The program should prompt the user for the rest of the necessary inputs.

## Assumptions
The biggest "assumption" here is that the mentioned CSV is already formatted correctly.  
Without this guarantee, there would need to be additional checks to make sure first_name, last_name, and DOB
are all in their specified formats, and additionally, I would have to check if first_name was the first column,
last_name was the second, and DOB was the third. For this problem's sake, I'm assuming the csv that the program 
will be tested on is formatted as the example specified. 

Although in the solution I specify both the encoding and delimter ("," and UTF-8), I didn't do extensive testing if 
varying ones were used. So fair warning, this might break if a WEIRD csv is passed into it.
Overall, I'm hoping that delimiter checking and encoding stuff are out of scope for this...

Anyways, the last "assumption" made is due to a little bit of vague wording in the problem description..
"The application should then accept a name or year and return all records that match the value for the provided filter"

For this part, I assumed the filter was case sensitive and was referring to records that contained the term 
as a substring.. By this, I mean if a user chooses to search for the first name "Rob", both records with "Rob"
and "Robert" will be displayed. Also, if said user searched for "rob", he would get neither record, as Rob should be capitalized.
-Note that only one or two lines of code would have to be changed to make any of these changes.. 
	(e.g. rather than "term in row[col]" it would be "term == row[col]"). 

Figured it was still worth pointing out..

Other than that, I think this solution is simple enough and gets the point across..
Looking forward to speaking on Friday! 

Best,
J





