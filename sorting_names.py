names = input().split(', ')


def length_sort(text):
    return -len(text), text


names.sort(key=length_sort)
print(names)
