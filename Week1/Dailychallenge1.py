string= input("Enter a string with exactly 10 characters long:")

if len(string)<10:
    print("String is not long enough.")

elif len(string)>10:
    print("String is too long.")

else:
    print("Perfect string")

#firstcharacter
print("First character:", string[0])
#lastcharacter
print("Last character:", string[-1])

for i in range(len(string)):
    print(string[:i+1])
    