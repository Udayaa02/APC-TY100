s = input("Enter a string: ")

vowels = consonants = digits = spaces = special = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        consonants += 1
    elif '0' <= ch <= '9':
        digits += 1
    elif ch == ' ':
        spaces += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special)