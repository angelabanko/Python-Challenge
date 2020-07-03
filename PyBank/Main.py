# import os  and csv to be able to read csv files
import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname,'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # number of months in the csv
    csv_header = next(csvreader)
    month = []
    value = []
    # net total over the whole period
    for row in csvreader:
        month.append(row[0])
        value.append(int(row[1]))
    listdata = list(csvreader)
    row_count = len(month)
    totalvalue = sum(value)
    print("Finacial Analysis")
    print("---------------------")
    print("Total Months: " + str(row_count))
    print("Total: " + "$" +str(totalvalue))
    
    #average change 
    average =  totalvalue / float(row_count)
    print("Average Change: " + "$" + str(average))

    #greatest increase and decrease of profit

    maxincrease = max(value)
    maxmonth = month[value.index(maxincrease)] 
    print("Greatest Increase in Profits: " + maxmonth + " ($" + str(maxincrease) + ")")

    decrease = min(value)
    decreasemonth = month[value.index(decrease)] 
    print("Greatest Decrease in Profits: " + decreasemonth + " ($" + str(decrease) + ")")
# printing to a text file
    outputfile = open("PyBank_Analysis.txt", "w")
    outputfile.write(("Financial Analysis") +"\n"+
    ("-------------------------") + "\n" +
    ("Total Months: " + str(row_count) + "\n" + 
    ("Total: " + "$" +str(totalvalue)) + "\n" +
    ("Average Change: " + "$" + str(average)) + "\n" +
    ("Greatest Increase in Profits: " + maxmonth + " ($" + str(maxincrease) + ")") + "\n" +
    ("Greatest Decrease in Profits: " + decreasemonth + " ($" + str(decrease) + ")")))
    outputfile.close()




