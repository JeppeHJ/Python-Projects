import pandas


letter_data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dictionary = {row.letter: row.code for (index, row) in letter_data.iterrows()}

def generate_phonetic():
    name = input("Enter your name ").upper()
    try:
        conversion = [new_dictionary[n] for n in name]
        print(conversion)
    except KeyError:
        print("Only letters of the alphabet, please")
        generate_phonetic()

generate_phonetic()
