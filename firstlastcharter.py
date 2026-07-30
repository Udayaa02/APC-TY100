s = input("Enter a string: ")

count = 0
for i in s:
    count += 1

if count == 0:
    print("String is empty.")
else:
    print("First character:", s[0])
    print("Last character:", s[count - 1])