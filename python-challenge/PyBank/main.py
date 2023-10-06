# Imports

import csv
import os

# reading

with open('./Resources/budget_data.csv', 'r') as file:
    csv_reader = csv.reader(file)


    
    newrow = next(csv_reader)
    newrow2 = next(csv_reader)
    cellCount = 1
    totals = int(newrow2[1])
    difference = int(newrow2[1])
    avList = []



    
    
    for row in csv_reader:

        cellCount = cellCount + 1

        totals = totals + int(row[1]) 

        change =int(row[1]) - difference
        avList = avList + [change]
        difference = int(row[1])    
        
    
    avDif = sum(avList)/len(avList)
    
    print ('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {cellCount}')
    print(f'Total: {totals}')
    print(f'Average Change: {round(avDif, 2)}')
    print(f'Greatest Increase in Profits: {max(avList)}')
    print(f'Greatest Decrease in Profits: {min(avList)}')
   
