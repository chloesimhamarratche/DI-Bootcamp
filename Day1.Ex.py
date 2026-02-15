#EX1
print("Hello world\nHello world\nHello world\nHello world")

#EX2
ex2= (99**3)*8
print(ex2)


#EX3
print(5<3) #False
print(3==3) #True
print(3=="3") #False
#print("3">3) #Error
print("Hello"=="hello") #False


#EX4
computer_band= "Apple"
print("I have a" ,computer_band, "computer")


#EX5
name= "Chloe Simha"
age= 22
shoe_size= 39
info= f"My name is {name}, i am {age} and my shoe size is {shoe_size}."
print(info)


#EX6
a=8
b=2
if a>b:
    print("Hello world")


#EX7
number= int(input("Enter a number:"))
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")


#EX8
myname= "Chloe Simha"
username= input("What's your name?")
if myname == username:
    print("No way, we have the same name !")
else: 
    print(f"Nice to meet you {username} !")


#EX9
userheight= int(input("What's your height in centimeters ?"))
if userheight >=145:
    print("You are tall enough to ride !")
else: 
    print("You need to grow some more to ride...")
