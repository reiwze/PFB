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

# Assign the variable 'highestvalue' and find the highest value using max() function from the amount list
highestvalue = max(overheads_amount)

# Use for loop to iterate over the range of objects. In this instance, 'information' is used as a temporary variable
for information in overheads_cat:

    # Use the 'if statement' to execute a portion of the code when certain condition(s) are met
    # In this case, execute the function when the highest value in the 'overhead_amount' list is met
    if information[1] == str(highestvalue):

        # Assign the variable 'highest_overhead' to the information that is extracted
        highest_overhead = information[0]

# Create a filepath to "summary_report.txt" file where all our outputs would be 
summary_path= Path.cwd()/"project_group"/"summary_report.txt"
# Create the file using the .touch() function
summary_path.touch()

# Create a function 'overheads_function()' 
def overheads_function():

    # Include docstrings to the function using a triple-quoted string, it is used to include information of the function.
    """
    - Function would compare the overheads and find the highest overhead
    - In this function there are no parameters

    """

    # Assign the variable 'output' to the highest overhead output
    output= (f"[HIGHEST OVERHEADS] {highest_overhead}: {highestvalue}% \n")

    # Use .open() function to to append to the final txt file
    # Encoding allows us include longer or all characters and save files as file
    with summary_path.open (mode="a", encoding= "UTF-8") as file:

        # Use .write() function to write the output and indicate end of text line in the summary report
        file.write(output)

        # Use .close() function to close file and prevent issues of corrupted data
        file.close()