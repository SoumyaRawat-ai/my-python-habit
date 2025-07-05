import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

data_dic = {row.letter:row.code for index, row in data.iterrows()}
def gernerate_phonetic():
    try:
        enter = input('enter a word').upper()
        output_list = [data_dic[letter] for letter in enter]

    except KeyError:
        print('Sorry, only letter in the alphabet please.')
        gernerate_phonetic()
    else:print(output_list)

gernerate_phonetic()