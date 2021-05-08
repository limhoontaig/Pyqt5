#sears.py
bill_thickness = 0.11 * 0.001 # Transform to meter of bill thickness
sears_height = 442 # Height of sears tower is 442M
num_bills = 1
tot_bills = 1
day = 1 
height = 0

while tot_bills * bill_thickness < sears_height:
    print(day, num_bills, tot_bills, num_bills * bill_thickness, height)
    num_bills = num_bills * 2
    tot_bills += num_bills
    height = tot_bills * bill_thickness
    day = day + 1

print(day, num_bills, tot_bills, num_bills * bill_thickness, height)
print("Number of days: ", day,'days')
print('Numbers of bills of last day: ', num_bills,'each')
print('Cummulative number of Bills by day:', tot_bills,'each')
print('Final Height: ', tot_bills * bill_thickness,'meters')
