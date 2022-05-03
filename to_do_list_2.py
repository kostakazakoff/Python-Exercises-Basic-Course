command = input()
# create an empty notes list:
notes = [0] * 10

while command != 'End':
    # create a tokens from the command (list of priority and note):
    token = command.split('-')
    priority = int(token[0]) - 1
    note = token[1]
    # insert the notes in their right places:
    notes.pop(priority)
    notes.insert(priority, note)
    command = input()

# filtering notes by removing zeros:
to_do_list = [x for x in notes if x != 0]
print(to_do_list)
