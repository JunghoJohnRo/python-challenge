import os
import csv

# Creating a path to pull data from folder (Googled for ".expanduser" function to read the file)
budgetCSV = os.path.expanduser('~/Desktop/Homework 3/python-challenge/budget_data.csv')

# Reading the CSV file
with open(budgetCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # Define the Variables and Starting values
    firstvalue = next(csvreader)
    row = 0
    totalMonth = 1
    totalRevenue = int(firstvalue[1])
    revenueChange = 0
    currentRev = int(firstvalue[1])
    previousRev = 0
    lowestRev = int(firstvalue[1])
    greatestRev = int(firstvalue[1])
    totalRevchange = 0

    # Loop through the data
    for row in csvreader:
        
        # Total Months
        totalMonth += 1

        # Total Profits/Losses 
        totalRevenue += int(row[1])

        # Tracking Month to Month Profit/Losses Change
        previousRev = currentRev
        currentRev = int(row[1])
        revenueChange = currentRev - previousRev
        totalRevchange += revenueChange

        # Finding Greatest Decrease & Increase in Profit/Losses
        if revenueChange > greatestRev:
            greatestRev = revenueChange
            greMonth = str(row[0])
        if revenueChange < lowestRev:
            lowestRev = revenueChange
            lowMonth = str(row[0])
    
    # Calculate Average Change of Profit/Losses
    averagechange = totalRevchange/(totalMonth-1)

# Print Final Results in Terminal
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {str(totalMonth)}")
print(f"Total: ${str(totalRevenue)}")
print(f"Average Change: ${str(round(averagechange, 2))}")
print(f"Greatest Increase in Profits: {greMonth} (${str(greatestRev)})")
print(f"Greatest Decrease in Proftis: {lowMonth} (${str(lowestRev)})")

# Specify where to export Text File to
export_file = os.path.expanduser('~/Desktop/Homework 3/python-challenge/PyBank/Final.txt')

# Open the file and write what to print in Text File (Googled "\n" so it prints in the next line)
with open(export_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------------\n")
    file.write(f"Total Months: {str(totalMonth)}\n")
    file.write(f"Total: ${str(totalRevenue)}\n")
    file.write(f"Average Change: ${str(round(averagechange, 2))}\n")
    file.write(f"Greatest Increase in Profits: {greMonth} (${str(greatestRev)})\n")
    file.write(f"Greatest Decrease in Proftis: {lowMonth} (${str(lowestRev)})\n")