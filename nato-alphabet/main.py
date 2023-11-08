import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

phoetic_dict={row.letter:row.code for (index,row) in data.iterrows()}


def generate_phonetic():
    word=input(str("Enter a word:")).upper()

    try:
        output_list =[phoetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry,only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)
        
generate_phonetic()