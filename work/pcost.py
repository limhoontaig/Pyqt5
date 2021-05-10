# C:\source\PyQt5\work\pcost.py

import csv

def portfolio_cost(filename):

    total_cost = 0

    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        try:
            total_cost += int(row[1])*float(row[2])
        except ValueError:
            print("Couldn't Parse", row)
    return(total_cost)

cost = portfolio_cost('data/portfolio.csv')
print('Total cost :',cost)

        