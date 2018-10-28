import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# Set initial variable to hold the total number of months
totalMonths = 0

# Set initial variable to hold the total net amount of "Profit/Losses"
totalRevenue = 0

# Set initial variables to hold the greatest increase in profits (date and amount)
maxDate = "n/a"
maxAmount = 0

# Set initial variables to hold the greatest decrease in profits (date and amount)
minDate = "n/a"
minAmount = 0

# Set initial variable to hold the total net change in "Profit/Losses" between months
totalChange = 0

# Set initial variable to hold the "Profit/Losses" amount for the previous month
previousAmount = 0

# Read in the CSV file
with open(csvpath, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    
    # Loop through the data
    for row in csvreader:
        
        # Add one to the total number of months
        totalMonths += 1

        # Add to the total revenue
        totalRevenue += int(row[1])

        # Set the profit change from the previous month
        profitChange = int(row[1]) - previousAmount

        # Check if we are on the first month, if so...
        if(totalMonths == 1):

            # Set the profit change to zero
            profitChange = 0

        # Check if the profit change is greater than the greatest increase in profits, if so...
        if profitChange > maxAmount:

            # Set the greatest increase in profits to the profit change
            maxDate = row[0]
            maxAmount = profitChange

        # If the profit change is less than the greatest decrease in profits...    
        elif profitChange < minAmount:
            minDate = row[0]
            minAmount = profitChange

        # Add to the total profit change
        totalChange += profitChange

        # Reset the "Profit/Losses" amount for the previous month for the next loop
        previousAmount = int(row[1])

# Set the average change in "Profit/Losses" between months
averageChange = round(totalChange / (totalMonths - 1), 2)

# Print out the analysis for the financial records
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalMonths))
print("Total: $" + str(totalRevenue))
print("Average Change: $" + str(averageChange))
print("Greatest Increase in Profits: " + maxDate + " ($" + str(maxAmount) + ")")
print("Greatest Decrease in Profits: " + minDate + " ($" + str(minAmount) + ")")

# Export a text file with the results
analysisText = open("analysis.txt", 'w')

analysisText.write("Financial Analysis\n")
analysisText.write("----------------------------\n")
analysisText.write("Total Months: " + str(totalMonths) + "\n")
analysisText.write("Total: $" + str(totalRevenue) + "\n")
analysisText.write("Average Change: $" + str(averageChange) + "\n")
analysisText.write("Greatest Increase in Profits: " + maxDate + " ($" + str(maxAmount) + ")\n")
analysisText.write("Greatest Decrease in Profits: " + minDate + " ($" + str(minAmount) + ")")