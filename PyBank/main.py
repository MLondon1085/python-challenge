import os
import csv

PyBank_csv_path = os.path.join('..', 'PyBank', 'budget_data.csv')

# with open(PyBank_csv_path, 'r') as text:
#     print(text)
#     lines = text.read()
#     print(lines)

with open(PyBank_csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader, none)

    # total_months=0
    # total_revenue=0
    # revenue_change=[]
    # prev_revenue=0
    
    # for row in csvreader:
    #     total_months=total_months+1
    #     total_revenue=total_revenue+int(row[1])    
    #     monthly_diff=int(row[1])-prev_revenue
    #     revenue_change.append(monthly_diff)
    #     prev_revenue=int(row[1])

    for row in csvreader:
       all_months.append(row[0])
       pl.append(row[1])

#count total no of months
total_month = len(all_months)

#total net profit and loss
net_pl = sum(pl)

#avg revenue
avg_rev = round(net_pl/total_month, 2)

   #max increase and decrease

max_profit=pl[0]
min_profit=pl[0]

for x in range(len(pl)):
    if pl[x]> max_profit:
        max_profit=pl[x]
        max_profit_month=all_month[x]
        
    elif pl[x]<min_profit:
        min_profit=pl[x]
        min_profit_month=all_month[x]


print ("Financial Analysis")
print("----------------------------------")
print("Total No of Months:" + str(total_month))
print("Net Profit and Loss:" + str(net_pl))
print("Average Change in P/L:" + str(avg_rev))
print ("Maximum Profit:" + str(max_profit)+" " + "Month:" + " " +str(max_profit_month))
print ("Minimum Profit:" + str(min_profit) + " " +"Month:"+" "+ str(min_profit_month))


for x in range():