
import os, csv
pybank =  r"./Resources/budget_data.csv" # you can do this way.

# when using with. when it leaves the scope, it will automatically call .close()
# with open(pybank) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")

# this class can be used "with".
class Budget(object):
    def __init__(self, path):
        self._path = path
        self._file = open(self._path)
        self._data = csv.reader(self._file, delimiter=",")
    
    # def __enter__(self):
    #     self._file = open(self._path)
    #     self._data = csv.reader(self._file, delimiter=",")
    #     return self
        
    # def __exit__(self):
    #     self._file.close()

    def close(self):
        if self._file:
            self._file.close()
            self._file = None
    
    def _reset_pointer(self):
        self._file.seek(0)

    def _skip_header(self):
        self._reset_pointer()
        next(self._data)

    def total_months(self):
        self._skip_header()
        return len(list(self._data))

    def monthly_change(self):
        self._skip_header()
        change = 0
        previous_profile = 0
        average_profile = 0
        change_list = []
        # profile_diff = []
        for row in self._data:
            change = float(row[1]) - previous_profile
            change_list.append(change)
            previous_profile = float(row[1])
        change_list.remove(change_list[0])
        average_profit = sum(change_list) / (len(change_list))
        max_increase = max(change_list)
        max_decrease = min(change_list)
        max_increase_month = change_list.index(max_increase) + 1
        max_decrease_month = change_list.index(max_decrease) + 1
        return average_profit, max_increase_month, max_decrease_month, max_increase, max_decrease

    def profit(self):
        self._skip_header()
        profit = 0
        for row in self._data:
            profit += float(row[1]) 
        return profit

    def months_list(self):
        self._skip_header()
        months_list = []
        for row in self._data:
            months_list.append(row[0])
        return months_list

# tried to use "with", but i encountered a weird error:
# TypeError: __exit__() takes 1 positional argument but 4 were given

# I haven't passed 4 arguemens to __exit__(), because when using "with", once you left the scope, it calls __exit__() automatically.

# if you want to use "with" for your class, you need to define __enter__() and __close__()

# with Budget(pybank) as budget_data:

budget_data = Budget(pybank)
months = budget_data.total_months()
print("number of months: ", months)
profit = budget_data.profit()
print("profit: ", profit)
average_profit, max_increase_month, max_decrease_month, max_increase, max_decrease = budget_data.monthly_change()
print(f"Average Change: ", round(average_profit,2))
months_list = budget_data.months_list()
print(f"Greatest Increase in Profits: {months_list[max_increase_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {months_list[max_decrease_month]} (${(str(max_decrease))})")
budget_data.close() # i don't use "with" to open. so, i need to close manually. otherwise, memory leak.