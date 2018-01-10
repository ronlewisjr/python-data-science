# 1 - lists
# order is important, change
odds = [5, 7, 9]
sum(odds)
total = 0
for num in odds:
    total = total + num
    # total += num

total = 0
for i, num in enumerate(odds):
    total = total + (i * num)

sqareroots = [n**0.5 for n in odds]
cuberoots = [n**(1 / 3) for n in odds]
divisbleby5 = [n**(1 / 3) for n in range(31) if n % 5 == 0]
list(map(lambda n: n**(1 / 3), odds))
list(filter(lambda n: n < 5, [3, 4, 5, 6, 7]))
from functools import reduce
reduce(lambda total, n: total * n, odds, 1)

# 2 - tuple
# order is good, immutable
tup1 = (3, 4)

# 3 - sets
# no order, iterable, unique, mutable, only takes immutable/hashable values
s1 = {3, 4}

# 4 - dicts
# no order, iterable, unique keys (only), keys hashable/immutable (only)

d = {}
for n in range(5):
    d[n] = n**2
d.get(5, 'default')

{n: n**0.5 for n in range(50) if n % 10 == 0}
[(n, n**0.5) for n in range(50) if n % 10 == 0]