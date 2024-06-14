import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

alphabetic_data = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter the Name: ").upper()
final_letter = [alphabetic_data[letter] for letter in word]
print(final_letter)
