# pcost.py

import report
import sys


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    portfolio = report.read_portfolio(filename)
    return sum([s.shares * s.price for s in portfolio])


def main(args):
    filename = args[1]
    print("Total cost:", portfolio_cost(filename))


if __name__ == "__main__":
    main(sys.argv)
