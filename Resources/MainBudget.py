import os
import csv

budgetdatacsv = os.path.join('budget_data.csv')
outputfile = os.path.join('budgetanalysis.txt')

total_months_row = 0
total_revenue = 0
total_monthly_change = 0
max_increase = 0.00
max_decrease = 0.00
max_increase_date = 0
max_decrease_date = 0
current_date = 0
ProfitLosses = []


with open('budget_data.csv', newline='') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    for i in csvreader:
        total_months_row = total_months_row + 1
        total_revenue = total_revenue + int(i[1])
        previous_revenue = int(i[1])
        ProfitLosses.append(int(i[1]))
        # for budgetDataRow in csvreader:

    # total_months_row = total_months_row + 1
for x in range(0, len(ProfitLosses)):
    previous_revenue = ProfitLosses[x-1]
    current_revenue = ProfitLosses[x]
    total_revenue = total_revenue + current_revenue

    # current_date = i[0]
    current_monthly_change = current_revenue - previous_revenue
    total_monthly_change = total_monthly_change + current_monthly_change

    # calculate revenue change for each month and capture max, min values.
    if total_monthly_change > 1:
        total_monthly_change = current_revenue - previous_revenue
        total_revenue = total_revenue + total_monthly_change
        total_revenue = total_revenue + 1
        avg_change = total_monthly_change / total_months_row

    if total_monthly_change >= 0:
        if total_monthly_change > max_increase:
            max_increase = total_monthly_change
            max_increase_date = current_date
            avg_change = total_monthly_change / total_months_row

    elif total_monthly_change < 0:
        if total_monthly_change < max_decrease:
            max_decrease = total_monthly_change
            max_decrease_date = current_date

            # print("max" + str(max_increase))
            # print("min" + str(max_decrease))

            previous_revenue = current_revenue
            avg_change = total_monthly_change / total_months_row
            # print("Average Monthly Change: " + str(avg_change))

    # print the output
print(" ")
print("Financial Analysis")
print("-" * 45)
print("Total Months: " + str(total_months_row))
print("Total Revenue: $" + str(total_revenue))
print("Average Change in Revenue: $" + str(avg_change))
print("Greatest Increase in Revenue: " + str(max_increase_date) + " ($" +
      str(max_increase) + ")")
print("Greatest Decrease in Revenue: " + str(max_decrease_date) + " ($" +
      str(max_decrease) + ")")
print(" ")

#export to text
outputfile = open('budgetanalysis.txt', 'w')
line1 = ('')
line2 = ('Financial Analysis')
line3 = ('Total Months: ' + str(total_months_row))
line4 = ('Total Revenue: $' + str(total_revenue))
line5 = ('Average Change in Revenue: $' + str(avg_change))
line6 = ('Greatest Increase in Revenue: ' + str(max_increase_date) + ' ($' + str(max_increase) + ')')
line7 = ("Greatest Decrease in Revenue: " + str(max_decrease_date) + " ($" +
      str(max_decrease) + ")")
line8 = ('')
outputfile.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7, line8))