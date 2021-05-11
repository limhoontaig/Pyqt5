# E:\source\pyqt5\work\exam_02_26.py

import sys
import csv
from pprint import pprint

def dict_portfolio(filename):

    types = [str,float,str,str,float,float,float,float,int]
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    row = next(rows)
    d_list = []

    for row in rows:
        converted = [func(val) for func, val in zip(types, row)]
        record = dict(zip(headers, converted))
        d_list.append(record)
    return d_list


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
            
portfolio_dict = dict_portfolio('data/dowstocks.csv')
pprint(portfolio_dict)
