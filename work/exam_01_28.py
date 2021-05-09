import gzip
with gzip.open('data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')