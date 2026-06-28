# ============================================================
# Exercise 1 : Cats
# ============================================================

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


def find_oldest_cat(cat1, cat2, cat3):
    oldest_cat = cat1

    if cat2.age > oldest_cat.age:
        oldest_cat = cat2

    if cat3.age > oldest_cat.age:
        oldest_cat = cat3

    return oldest_cat


# Create 3 cat objects
cat1 = Cat("Mimi", 3)
cat2 = Cat("Luna", 7)
cat3 = Cat("Simba", 5)

# Find and print the oldest cat
oldest_cat = find_oldest_cat(cat1, cat2, cat3)

print("===== Exercise 1 : Cats =====")
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
print()



# ============================================================
# Exercise 2 : Dogs
# ============================================================

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")


# Create dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 40)

print("===== Exercise 2 : Dogs =====")

# Print details
print(f"David's dog is called {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"Sarah's dog is called {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# Compare dog sizes
if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"The bigger dog is {sarahs_dog.name}.")
else:
    print("Both dogs have the same height.")

print()



# ============================================================
# Exercise 3 : Who's the song producer?
# ============================================================

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


print("===== Exercise 3 : Song =====")

stairway = Song([
    "There's a lady who's sure",
    "All that glitters is gold",
    "And she's buying a stairway to heaven"
])

stairway.sing_me_a_song()
print()



# ============================================================
# Exercise 4 : Afternoon at the Zoo
# ============================================================

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}

        for animal in sorted_animals:
            first_letter = animal[0].upper()

            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []

            grouped_animals[first_letter].append(animal)

        return grouped_animals

    def get_groups(self):
        grouped_animals = self.sort_animals()

        print("Grouped animals:")
        for letter, animals in grouped_animals.items():
            print(f"{letter}: {animals}")


print("===== Exercise 4 : Zoo =====")

# Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Add animals
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Zebra")

# Display animals
brooklyn_safari.get_animals()
print()

# Sell one animal
brooklyn_safari.sell_animal("Bear")

# Display animals after selling
print("After selling Bear:")
brooklyn_safari.get_animals()
print()

# Sort and group animals
brooklyn_safari.get_groups()
print()



# ============================================================
# Bonus : Add multiple animals at once
# ============================================================

class ZooBonus:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}

        for animal in sorted_animals:
            first_letter = animal[0].upper()

            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []

            grouped_animals[first_letter].append(animal)

        return grouped_animals

    def get_groups(self):
        grouped_animals = self.sort_animals()

        print("Grouped animals:")
        for letter, animals in grouped_animals.items():
            print(f"{letter}: {animals}")


print("===== Bonus : Zoo with multiple animals =====")

bonus_zoo = ZooBonus("Bonus Safari")

bonus_zoo.add_animal("Giraffe", "Bear", "Baboon", "Cougar", "Cat", "Lion", "Zebra")
bonus_zoo.get_animals()
print()

bonus_zoo.get_groups()