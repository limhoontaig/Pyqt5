with open('data/portfolio.csv', 'rt') as f:
    headers = next(f)
    print(headers)
    for line in f:
       print(line, end='')


