s = input("Enter a string: ")

done = ""

for ch in s:
    if ch not in done:
        count = 0
        for x in s:
            if ch == x:
                count += 1
        print(ch, ":", count)
        done += ch