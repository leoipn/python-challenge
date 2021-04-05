import os
import csv

total_months = 0
net_total_amount = 0
amount_change = 0
previous_amount = 0
lst_amount_changes = []
greatest_increase = {"month":"","amount":0}
greatest_decrease = {"month":"","amount":0}

## Main Code
csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read each row of the csv file
    for row in csvreader:
        # Total months in the file
        total_months += 1
    
        # Net total amount
        net_total_amount = int(row[1]) + net_total_amount

        # Get the amount changes to use them to calculate the average.
        if previous_amount != 0:
            amount_change = float(row[1]) - previous_amount 
            lst_amount_changes.append(amount_change)
        previous_amount = float(row[1])

        # We compare each row value with the previous one to know wich one is the greatest increase.
        if(amount_change > int(greatest_increase["amount"])):
            greatest_increase["month"] = row[0]
            greatest_increase["amount"] = amount_change

        # We compare each row value with the previous one to know wich one is the greatest decrease.
        if(amount_change < int(greatest_decrease["amount"])):
            greatest_decrease["month"] = row[0]
            greatest_decrease["amount"] = amount_change

    # We calculate the average
    average = sum(lst_amount_changes)/len(lst_amount_changes)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average  Change: ${average:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['amount']})")

# Specify the file to write to
output_path = os.path.join("analysis", "financial_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
file = open(output_path, 'w')
file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {total_months}\n")
file.write(f"Total: ${net_total_amount}\n")
file.write(f"Average  Change: ${average:.2f}\n")
file.write(f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})\n")
file.write(f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['amount']})\n")

file.close()