# ------------------------------Cash on Hand Code Starts Here------------------------------------

# Import Path method from pathlib
from pathlib import Path 
import csv 

# Create a file path by using strings to "cash_on_hand"
# Note that the `Path` refers Path function from pathlib 
coh_path= Path.cwd()/'project_group'/'csv_reports'/'Cash on Hand.csv' 

# Create 2 empty lists to store the days and amount into the lists from the csv
coh_days = [] 
coh_amount = [] 

# Use .open() function to access mode of file to read the csv file
# Encoding allows us include longer or all characters and save files as file
with coh_path.open(mode = "r", encoding = "UTF-8", newline = "") as file : 

    # Use .reader() function in csv module to read the data in Cash on Hand file
    readfiles = csv.reader(file) 

    # Use next() function to return the next item in the list
    next(readfiles) 

    # Use for loop to iterate over the range of objects. In this instance, 'line' is used as a temporary variable 
    for line in readfiles: 

        # Use .append() function to add each element into the empty list 'coh_days' 
        coh_days.append(line)

        # Use .append() function to add the amount into the empty list 'coh_amount' and use int() function to convert it into an integer
        # Use index[1] to extract the amount in the index 1 of the 'coh_amount' list
        coh_amount.append(int(line[1]))

# Create a filepath to "summary_report.txt" file where all our outputs would be 
summary_path = Path.cwd()/'project_group'/'summary_report.txt'
# Create the file using the .touch() function
summary_path.touch()
