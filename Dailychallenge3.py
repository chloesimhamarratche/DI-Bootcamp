#C1
word = input("Enter a word: ")

lettersdic = {}

for index, letter in enumerate(word):

    if letter in lettersdic:
        lettersdic[letter].append(index)
    else:
        lettersdic[letter] = [index]

print(lettersdic)

#C2
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

wallet = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item, price in items_purchase.items():
    cleanprice = int(price.replace("$", "").replace(",", ""))
    
    if cleanprice <= wallet:
        basket.append(item)
        wallet -= cleanprice

if not basket:
    print("Nothing")
else:
    print(sorted(basket))

