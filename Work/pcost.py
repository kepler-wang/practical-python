# pcost.py

import sys
from report import read_portfolio


def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    return sum(stock["price"] * stock["shares"] for stock in portfolio)


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Enter a filename:")

cost = portfolio_cost(filename)
print("Total cost:", cost)
