import os

import csv

#Loading CSV file


#* Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

#As an example, your analysis should look similar to the one below:

 
 # Financial Analysis

  #Total Months: 86
 # Total: $38382578
  #Average  Change: $-2315.12
 # Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
 

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Setting CSV path

csvpath = os.path.join( 'Resources', 'budget_data.csv')


# Creating list to store data

changelist= []
monthlist = []

#Creating Varialbes for data set that with initial equal = 0
months = 0
revenue= 0
profit_loss_change = 0
previous_profit_loss = 0
current_profit_loss = 0





#Opening CSV fie and skip the header row

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)
    
   
#Running for Loops in the data set

    for row in csvreader:
        months += 1
#Calculate total amount of revenue over entire period    
        current_profit_loss = int(row[1])
        revenue += current_profit_loss

#Creating if statements
        if(months ==1):
            previous_profit_loss = current_profit_loss
            continue
        else:
            profit_loss_change = current_profit_loss - previous_profit_loss

#Appending varialbe to list
        monthlist.append (row[0])
        changelist.append (profit_loss_change)

#Looping current profit/loss to previous profit/loss
        previous_profit_loss = current_profit_loss

#Calculating average and sum
revenue_sum = sum(changelist)
average_revenue = round (revenue_sum/(months -1),2)

#Calculating highest and lowest increase in profit and months
greatest_increase = max(changelist)
greatest_decrease = min(changelist)

increase_index = changelist.index (greatest_increase)
decrease_index = changelist.index(greatest_decrease)

increase_month = monthlist [increase_index]
decrease_month = monthlist [decrease_index]





#printing analysis to terminal
print("Financial Analysis for")
print ("-------------------------------------------------------")
print(f"Total Months: {months}")
print(f"Total Revenue: ${revenue}")
print(f"Average Revenue Change: ${average_revenue}")
print(f"Greatest Increase in Profit: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profit: {decrease_month} (${greatest_decrease})")

#Saving the output in txt format
output_file = os.path.join('Analysis', 'pybank_data.txt')

#open write file
txtfile = open(output_file, mode = 'w')

#print analysis to file   
txtfile.write("Financial Analysis for \n" ) 
txtfile.write ("-------------------------------------------------------\n")
txtfile.write(f"Total Months: {months} \n")
txtfile.write(f"Total Revenue: ${revenue} \n")
txtfile.write(f"Average Revenue Change: ${average_revenue} \n")
txtfile.write(f"Greatest Increase in Profit: {increase_month} (${greatest_increase}) \n")
txtfile.write(f"Greatest Decrease in Profit: {decrease_month} (${greatest_decrease}) \n")

txtfile.close()