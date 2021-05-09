total_cost = 0

with open('data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    print(headers)
    for line in f:
        row = line.split(',')
        try:
            total_cost += int(row[1])*float(row[2])
            print(row, end='')
        except ValueError:
            print("Couldn't Parse", line)
    print()
    print(total_cost)
