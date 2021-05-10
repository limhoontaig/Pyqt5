# C:\source\PyQt5\work\pcost.py

import csv
import sys

def read_portfolio(filename):

    portfolio = []

    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        holding = (row[0], int(row[1]), float(row[2]))
        portfolio.append(holding)
    return(portfolio)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'

total_list = read_portfolio(filename)
print('Total list :',total_list)
        