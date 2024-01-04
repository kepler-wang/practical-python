# pcost.py
#
# Exercise 1.27

import sys
import csv


def portfolio_cost(filename):
    cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(f)
        for rowno, row in enumerate(rows, start=1):
            try:
                cost += int(row[1]) * float(row[2])
            except ValueError:
                print(f"Row {rowno}: Bad row: {row}")
    return cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)
