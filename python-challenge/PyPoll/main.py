# Imports

import csv
import os

# reading

with open('./Resources/election_data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    newrow = next(csv_reader)
    newrow2 = next(csv_reader)
    cellCount = 1
    counter = 0
    vCounter1 = 0
    vCounter2 = 0
    vCounter3 = 0

    for row in csv_reader:

        cellCount = cellCount + 1



    print ('Election Results')
    print('----------------------------')
    print(f'Total Votes: {cellCount}')
    print('----------------------------')
    print()