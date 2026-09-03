info = input("Enter additional information: ")

with open("student.txt", "a") as file:
    file.write(info + "\n")

print("Information appended successfully.")
