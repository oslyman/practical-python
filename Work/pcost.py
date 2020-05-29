# pcost.py
#
# Exercise 1.27, 1.30-3
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for r in rows:
            try:
                total_cost += float(r[1]) * float(r[2])
            except ValueError:
                print("WARN: the csv file is missing a value, skipping this row")
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print(f'Total cost {round(cost, 2):0.2f}')