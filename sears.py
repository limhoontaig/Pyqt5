# E:\source\pyqt5\sears.py

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
tot_bills = 1
day            = 1

while tot_bills * bill_thickness < sears_height:
    print(f'{day:>4d} {num_bills:>10d} {tot_bills:>10d} {tot_bills * bill_thickness:10.2f}')
    day = day + 1
    num_bills = num_bills * 2
    tot_bills += num_bills

print('Number of days       ', day)
print('Number of bills      ', num_bills)
print('Total Number of bills', tot_bills)
print('Final height         ', tot_bills * bill_thickness)