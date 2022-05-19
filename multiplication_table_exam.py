import random
answer = ''
want_to_play = True
right = 0
wrong = 0

# game continue while the bool 'want_to_play' is True:
while want_to_play:
    numbers = []
    
    # generating 2 random numbers (from 1 to 9): =================================
    for i in range(2):
        numbers.append(random.randrange(1, 10))
    
    # waiting for the answer: ====================================================
    print(f'What is the result of the multiplication: {numbers[0]}*{numbers[1]}?')
    answer = input('Enter the right answer \'Stop\' for exit: ')
    
    # check the answer (if 'Stop', exit the game: ================================
    if answer != 'Stop':
        if int(answer) == numbers[0] * numbers[1]:
            right += 1
            print('Right answer!')
        else:
            wrong += 1
            print('Wrong answer!')
            
    # printing the number of right and wrong answers and defining the bool 'want_to_play':
    else:
        print()
        print(f'You've got {right} right and {wrong} wrong answers.')
        want_to_play = False
