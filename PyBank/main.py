#Your task is to create a Python script that 
#analyzes the records to calculate each of the 
#following values:
import os
import csv

# Set path for file
csv_path = os.path.join("Resources", "budget_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Open the CSV using the UTF-8 encoding
with open(csv_path, encoding='UTF-8') as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)

    #Set variables
    total_months = 0
    gains = 0
    previous_gains = 0
    monthly_changes = []
    dates = []


    # Read each row of data after the header
    for row in csv_reader:
        month = row[0]
        profit_loss = int(row[1])

        #The total number of months included in the dataset
        total_months += 1
        
        #The net total amount of "Profit/Losses" over the 
        # entire period
        gains += profit_loss

#The changes in "Profit/Losses" over the entire period, 
# #and then the average of those changes
        if total_months > 1: 
            monthly_change = profit_loss - previous_gains
            monthly_changes.append(monthly_change)
            dates.append(month)

            previous_gains = profit_loss

            average_change = round(gains/(total_months))

#The greatest increase in profits (date and amount) 
# #over the entire period
            greatest_increase = max(monthly_changes)
            greatest_date_increase = dates[monthly_changes.index(greatest_increase)]
#The greatest decrease in profits (date and amount) 
# #over the entire period
            greatest_decrease = min(monthly_changes)
            greatest_date_decrease = dates[monthly_changes.index(greatest_decrease)]



print ("Financial Analysis")
print ("------------------------")
print (f"Total Months : {total_months}")
print (f"Total : {gains}")
print (f"Average Change : {average_change}")
print (f"Greatest Increase in Profits : {greatest_date_increase} ${ greatest_increase}")
print (f"Greatest Decrease in Profits : {greatest_date_decrease} ${ greatest_decrease}")

with open("Financial_Analysis_Result.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("------------------------\n")
    file.write(f"Total Months : {total_months}\n")
    file.write(f"Total : {gains}\n")
    file.write(f"Average Change : {average_change}\n")
    file.write(f"Greatest Increase in Profits : {greatest_date_increase} ${greatest_increase}\n")
    file.write(f"Greatest Decrease in Profits : {greatest_date_decrease} ${greatest_decrease}\n")