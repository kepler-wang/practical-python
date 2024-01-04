# pcost.py
#
# Exercise 1.27

cost = 0.0

with open("Data/portfolio.csv", "rt") as f:
    headers = next(f)
    for line in f:
        row = line.split(",")
        cost = cost + int(row[1]) * float(row[2])

print("Total cost", cost)
