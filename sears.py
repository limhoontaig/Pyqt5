# E:\source\pyqt5\sears.py

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 542             # Height (meters)
num_bills      = 1
tot_bills = 1
day            = 1

while tot_bills * bill_thickness < sears_height:
    print(f'{day:>4d} {num_bills:>10d} {tot_bills:>10d} {tot_bills * bill_thickness:10.2f}')
    day = day + 1
    num_bills = num_bills * 2
    tot_bills += num_bills
print('---------------------------- ----------')
print('Number of days             :', f'{day:>10d}')
print('Number of bills of last day:', f'{num_bills:>10d}')
print('Total Number of bills      :', f'{tot_bills:>10d}')
print('Final height               :', f'{tot_bills * bill_thickness:>10.2f}')
print('**************************** **********')