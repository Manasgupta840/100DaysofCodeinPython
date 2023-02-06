import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(letter_dict)


def phonetic_name(name):
    result = [letter_dict.get(letter.upper()) for letter in name]
    print(result)


phonetic_name("Manas")
