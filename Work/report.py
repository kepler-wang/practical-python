# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    "Opens a given portfolio file and reads it into a list of dictionaries"
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                "name": record["name"],
                "shares": int(record["shares"]),
                "price": float(record["price"]),
            }
            portfolio.append(stock)

    return portfolio


def read_prices(filename):
    "Reads a set of prices such as this into a dictionary"
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


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
