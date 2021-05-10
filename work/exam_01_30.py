import csv


def portfolio_cost(filename):
    ''' computes a total cost(shares*price) of a portfolio file'''
    total_cost = 0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
        return total_cost

total_cost = portfolio_cost('data/portfolio.csv')
print('Total cost :',total_cost)