
PLACEHOLDER = "[name]"

with open("persons_names.txt") as names_file:
    names = names_file.readlines()

with open("letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter =  letter_content.replace(PLACEHOLDER, stripped_name)
        with open("ready_made_letter.txt", mode='a') as new_lett:
            new_lett.write(new_letter)
