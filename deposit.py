deposit = float(input())
deposit_time = int(input())
deposit_interest = float(input()) /100

for_month = deposit * deposit_interest / 12
for_period = deposit + deposit_time * for_month

print(for_period)