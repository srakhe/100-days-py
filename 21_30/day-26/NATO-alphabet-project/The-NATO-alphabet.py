import pandas

# TODO 1: Create a dictionary in this format:
natoDataFrame = pandas.read_csv('nato_phonetic_alphabet.csv')
natoDict = {row.letter: row.code for (index, row) in natoDataFrame.iterrows()}

# TODO 2: Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter your word: ')
for letter in word:
    print(f'{letter} : {natoDict[letter.upper()]}')
