text = input().split()
palindrome = input()
palindromes_list = []

for word in text:
    if word == ''.join(reversed(word)):
        palindromes_list.append(word)

palindrome_count = palindromes_list.count(palindrome)
print(palindromes_list)
print(f'Found palindrome {palindrome_count} times')
