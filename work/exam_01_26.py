with open('./work/data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    print(headers)
    for line in f:
        row = line.split(',')
        print(row, end='')


