#sears.py
bill_thickness = 0.11 * 0.001 # Transform to meter of bill thickness
sears_height = 442 # Height of sears tower is 442M
num_bills = 1
day = 1 
height = 0

while num_bills * bill_thickness < sears_height:
    height += num_bills * bill_thickness
    print(day, num_bills, num_bills * bill_thickness, height)
    
    day = day + 1
    num_bills = num_bills * 2

print("Number of days: ", day)
print('numbers of bills: ', num_bills)
print('Final Height: ', num_bills * bill_thickness)
