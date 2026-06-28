# ============================================================
# Daily Challenge : Old MacDonald's Farm
# ============================================================

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        output = f"{self.name}'s farm\n\n"

        for animal, count in self.animals.items():
            output += f"{animal:<10}: {count}\n"

        output += "\n    E-I-E-I-O!"
        return output

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animals_sentence = []

        for animal in animal_types:
            count = self.animals[animal]

            if count > 1:
                animals_sentence.append(animal + "s")
            else:
                animals_sentence.append(animal)

        if len(animals_sentence) == 1:
            animals_text = animals_sentence[0]
        elif len(animals_sentence) == 2:
            animals_text = animals_sentence[0] + " and " + animals_sentence[1]
        else:
            animals_text = ", ".join(animals_sentence[:-1])
            animals_text += " and " + animals_sentence[-1]

        return f"{self.name}'s farm has {animals_text}."

    def add_animals(self, **kwargs):
        for animal_type, count in kwargs.items():
            self.add_animal(animal_type, count)


# ============================================================
# Test the code
# ============================================================

macdonald = Farm("McDonald")

macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)

print(macdonald.get_info())

print()
print("Animal types:")
print(macdonald.get_animal_types())

print()
print(macdonald.get_short_info())

print()
print("After adding multiple animals:")

macdonald.add_animals(cow=5, sheep=2, goat=12)

print(macdonald.get_info())