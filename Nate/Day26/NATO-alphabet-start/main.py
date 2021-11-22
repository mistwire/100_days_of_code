
import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

input_value = input("Word to convert: ").upper()
output_value = [nato_dict[letter] for letter in input_value]

print(output_value)


