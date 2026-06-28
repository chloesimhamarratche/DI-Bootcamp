# ============================================================
# Exercise 1 : Pets
# ============================================================

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Siamese(Cat):
    pass


all_cats = [
    Bengal("Milo", 3),
    Chartreux("Luna", 5),
    Siamese("Simba", 2)
]

sara_pets = Pets(all_cats)

print("===== Exercise 1 : Pets =====")
sara_pets.walk()
print()



# ============================================================
# Exercise 2 : Dogs
# ============================================================

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} won the fight"
        elif other_power > my_power:
            return f"{other_dog.name} won the fight"
        else:
            return "It's a tie"


dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 25)
dog3 = Dog("Max", 4, 18)

print("===== Exercise 2 : Dogs =====")
print(dog1.bark())
print(f"{dog1.name}'s run speed is {dog1.run_speed()}")
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print()



# ============================================================
# Exercise 3 : Dogs Domesticated
# ============================================================

import random


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [self.name]

        for dog in args:
            dog_names.append(dog.name)

        return f"{', '.join(dog_names)} all play together"

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]

            trick = random.choice(tricks)
            print(f"{self.name} {trick}")
        else:
            print(f"{self.name} is not trained yet")


my_dog = PetDog("Fido", 2, 10)
my_other_dog = PetDog("Buddy", 4, 15)
my_third_dog = PetDog("Max", 3, 12)

print("===== Exercise 3 : Dogs Domesticated =====")
my_dog.train()
print(my_dog.play(my_other_dog, my_third_dog))
my_dog.do_a_trick()
print()



# ============================================================
# Exercise 4 : Family and Person Classes
# ============================================================

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print(
                        f"You are over 18, your parents Jane and John accept that you will go out with your friends"
                    )
                else:
                    print("Sorry, you are not allowed to go out with your friends")
                return

        print(f"{first_name} is not in the family")

    def family_presentation(self):
        print(f"Family name: {self.last_name}")

        for person in self.members:
            print(f"{person.first_name} {person.last_name}, age: {person.age}")


print("===== Exercise 4 : Family and Person Classes =====")

my_family = Family("Cohen")

my_family.born("Sarah", 22)
my_family.born("David", 15)
my_family.born("Lea", 18)

my_family.family_presentation()
print()

my_family.check_majority("Sarah")
my_family.check_majority("David")
my_family.check_majority("Lea")
