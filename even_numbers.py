list_of_numbers = list(map(int, input().split(', ')))

# extract the list of even number indexes from the list range:
even_indexes = list(map(lambda x: x if list_of_numbers[x] % 2 == 0 else 'odd', range(len(list_of_numbers))))

# filter the result of indexes (clearing the 'odd' entries):
even_indexes = list(filter(lambda x: x != 'odd', even_indexes))

print(even_indexes)
