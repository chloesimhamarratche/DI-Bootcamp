#EX1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

mydict = dict(zip(keys, values))

print(mydict)

#EX2
family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

totalcost = 0

for name, age in family.items():

    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    print(f"{name} pays ${price}")
    totalcost += price

print("Total cost:", totalcost)
