old_version = list(map(int, input().split('.')))
# creating an integer by the values in version (for example - [1, 2, 3] = 123) and increasing with 1
# The result is the next version list:
next_version = [x for x in str(old_version[0] * 100 + old_version[1] * 10 + old_version[2] + 1)]
print('.'.join(next_version))
