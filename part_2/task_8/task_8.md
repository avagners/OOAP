## Ковариатность

```python
from typing import Tuple

class Animal: ...
class Dog(Animal): ...

an_animal: Animal = Animal()
lassie: Dog = Dog()
snoopy: Dog = Dog()

animals: Tuple[Animal, ...] = (an_animal, lassie)
dogs: Tuple[Dog, ...] = (snoopy, lassie)

animals = dogs
```

## Контравариатность

```python
from typing import Callable

class Animal: ...
class Dog(Animal): ...

def animal_run(animal: Animal) -> None:
    print('An animal is running.')

def dog_running(dog: Dog) -> None:
    print('A dog is running.')

def make_dog_run(a_dog: Animal, run_func: Callable[[Dog], None]) -> None:
    run_func(a_dog)

lassie: Dog = Dog()

make_dog_run(a_dog=lassie, run_func=animal_run)

# функция контравариантна по типам аргументов
```