from abc import abstractmethod, ABC


class Animal(ABC):

    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def __init__(self, name: str):
        super().__init__(name, "Cat")

    def make_sound(self):
        print("Meow")


class Dog(Animal):

    def __init__(self, name: str):
        super().__init__(name, "Dog")

    def make_sound(self):
        print("Woof")


if __name__ == '__main__':
    cat = Cat("Whiskers")
    cat.make_sound()  # Output: Meow

    dog = Dog("Buddy")
    dog.make_sound()  # Output: Woof
