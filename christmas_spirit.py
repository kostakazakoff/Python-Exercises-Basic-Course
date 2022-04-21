quantity = int(input())
days = int(input())
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
day_counter = 0
christmas_spirit = 0
total_cost = 0

while day_counter != days:
    day_counter += 1
    tenth_day = False
    if day_counter % 11 == 0:
        quantity += 2
    if day_counter % 2 == 0:
        total_cost += ornament_set * quantity
        christmas_spirit += 5
    if day_counter % 3 == 0:
        total_cost += (tree_skirt + tree_garlands) * quantity
        christmas_spirit += 13
    if day_counter % 5 == 0:
        total_cost += tree_lights * quantity
        christmas_spirit += 17
        if day_counter % 3 == 0:
            christmas_spirit += 30
    if day_counter % 10 == 0:
        tenth_day = True
        total_cost += tree_skirt + tree_garlands + tree_lights
        christmas_spirit -= 20
if tenth_day:
    christmas_spirit -= 30
print(f'Total cost: {total_cost}')
print(f'Total spirit: {christmas_spirit}')