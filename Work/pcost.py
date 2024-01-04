# pcost.py
#
# Exercise 1.27

import sys


def portfolio_cost(filename):
    cost = 0.0

    with open(filename, "rt") as f:
        headers = next(f)
        try:
            for line in f:
                row = line.split(",")
                cost = cost + int(row[1]) * float(row[2])
        except ValueError:
            print("Missing data!")

    return cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)
