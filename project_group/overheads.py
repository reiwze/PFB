# -------------------------------------------Overheads Code Starts Here-------------------------------------------------

# Import Path method from pathlib
from pathlib import Path
import csv

# Create a file path by using strings to "Overheads"
# Note that the `Path` refers Path function from pathlib 
overheads_read = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"

# Create 2 empty lists to store the catagories and amount into the lists from the csv
overheads_cat=[]
overheads_amount= []

# Use .open() function to access mode of file to read the csv file
# Encoding allows us include longer or all characters and save files as file
with overheads_read.open (mode="r", encoding= "UTF-8") as file: 

    # Use .reader() function in csv module to read the data in Overheads file
    readfiles= csv.reader(file)

    # Use next() function to return the next item in the list
    next(readfiles)

    # Use for loop to iterate over the range of objects. In this instance, 'line' is used as a temporary variable
    for line in readfiles:

        # Use .append() function to add each element into the empty list 'overheads_cat' 
        overheads_cat.append(line)

        # Use .append() function to add the amount into the empty list 'overheads_amount'  
        # Use index[1] to extract the amount in the index 1 of the 'overheads_amount' list
        overheads_amount.append(float(line[1]))
