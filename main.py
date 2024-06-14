import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


def generate_phonetic():
    try:
        word = input("Please enter a word: ").upper()
        output = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")  #
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
