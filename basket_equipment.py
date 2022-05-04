tax_for_year = int(input())

shoes = tax_for_year - tax_for_year * 0.4
dress = shoes - shoes * 0.2
ball = dress / 4
accessories = ball / 5

total_price = tax_for_year + shoes + dress + ball + accessories

print(total_price)