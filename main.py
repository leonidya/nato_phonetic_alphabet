import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_name = input("Enter a word: ").upper()
user_name = [letter for letter in user_name]


def convert_names(user_name):
    list_of_codes = [nato_dict[letter] for letter in user_name]
    return list_of_codes


print(convert_names(user_name))
