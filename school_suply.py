pencil_pack = 5.8
marker_pack = 7.2
liter_detergent = 1.2

pencil_quantity = int(input())
marker_quantity = int(input())
detergent_quantity = int(input())
discount = int(input()) / 100

price = pencil_quantity * pencil_pack + \
        marker_quantity * marker_pack + \
        detergent_quantity * liter_detergent
discount_sum = price * discount

total_price = price - discount_sum

print(total_price)