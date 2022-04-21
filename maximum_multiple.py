divisor = int(input())
boundary = int(input())
result = 0
there_is_a_result = False
for n in range(divisor, boundary + 1):
    if n % divisor == 0:
        there_is_a_result = True
        result = n
if there_is_a_result:
    print(result)
