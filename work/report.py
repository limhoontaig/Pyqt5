# C:\source\PyQt5\work\pcost.py

import csv

def read_portfolio(filename):

    portfolio = []

    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        holding = (row[0], int(row[1]), float(row[2]))
        portfolio.append(holding)
    return(portfolio)

def total_cost(portfolio):
    
    total = 0 
    for name, shares, price in portfolio:
        total += shares * price
    return total


portfolio = read_portfolio('data/portfolio.csv')
total = total_cost(portfolio)
print(total)