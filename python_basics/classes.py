from random import random


class Animal:

    def __init__(self, animal_type):
        self.animal_type = animal_type

    def make_a_sound(self):
        if self.animal_type == "cat":
            print("meow")
        elif self.animal_type == "dog":
            print("hau")
        else:
            print("Unknown animal")

    def get_weight(self):
        return int(random() * 100)

    def calculate_food(self):
        result = self.get_weight() * 0.02
        return result


cat = Animal("cat")
cat.make_a_sound()
food_needed = cat.calculate_food()
print(f"I need {food_needed}kg food")