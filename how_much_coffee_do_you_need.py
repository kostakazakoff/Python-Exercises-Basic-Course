command = input()
coffees = 0
options = ['coding', 'dog', 'cat', 'movie']
while command != 'END':
    if coffees >= 5:
        print('You need extra sleep')
        exit()
    for var in options:
        if command.lower() == var:
            coffees += 1
            if command.isupper():
                coffees += 1
    command = input()
print(coffees)