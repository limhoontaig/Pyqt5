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
        for k in d:
            print(k,'=',d[k])

    return total_cost, keys
            
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'

total_cost = portfolio_cost(filename)
print('Total cost :',f'{total_cost[0]:10,.2f}')
print('Keys :', total_cost[1])
