# E:\source\pyqt5\mortage.py

principal = 500000.0
rate = 0.05
payment = 2684.11

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0
monthly_paid = 0
total_paid = 0.0
month = 0
h = ['month','principal','monthly_paid','monthly_rate','monthly_total','total_paid','remain_principal']
print(f'{h[0]:>5s} {h[1]:>12s} {h[2]:>12s} {h[3]:>12s} {h[4]:>12s} {h[5]:>12s} {h[6]:>12s}')

while principal > 0:
    month +=1
    monthly_rate = principal * rate / 12
    if principal > payment + extra_payment:
        if month >= extra_payment_start_month and month <= extra_payment_end_month:
            principal = principal * (1+rate/12) - payment - extra_payment
            monthly_paid = payment + extra_payment - monthly_rate
            total_paid += payment + extra_payment
            print(f'{month:>5d} {principal+monthly_paid:>12.2f} {monthly_paid:>12.2f} {monthly_rate:>12.2f} {monthly_paid+monthly_rate:>13.2f} {total_paid:>12.2f} {principal:>16.2f}')

        else:
            principal = principal * (1+rate/12) - payment
            monthly_paid = payment - monthly_rate
            total_paid += payment
            print(f'{month:>5d} {principal+monthly_paid:>12.2f} {monthly_paid:>12.2f} {monthly_rate:>12.2f} {monthly_paid+monthly_rate:>13.2f} {total_paid:>12.2f} {principal:>16.2f}')
    else:
        monthly_paid = principal - monthly_rate
        total_paid += principal + monthly_rate
        principal = 0
        print(f'{month:>5d} {principal+monthly_paid:>12.2f} {monthly_paid:>12.2f} {monthly_rate:>12.2f} {monthly_paid+monthly_rate:>13.2f} {total_paid:>12.2f} {principal:>16.2f}')
print('Total paid', f'{total_paid:>12.2f}')
