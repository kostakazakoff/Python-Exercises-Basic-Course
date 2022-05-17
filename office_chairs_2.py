number_of_rooms = int(input())
chairs = []
difference = []

# creating a list of the rooms with chairs:
for room in range(number_of_rooms):
    chairs.append(list(input().split()))

# creating a list of chair differences (positive - chairs left, negative - chairs not enough):
for i in range(len(chairs)):
    available_chairs = len(chairs[i][0])
    needed_chairs = int(chairs[i][1])
    difference.append(available_chairs - needed_chairs)

# check if they are the not_enough chairs in any of the rooms (negative values):
not_enough = len(list(filter(lambda x: x < 0, difference))) > 0

# printing the result (if there are missing chairs in the rooms):
if not_enough:
    for i in range(len(difference)):
        if difference[i] < 0: print(f'{abs(difference[i])} more chairs needed in room {i + 1}')

# printing the result if the chairs are enough:
else:
    print(f'Game On, {sum(difference)} free chairs left')
