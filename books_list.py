pages_in_book = int(input())
pages_in_hour = int(input())
days = int(input())

hours_for_book = pages_in_book / pages_in_hour

hours_in_day = hours_for_book // days

print(hours_in_day)