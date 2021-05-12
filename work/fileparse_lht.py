# C:\source\PyQt5\work\fileparse_lht.py

import csv

def parse_csv(filename):
    '''
    Parse a CSV file into a list of records with type conversion
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers (if any)
        headers = next(rows)
        
        records = []
        for row in rows:
            if not row:    # skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
