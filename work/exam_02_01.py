import sys
import csv

def portfolio_cost(filename):
    total_cost = 0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        t = (row[0], int(row[1]), float(row[2]))
        print(t)
        try:
            total_cost = t[1]*t[2]
        except ValueError:
            print('Value Error :', row)

    return total_cost
            
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'

total_cost = portfolio_cost(filename)
print('Total cost :',total_cost)
