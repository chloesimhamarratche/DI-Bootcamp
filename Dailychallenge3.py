
word = input("Enter a word: ")

lettersdic = {}

for index, letter in enumerate(word):

    if letter in lettersdic:
        lettersdic[letter].append(index)
    else:
        lettersdic[letter] = [index]

print(lettersdic)
