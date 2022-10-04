student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)
# student_data_frame = pandas.DataFrame(student_dict)


# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter Name: ")
name_letter = [letter.upper() for letter in name]
name_nato = {letter: nato_dict[letter] for letter in name_letter}
print(name_nato)
