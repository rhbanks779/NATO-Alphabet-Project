import pandas 

data = pandas.read_csv("nato_phonetic.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Please enter your name: ").upper()

phonetic_words = [nato_dict[letter] for letter in word]
print(phonetic_words)