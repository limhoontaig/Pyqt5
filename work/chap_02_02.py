# chap 2.2 create a list from a data file
import sys
import csv

def portfolio_list(filename):
    records = []
    total_cost = 0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        records.append((row[0],int(row[1]),float(row[2])))
        try:
            total_cost = int(row[1])*float(row[2])
        except ValueError:
            print('Value Error :', row)
        
    return records, total_cost
            
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'

total = portfolio_list(filename)
print()
print('Total list :', total[0])
print()
print('Total cost :', total[1])
