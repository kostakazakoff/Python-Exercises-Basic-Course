def change(money):
    money = int(100 * money)
    coins = 0
    coin_value = (200, 100, 50, 20, 10, 5, 2, 1)
    for coin in coin_value:
        coins += money // coin
        money = money % coin
    return coins

m = float(input())
result = change(m)
print(result)
