num_of_orders = int(input())
total = 0
for order in range(num_of_orders):
    price = float(input())
    days = int(input())
    capsules = int(input())
    price *= capsules * days
    total += price
    print(f'The price for the coffee is: ${price:.2f}')
print(f'Total: ${total:.2f}')
