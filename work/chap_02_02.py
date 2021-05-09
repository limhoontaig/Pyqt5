import sys
import csv

def portfolio_cost(filename):
    records = []
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        records.append((row[0],int(row[1]),float(row[2])))
        # try:
        #     total_cost = d['shares']*d['price']
        # except ValueError:
        #     print('Value Error :', row)
        
    return records
            
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'

total_list = portfolio_cost(filename)
print('Total lost :', total_list)
