# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0
extra_months = 12
months = 0

while principal > 0:
    months = months + 1
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    if principal < payment:
        total_paid = total_paid + principal
        break

    print(months, round(total_paid, 2), round(principal, 2))

print("Total paid", round(total_paid, 2), "over", months, "months")
