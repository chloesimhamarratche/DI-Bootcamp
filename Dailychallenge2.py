#Challenge1

number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

multiples = []

for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)

#Challenge2
word = input("Enter a word: ")

newword = ""

for letter in word:
    if newword == "" or letter != newword[-1]:
        newword += letter

print(newword)
