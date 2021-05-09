def portfolio_cost(filename):
    total_cost = 0

    with open('data/portfolio.csv', 'rt') as f:
        headers = next(f).split(',')
        for line in f:
            row = line.split(',')
            try:
                total_cost += int(row[1])*float(row[2])
            except ValueError:
                print("Couldn't Parse", line)
        return total_cost

total_cost = portfolio_cost('data/portfolio.csv')
print('Total cost :',total_cost)