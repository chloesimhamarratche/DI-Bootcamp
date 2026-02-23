#EX1
myfavnumbers= {2,4,6}

myfavnumbers.add(7)
myfavnumbers.add(8)

myfavnumbers.remove(8)

friendfavnumbers= {1,3,5}

ourfavnumbers= myfavnumbers.union(friendfavnumbers)

print(f"My fav numbers are : ",myfavnumbers)
print(f"My friend's fav numbers are : ",friendfavnumbers)
print(f"Our fav numbers are : " ,ourfavnumbers)

#EX2
mytuple= (1,2,3)
mytuple= mytuple + (4,5,6)
print(mytuple)

#EX3
basket= ["banana", "apples", "oranges", "blueberries"]

basket.remove("banana")
basket.remove("blueberries")

basket.append("kiwi")

basket.insert(0,"apples")

countapples= basket.count("apples")
print(f"Number of apples : " , countapples)

basket.clear()

print(f"Final basket : ", basket)

#EX4
numbers= []

for i in range(2,6):
    numbers.append(i-0.5)
    numbers.append(i)

print(numbers)

#EX5
for i in range(1,21):
    print(i)

for i in range(1,21):
    if i % 2 == 0:
        print(i)

#EX6
while True:
    name= input("Enter your name")

    if name.isdigit() or len(name) < 3:
        print("give the correct name:")
    else:
        print("Thank you")

#EX7
fruits = input("Enter your favorite fruits (separated by spaces): ").split()

choice = input("Enter the name of any fruit: ")

if choice in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")











