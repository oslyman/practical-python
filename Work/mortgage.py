# mortgage.py
#
# Exercises 1.7-11, 1.18

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    monthly_payment = payment
    if month >= extra_payment_start_month and month < extra_payment_end_month:
        monthly_payment += extra_payment
    month += 1
    if monthly_payment > principal:
        total_paid += principal
        principal = 0
        print(f'{month} {round(total_paid, 2):6.2f} {round(principal, 2):6.2f}')
        break

    principal = principal * (1+rate/12) - monthly_payment
    total_paid = total_paid + monthly_payment
    print(f'{month} {round(total_paid, 2):6.2f} {round(principal, 2):6.2f}')

print(f'Total paid {round(total_paid, 2):6.2f}')
print(f'Total months {month}')
