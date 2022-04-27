count_of_numbers = int(input())


def tribonacci(count):
    # start with a list of 3 integers (to avoid list out of range in first two calculations):
    tribonacci_numbers = [0, 0, 1]
    
    for i in range(count - 1):
        # calculating the next number in the Tribonacci sequence in the count range:
        number = tribonacci_numbers[i] + tribonacci_numbers[i + 1] + tribonacci_numbers[i + 2]
        # appending the next number to the Tribonacci sequence list:
        tribonacci_numbers.append(number)
        
    # creating a list, filtering the zeros (used at the begining):
    tribonacci_numbers = list(filter(lambda x: x != 0, tribonacci_numbers))
    return tribonacci_numbers


result = tribonacci(count_of_numbers)
print(*result)
