import csv

def read_portfolio(filename):

    with open('data/portfolio.csv', 'rt') as f:
        portfolio = []
        headers = next(f)
        for rows in f:
            holding = (row[0], int(row[1]), float(row[2])
            portfolio.append(holding)
        return portfolio

portfolio = read_portfolio('data/portfolio.csv')
print('Total cost :', portfolio)