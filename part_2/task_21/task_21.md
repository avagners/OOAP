### Наследование реализации (implementation inheritance).  
В этом примере класс Car полностью реализован и служит базовым классом для классов SportsCar и ElectricCar, которые наследуют его атрибуты и методы. Классы SportsCar и ElectricCar добавляют свою собственную уникальную абстракцию структуры данных (в данном случае атрибуты top_speed и battery_capacity, соответственно).

```python
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start_engine(self):
        print("Engine started")
        
    def stop_engine(self):
        print("Engine stopped")
        
class SportsCar(Car):

    def __init__(self, make, model, year, top_speed):
        super().__init__(make, model, year)
        self.top_speed = top_speed
        
    def start_engine(self):
        print("Sports car engine started")
        
    def stop_engine(self):
        print("Sports car engine stopped")
        
class ElectricCar(Car):

    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        
    def start_engine(self):
        print("Electric car engine started")
        
    def stop_engine(self):
        print("Electric car engine stopped")
```

### Льготное наследование (facility inheritance)  
В этом примере родительский класс Shape предоставляет базовую структуру и стандартные компоненты (координаты x, y и метод расчета площади), которые используются его классами-потомками Rectangle и Circle. Потомки наследуют базовую структуру и добавляют свою собственную реализацию метода area, основанную на уникальных свойствах их фигуры. Это представляет собой льготное наследование, когда родительский класс предоставляет набор компонентов, а его потомки реализуют конкретные специальные случаи.

```python
class Shape:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def area(self):
        pass
    
class Rectangle(Shape):

    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
```