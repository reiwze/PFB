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

# Create a function 'coh_difference()'
def coh_difference():

    # Include docstrings to the function using a triple-quoted string, it is used to include information of the function.
    """
    - Function would calculate the difference in the amount of cash on hand between the day itself and the day before, from Day 40-50
    - In this function there are no parameters

    """

    # Use 'len(coh_amount)-1' to count the number of days there are, 11 days from Day 40-50 are placed inside the positions of index 0-10
    # Using the for loop with range(0, (len(coh_amount)-1), we are looking at iterating the values of the 11 days 
    for num in range(0,(len(coh_amount)-1)):

        # The amount on the first day would be assigned [num] as it is in index 0
        first_day = coh_amount[num]

        # The amount on the second day would be assigned [num+1] as it is in index 1
        second_day = coh_amount[num+1]
        
        # Use the 'if statement' to execute a portion of the code when certain condition(s) are met
        # In this case, execute the portion of the code when 'first_day' is more than 'second_day'
        if first_day > second_day:

            # Assign the variable 'difference' and find the difference between the amount of the first day and second day by subtracting it 
            difference = first_day - second_day

            # Using 'coh_days[num+1][0]', we are looking at the second day used for comparision which falls under index 0 in the 'coh_days' list 
            # Assign the variable 'difference_day' to the cash deficit day
            difference_day = coh_days[num+1][0]

            # Use .open() function to to append to the final txt file
            # Encoding allows us include longer or all characters and save files as file
            with summary_path.open(mode='a',encoding='UTF-8') as file:

                # Use .write() function to write the results and indicate end of text line in the summary report
                # Use float() function to float the 'difference_day' for our results
                file.write(f"[CASH DEFICIT] DAY: {float(difference_day)}, AMOUNT: USD{difference} \n")

                # Use .close() function to close file and prevent issues of corrupted data
                file.close()