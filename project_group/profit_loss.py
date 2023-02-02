# -------------------------------------------Profit and Loss Code Starts Here-------------------------------------------------

# Import Path method from pathlib
from pathlib import Path
import csv

# Create a file path by using strings to "Profits and Loss"
# Note that the `Path` refers Path function from pathlib 
profitloss_read = Path.cwd()/"project_group"/"csv_reports"/"Profits and Loss.csv"

# Create 2 empty lists to store the days and amount into the lists from the csv
profit_loss_days = []
profit_loss_amount = []

# Use .open() function to access mode of file to read the csv file 
# Encoding allows us include longer or all characters and save files as file
with profitloss_read.open(mode = "r", encoding = "UTF-8", newline = "") as profit_loss :

    # Use .reader() function in csv module to read the data in Profit and Loss file
    readfiles = csv.reader(profit_loss)

    # Use next() function to return the next item in the list
    next(readfiles)

    # Use for loop to iterate over the range of objects. In this instance, 'line' is used as a temporary variable
    for line in readfiles: 

        # Use .append() function to add each element into the empty list 'profit_loss_days'
        profit_loss_days.append(line)

        # Use .append() function to add the amount into the empty list 'profit_loss_amount' and use int() function to convert it into an integer
        # Use index[4] to extract the amount in the index 4 of the 'profit_loss_amount' list 
        profit_loss_amount.append(int(line[4]))

# Create a filepath to "summary_report.txt" file where all our outputs would be 
summary_path = Path.cwd()/"project_group"/"summary_report.txt"

# Create the file using the .touch() function
summary_path.touch()

