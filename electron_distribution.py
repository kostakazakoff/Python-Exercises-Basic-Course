electrons = int(input())
shell = 0
list_of_shells = []

while electrons > 0:
    shell += 1

    # define electrons in a shell by given formula:
    e_in_shell = 2 * shell ** 2

    # adding the electrons (if enough) to the shells:
    if e_in_shell <= electrons: list_of_shells.append(e_in_shell)

    # adding the left electrons in the last shell:
    else: list_of_shells.append(electrons)
    electrons -= e_in_shell

print(list_of_shells)
