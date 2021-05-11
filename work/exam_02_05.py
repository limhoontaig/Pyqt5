import csv

def read_portfolio(filename):

    portfolio = []
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        holding = {
            'name':row[0],
            'shares':int(row[1]),
            'price':float(row[2])
        }
        portfolio.append(holding)
    return portfolio

portfolio = read_portfolio('data/portfolio.csv')
print('Total cost :', portfolio)