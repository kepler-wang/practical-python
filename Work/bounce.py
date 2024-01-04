# bounce.py
#
# Exercise 1.5

height = 100.0
bounces = 0

while bounces < 10:
    height = height * (3 / 5)
    bounces = bounces + 1
    print(bounces, round(height, 4))
