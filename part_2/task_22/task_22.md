В этом примере иерархия классов реализует наследование видов. Животные могут быть классифицированы на основе различных критериев. Один из критериев - является ли животное млекопитающим или нет, а другой - плотоядное оно или травоядное.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}"

class Mammal(Animal):
    def __init__(self, name, species, diet):
        super().__init__(name, species)
        self.diet = diet
    
    def __str__(self):
        return f"{super().__str__()}, Diet: {self.diet}"

class Carnivore(Mammal):
    def __init__(self, name, species, diet, prey):
        super().__init__(name, species, diet)
        self.prey = prey
    
    def __str__(self):
        return f"{super().__str__()}, Prey: {self.prey}"

class Herbivore(Mammal):
    def __init__(self, name, species, diet, plant_type):
        super().__init__(name, species, diet)
        self.plant_type = plant_type
    
    def __str__(self):
        return f"{super().__str__()}, Plant Type: {self.plant_type}"

class Lion(Carnivore):
    def __init__(self, name):
        super().__init__(name, "Lion", "Carnivore", "Meat", "Antelopes")

class Tiger(Carnivore):
    def __init__(self, name):
        super().__init__(name, "Tiger", "Carnivore", "Meat", "Deer")

class Elephant(Herbivore):
    def __init__(self, name):
        super().__init__(name, "Elephant", "Herbivore", "Plants", "Grass")

class Giraffe(Herbivore):
    def __init__(self, name):
        super().__init__(name, "Giraffe", "Herbivore", "Plants", "Trees")
```