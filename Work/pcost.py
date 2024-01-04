# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    cost = 0.0

    with open(filename, "rt") as f:
        headers = next(f)
        for line in f:
            row = line.split(",")
            cost = cost + int(row[1]) * float(row[2])

    return cost


cost = portfolio_cost("Data/portfolio.csv")
print("Total cost:", cost)
