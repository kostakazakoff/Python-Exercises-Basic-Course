nylon_sqm = 1.5
paint_l = 14.5
thinner_l = 5.0
bags = 0.4

nylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

materials_sum = (nylon + 2) * nylon_sqm + \
                paint * paint_l * 1.1 + \
                thinner * thinner_l + \
                bags
sallary = materials_sum * 0.3 * work_hours

total_price = materials_sum + sallary

print(total_price)