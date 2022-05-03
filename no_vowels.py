text = input()
text = list(text)
vowels = ['a', 'o', 'u', 'e', 'i']

text = ''.join(list(filter(lambda x: x.lower() not in vowels, text)))

print(text)
