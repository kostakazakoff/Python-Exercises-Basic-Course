names = input().split(', ')


# define a function, returning the sorted names by length (longest to the shortest order, and alphabetically):
def length_sort(text):
    return -len(text), text


# sorting the names
names.sort(key=length_sort)
print(names)
