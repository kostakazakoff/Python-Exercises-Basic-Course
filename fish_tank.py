l = int(input())
w = int(input())
h = int(input())
percent = float(input()) / 100

tank_volume = l * w * h
volume_in_liters = tank_volume * 0.001
used_volume = volume_in_liters * percent

water = volume_in_liters - used_volume

print(water)