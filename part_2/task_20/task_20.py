from abc import ABC, abstractmethod


# Наследования вариаций (variation inheritance)
class Animal:

    def make_sound(self):
        return "Some generic animal sound"


class Dog(Animal):

    def make_sound(self):
        return "Woof woof"


class Cat(Animal):

    def make_sound(self):
        return "Meow meow"


'''
В этом примере класс Animal имеет метод make_sound, который возвращает
общий звук животного. Классы Dog и Cat наследуют от класса Animal и
переопределяют метод make_sound, чтобы он возвращал специфический звук.
Это пример вариативного наследования, когда дочерние классы изменяют
поведение родительского класса без изменения его сигнатуры.
'''


# Наследование с конкретизацией (reification inheritance)
class Car(ABC):

    @abstractmethod
    def start_engine(self): ...


class SportsCar(Car):

    def start_engine(self):
        print("Starting engine for SportsCar")


class ElectricCar(Car):

    def start_engine(self):
        print("Starting engine for ElectricCar")


'''
В этом примере абстрактный класс Car имеет абстрактный метод start_engine,
который реализуется классами SportsCar и ElectricCar. Это пример наследования
с конкретизацией, поскольку дочерние классы только реализуют метод
родительского класса и не добавляют никакой новой функциональности.
'''


# Структурное наследование (structure inheritance)
class Shape:

    def __init__(self, name):
        self.name = name


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height


class Circle(Shape):

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius


'''
В этом примере классы Rectangle и Circle наследуют атрибут name от
класса Shape, но добавляют свои собственные атрибуты width и height
или radius. Наследование здесь структурное, поскольку классы Rectangle
и Circle добавляют новые атрибуты, а не просто реализуют методы,
определенные в Shape.
'''
