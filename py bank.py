import os
import csv

# Variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# csv file
csvpath = os.path.join('/Users', 'joelfernandes', 'Desktop', 'budget_data.csv')


with open(csvpath, newline='') as csvfile:
    # CSV Reader (Holds Contents)
    csvreader = csv.reader(csvfile, delimiter=',')


    csv_header = next(csvreader)
    row = next(csvreader)

    # Calculate Total Number Of Months, Net Amount Of Profit/Losses & Set Variables For Rows
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    # Read Each Row Of Data After The Header
    for row in csvreader:


        # Calculations of Number Of Months Included In Dataset
        total_months += 1
        # Calculate Net Amount Of Profit/Losses Over The Entire Period
        net_amount += int(row[1])

        # Change From Current Month To Previous Month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])

        # Calculate The Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        # Calculate The Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

            # The Average & The Date
    average_change = sum(monthly_change) / len(monthly_change)

    highest = max(monthly_change)
    lowest = min(monthly_change)


print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")


text = open('/Users/joelfernandes/Desktop/answer.csv', 'w+')


# Write New Data
text.write(f"Financial Analysis\n")
text.write(f"---------------------------\n")
text.write(f"Total Months: {total_months}\n")
text.write(f"Total: ${net_amount}\n")
text.write(f"Average Change: ${average_change}\n")
text.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
text.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")