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
            holding = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(holding)

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


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")


total_cost = 0.0
for stock in portfolio:
    total_cost += stock["shares"] * stock["price"]


value = 0.0
for stock in portfolio:
    value += stock["shares"] * prices[stock["name"]]

print("Total cost:", total_cost)
print("Current value:", value)

if value > total_cost:
    print(f"Gain {(value-total_cost):0.2f}")
else:
    print(f"Loss {(total_cost-value):0.2f}")


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


report = make_report(portfolio, prices)
headers = ("Name", "Shares", "Price", "Change")
print(f"%10s %10s %10s %10s" % headers)
print("---------- ---------- ---------- -----------")
for r in report:
    print("%10s %10d %10.2f %10.2f" % r)
