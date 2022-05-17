ciphered_message = input()


# define decipher function:
def decipher_message(ciphered_string):
    list_to_decipher = ciphered_string.split()
    ascii_values = []
    characters = []

    for content in list_to_decipher:
        # create a list with the extracted ASCII numbers (strings) from the strings in the source list:
        ascii_values.append(''.join(list(filter(lambda x: str(x).isdigit(), content))))
        # creating a list with the extracted alphabetic characters from the source list:
        characters.append(list(filter(lambda x: str(x).isalpha(), content)))

    # converting ASCII (strings) numbers to integers:
    ascii_characters = list(map(lambda x: chr(int(x)), ascii_values))

    # prepare an empty list for the deciphered result:
    deciphered = []

    # rotate the first and last character places:
    for i in range(len(characters)):
        if len(characters[i]) > 0:
            # create a temp copy of the last character of lists:
            temp_char = characters[i][0]
            # assign the value of last character to the first one:
            characters[i][0] = characters[i][-1]
            # assign value of temp (first character) to the last one:
            characters[i][-1] = temp_char
        # append to decipher a list of strings from the deciphered lists:
        deciphered.append(ascii_characters[i] + ''.join(characters[i]))
    # create a string from list:
    deciphered = ' '.join(deciphered)
    return deciphered


print(decipher_message(ciphered_message))
