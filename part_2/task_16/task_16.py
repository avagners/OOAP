from typing import List


class Animal:
    def make_sound(self):
        print("Animal is making a sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof woof")


class Cat(Animal):
    def make_sound(self):
        print("Meow meow")


# функция является ковариантной, поскольку входным аргументом animals является
# список объектов Animal, но она может принимать список любых подклассов,
# таких как Dog и Cat
def make_animals_sound(animals: List[Animal]):
    for animal in animals:
        animal.make_sound()


# метод make_sound является полиморфным, поскольку он определен в нескольких
# классах. Его поведение меняется в зависимости от класса вызывающего
# его объекта.
animals = [Dog(), Cat()]
make_animals_sound(animals)
