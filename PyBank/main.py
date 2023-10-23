#main.py
import os
import csv

#variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
months = []

#Set path for file
csvpath = os.path.join("..""budget_data.csv")
csv_path = "budget_data.csv"

# Read in the CSV file
with open(csv_path,encoding='utf') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Skip Header 
    next(csvreader)

    for row in csvreader:
        #The net total amount of "Profit/Losses" over the entire period
        date = row[0]
        profit_loss = int(row[1])

#The total number of months included in the dataset
        total_months += 1
        net_total += profit_loss
    # Calculate changes in profit/loss
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            months.append(date)
        
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
max_increase = max(changes)
max_decrease = min(changes)

# Find the corresponding dates for the greatest increase and decrease
date_max_increase = months[changes.index(max_increase)]
date_max_decrease = months[changes.index(max_decrease)]

# Print the results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {date_max_increase} (${max_increase})")
print(f"Greatest Decrease in Profits: {date_max_decrease} (${max_decrease})")

# Save the results to a text file
with open("financial_analysis.txt", "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("-----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {date_max_increase} (${max_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {date_max_decrease} (${max_decrease})\n")
