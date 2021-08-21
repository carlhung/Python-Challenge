# Import Dependencies
import os, csv
from pathlib import Path 

# Declare file path
pybank = os.path.join("..", "Resources", "budget_data.csv")

pybank = Path(r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\Python-Challenge\PyBank\Resources\budget_data.csv')

# Create empty lists to iterate through specific rows
monthscount = []
profit = []
monthlychange = []
 
with open(pybank) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip header
    pybank_header = next(csv_reader)

    # Loop thru the rows in the file
    for row in csv_reader: 

        # Append the total months and total profit to the related list
        monthscount.append(row[0])
        profit.append(int(row[1]))

    # Calculate monthly change of profit
    for i in range(len(profit)-1):
        
        # Take the difference between two months and append to the related list
        monthlychange.append(profit[i+1]-profit[i])
      
# Capture the max increase(Max) and max decrease(Min) of the the monthly profit
maxincrease = max(monthlychange)
maxdecrease = min(monthlychange)

# Correlate max and min to the proper month using month list and index from Max and Min
# Put plus 1 at the end because month associated with change is the next month
maxincreasemonth = monthlychange.index(max(monthlychange)) + 1
maxdecreasemonth = monthlychange.index(min(monthlychange)) + 1 

# Print result
print("Financial Analysis")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Total Months: {len(monthscount)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(monthlychange)/len(monthlychange),2)}")
print(f"Greatest Increase in Profits: {monthscount[maxincreasemonth]} (${(str(maxincrease))})")
print(f"Greatest Decrease in Profits: {monthscount[maxdecreasemonth]} (${(str(maxdecrease))})")

# Output files
output_file = Path(r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\Python-Challenge\PyBank\Financial Analysis Summary.txt')

with open(output_file,"w") as file:
    
    # Write methods to print to Financial Analysis Summary 
    file.write("Financial Analysis\n")
    file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    file.write(f"Total Months: {len(monthscount)}\n")
    file.write(f"Total: ${sum(profit)}\n")
    file.write(f"Average Change: {round(sum(monthlychange)/len(monthlychange),2)}\n")
    file.write(f"Greatest Increase in Profits: {monthscount[maxincreasemonth]} (${(str(maxincrease))})\n")
    file.write(f"Greatest Decrease in Profits: {monthscount[maxdecreasemonth]} (${(str(maxdecrease))})\n")