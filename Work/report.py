# report.py
#
# Exercise 2.4

import csv
import fileparse


def read_portfolio(filename):
    "Opens a given portfolio file and reads it into a list of dictionaries"
    with open(filename, "rt") as lines:
        return fileparse.parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float]
        )


def read_prices(filename):
    "Reads a set of prices such as this into a dictionary"
    with open(filename, "rt") as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    "takes a list of stocks and dictionary of prices as input and returns a list of tuples"
    report = []
    for stock in portfolio:
        name = stock["name"]
        shares = stock["shares"]
        price = prices[name]
        change = price - stock["price"]
        r = (name, shares, price, change)
        report.append(r)

    return report


def print_report(report):
    "Print out the report"
    headers = ("Name", "Shares", "Price", "Change")
    print(f"%10s %10s %10s %10s" % headers)
    print(("-" * 10 + " ") * len(headers))
    for r in report:
        print("%10s %10d %10.2f %10.2f" % r)


def portfolio_report(portfolio_filename, prices_filename):
    "Make a report and print it"
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report("Data/portfolio.csv", "Data/prices.csv")
