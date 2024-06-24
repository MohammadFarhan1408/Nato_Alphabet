import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

alphabetic_data = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_word():
    word = input("Enter the Name: ").upper()
    try:
        final_letter = [alphabetic_data[letter] for letter in word]
    except KeyError:
        print("Sorry, Not a valid alphabet")
        generate_word()
    else:
        print(final_letter)


generate_word()
