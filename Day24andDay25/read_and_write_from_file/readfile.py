file = open("practice.txt")
contents = file.read()
print(contents)
file.close()

# If we do not want to use file.close() function we can use 'with' it will manage directly
with open("practice.txt") as file:
    contents = file.read()
    print(contents)

# if we want to write in a file
with open("practice.txt", mode='w') as file:
    file.write("New text.")

# if we want to append any text in to file the mode = 'a'
with open("practice.txt", mode='a') as file:
    file.write("\nMy name is Manas")

# if the file is not present then it will also create the file
with open("new_file.txt", mode='w') as file:
    file.write("New text.")