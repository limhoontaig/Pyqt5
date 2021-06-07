# E:\source\pyqt5\sears.py


class Sears:
    def __init__(self):
        self.bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
        self.sears_height   = 542             # Height (meters)
        self.num_bills      = 1
        self.tot_bills = 1
        self.day            = 1
        self.sears_compute = []

    def sears():
        while self.tot_bills * self.bill_thickness < self.sears_height:
            self.sears.compute.append(f'{day:>4d} {num_bills:>10d} {tot_bills:>10d} {tot_bills * bill_thickness:10.2f}')
            day = day + 1
            num_bills = num_bills * 2
            tot_bills += num_bills
        return self.sears_compute


    def report(sears):
        print('---------------------------- ----------')
        print('Number of days             :', f'{day:>10d}')
        print('Number of bills of last day:', f'{num_bills:>10d}')
        print('Total Number of bills      :', f'{tot_bills:>10d}')
        print('Final height               :', f'{tot_bills * bill_thickness:>10.2f}')
        print('**************************** **********')

calculation = Sears.sears()

Sears.report(calculation)
