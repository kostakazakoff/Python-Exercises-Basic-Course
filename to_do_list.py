command = input()
notes = []

# creating a matrix (list of notes with a priority) - for example [['2', 'note'], ['1', 'note']...]:
while command != 'End':
    # creating a list (priority and note)
    command = command.split('-')
    # appending the note to the notes matrix
    notes.append(command)
    command = input()

# sorting the notes (matrix) by the priority (first column in any row):
for i in range(len(notes)):
    # compare each notes' priority (first column value) from the beginning to the current (index i) note:
    for j in range(i):
        # if the priority is higher (lower value in the integer in first column):
        if int(notes[i][0]) < int(notes[j][0]):
            # insert a note to the right place (before the note with a bigger priority value):
            notes.insert(j, notes[i])
            # clear the note from the previous position:
            notes.pop(i + 1)

# extracting the second row content and creating the already sorted to_do_list:
to_do_list = [row[1] for row in notes]
print(to_do_list)
