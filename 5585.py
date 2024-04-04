coins = [500, 100, 50, 10, 5, 1]
count = 0

_sum = int(input())

for coin in coins:
    change = _sum % coin
    count += _sum // coin

print(count)