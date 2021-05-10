# E:\source\pyqt5\work\exam_02_04.py

import sys
import csv

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
            
