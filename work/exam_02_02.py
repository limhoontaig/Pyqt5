import sys
import csv

def portfolio_cost(filename):
    total_cost = 0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        d = {
            'name' : row[0],
            'shares' : int(row[1]),
            'price' : float(row[2])
        }
        try:
            total_cost = d['shares']*d['price']
        except ValueError:
            print('Value Error :', row)
        keys = list(d)
        keys1 = []
        for k in d:
            keys1.append(k)
        keys2 = d.keys()

    return total_cost, keys, keys1, keys2
            
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'

total_cost = portfolio_cost(filename)
print('Total cost :',f'{total_cost[0]:10,.2f}')
print('keys = list(d):',total_cost[1])
print('for keys1 in d:', total_cost[2])
print('keys2 = d.keys():',total_cost[3])
