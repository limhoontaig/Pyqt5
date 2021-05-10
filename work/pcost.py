# C:\source\PyQt5\work\pcost.py

def portfolio_cost(filename):

    total_cost = 0

    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        for line in f:
            row = line.split(',')
            try:
                total_cost += int(row[1])*float(row[2])
            except ValueError:
                print("Couldn't Parse", line)
    return(total_cost)

cost = portfolio_cost('data/portfolio.csv')
print('Total cost :',cost)

        