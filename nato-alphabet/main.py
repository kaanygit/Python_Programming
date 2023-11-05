import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

phoetic_dict={row.letter:row.code for (index,row) in data.iterrows()}

word=input(str("Enter a word:")).upper()
output_list =[phoetic_dict[letter] for letter in word]

print(output_list)