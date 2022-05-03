names = input().split(', ')


# define a function, returning the parameters (string length and string) for sorting:
def length_alphabetic(text):
    return -len(text), text


# sorting the list of names
names.sort(key=length_alphabetic)
print(names)
