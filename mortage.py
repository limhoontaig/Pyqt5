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
h = ['month','principal','monthly_paid','monthly_rate','monthly_total','cumulative_paid','remain_principal']
print(f'{h[0]:>5s} {h[1]:>12s} {h[2]:>12s} {h[3]:>12s} {h[4]:>12s} {h[5]:>12s} {h[6]:>12s}')

def data_print():
    print(f'{month:>5d} {principal+monthly_paid:>12,.2f} {monthly_paid:>12,.2f} {monthly_rate:>12,.2f} {monthly_paid+monthly_rate:>13,.2f} {total_paid:>15,.2f} {principal:*>16,.2f}')
    return




while principal > 0:
    month +=1
    monthly_rate = principal * rate / 12
    if principal * rate / 12 >=payment:
        print('원금 이자는 ' + str(monthly_rate) + '원으로 상환 예정금액 ' + str(payment) + '원으로는 계약이 되지 않습니다. 상환금액을 올려야만 계약이 가능합니다.')
        break
    else:
        pass

    if principal > payment + extra_payment:
        if month >= extra_payment_start_month and month <= extra_payment_end_month:
            principal = principal * (1+rate/12) - payment - extra_payment
            monthly_paid = payment + extra_payment - monthly_rate
            total_paid += payment + extra_payment
            data_print()

        else:
            principal = principal * (1+rate/12) - payment
            monthly_paid = payment - monthly_rate
            total_paid += payment
            data_print()
    else:
        monthly_paid = principal - monthly_rate
        total_paid += principal + monthly_rate
        principal = 0
        data_print()
print(f'Total paid : {total_paid:>0.2f}')
