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
        print(d)
        try:
            total_cost = d['shares']*d['price']
        except ValueError:
            print('Value Error :', row)

    return total_cost
            
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'

total_cost = portfolio_cost(filename)
print('Total cost :',f'{total_cost:10,.2f}')
