# E:\source\pyqt5\work\exam_02_04.py

import sys
import csv

def read_portfolio(filename):

    types = [str, int, float]
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    row = next(rows)
    types = [str, int, float]
    converted_list = []
    for row in rows:
        converted = []
        converted = [func(val) for func, val in zip(types, row)]
        converted_list.append(converted)
    return converted_list


def portfolio_cost(filename):
    ''' Computes total cost(nshares * price) of a portfolio '''
    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost, keys, keys1, keys2
            
portfolio_list = read_portfolio('data/portfolio.csv')
print(portfolio_list)
