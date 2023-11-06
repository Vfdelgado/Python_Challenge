#Your task is to create a Python script that 
#analyzes the records to calculate each of the 
#following values:
import os
import csv

# Set path for file
csv_path = os.path.join("Resources", "budget_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

with open(csv_path, encoding='UTF-8') as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(csv_reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csv_reader:
        total_months += 1
        total_net += int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)
        month_of_change.append(row[0])

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Output the results
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${net_monthly_avg:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write results to a file
with open("Financial_Analysis_Result.txt", "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_net}\n")
    output_file.write(f"Average Change: ${net_monthly_avg:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")