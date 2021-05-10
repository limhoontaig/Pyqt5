# C:\source\PyQt5\work\pcost.py

import csv
import sys

def read_portfolio(filename):

    portfolio = []

    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        holding = {
            'name':row[0],
            'shares': int(row[1]),
            'price' : float(row[2])
        }            
        portfolio.append(holding)
    total = 0
    for s in portfolio:
        total += s['shares']*s['price']
    return(portfolio, total)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'

portfolio = read_portfolio(filename)
print('Total list :',portfolio[0])
print('Total cost :', portfolio[1])
        