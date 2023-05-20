import arcade

from abstract_classes.Characters import AbstractEnemy, Character
from character_indicators import HealthIndicator, HungerIndicator


# Пример класса-наследника персонажа
class Player(Character):

    # Статусы
    DAMAGE_NIL = 0  # damage() не вызывался
    DAMAGE_OK = 1  # успешно нанесен урон на n-единиц
    DAMAGE_ERR = 2  # показатель здоровья меньше нуля

    RECUPERATE_NIL = 0  # recuperate() не вызывался
    RECUPERATE_OK = 1  # успешно восстановлено здоровье на n-единиц
    RECUPERATE_ERR = 2  # показатель здоровья 100%

    def __init__(self, name: str, x: float, y: float) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.hunger_indicator = HungerIndicator()
        self.health = HealthIndicator()
        self._damage_status = self.DAMAGE_NIL
        self._recuperate_status = self.RECUPERATE_NIL

    def damage(self, n: int) -> None:
        self.health.decrease(n)
        if self.health.get_decrease_status():
            self._damage_status = self.DAMAGE_OK
        self._damage_status = self.DAMAGE_ERR

    def recuperate(self, n: int) -> None:
        self.health.increase(n)
        if self.health.get_increase_status():
            self._recuperate_status = self.RECUPERATE_OK
            return
        self._damage_status = self.RECUPERATE_ERR

    def get_name(self) -> str:
        return self.name

    def get_damage_status(self) -> int:
        return self._damage_status

    def get_recuperate_status(self) -> int:
        return self._recuperate_status

    def draw(self) -> None:
        arcade.draw_rectangle_filled(self.x, self.y, 50, 50, arcade.color.BLUE)


# Реализация класса врага
class Enemy(AbstractEnemy):

    # Статусы
    DAMAGE_NIL = 0  # damage() не вызывался
    DAMAGE_OK = 1  # успешно нанесен урон на n-единиц
    DAMAGE_ERR = 2  # показатель здоровья меньше нуля

    def __init__(self, name: str, x: float, y: float) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.health = HealthIndicator()
        self._damage_status = self.DAMAGE_NIL

    def damage(self, n: int) -> None:
        self.health.decrease(n)
        if self.health.get_decrease_status():
            self._damage_status = self.DAMAGE_OK
            return
        self._damage_status = self.DAMAGE_ERR

    def get_damage_status(self) -> int:
        return self._damage_status

    def draw(self) -> None:
        arcade.draw_rectangle_filled(self.x, self.y, 30, 30, arcade.color.RED)
