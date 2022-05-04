chicken = 10.35
fish = 12.40
vegetarian = 8.15
delivery = 2.50

chicken_p = int(input())
fish_p = int(input())
vegetarian_p = int(input())

main_menu_price = chicken_p * chicken + \
                fish_p * fish + \
                vegetarian_p * vegetarian
desert = main_menu_price * 0.2

total_price = main_menu_price + desert + delivery

print(total_price)