# pcost.py

import sys
from . import report


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost


def main(args):
    filename = args[1]
    print("Total cost:", portfolio_cost(filename))


if __name__ == "__main__":
    main(sys.argv)
