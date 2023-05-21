import arcade

from abstract_classes.Characters import AbstractEnemy, Character
from character_indicators import HealthIndicator, HungerIndicator
from items import Storage
from abstract_classes.Items import AbstractItem


# Пример класса-наследника персонажа
class Player(Character):

    # Статусы
    DAMAGE_NIL = 0  # damage() не вызывался
    DAMAGE_OK = 1  # успешно нанесен урон на n-единиц
    DAMAGE_ERR = 2  # показатель здоровья меньше нуля

    RECUPERATE_NIL = 0  # recuperate() не вызывался
    RECUPERATE_OK = 1  # успешно восстановлено здоровье на n-единиц
    RECUPERATE_ERR = 2  # показатель здоровья 100%

    GET_ITEM_STATUS_NIL = 0  # get_item() не вызывался
    GET_ITEM_STATUS_OK = 1  # успешно получен игровой предмет
    GET_ITEM_STATUS_ERR = 2  # хранилище переполнено

    USE_ITEM_STATUS_NIL = 0  # get_item() не вызывался
    USE_ITEM_STATUS_OK = 1  # успешно получен игровой предмет
    USE_ITEM_STATUS_ERR = 2  # хранилище переполнено

    def __init__(self, name: str, sprite: arcade.Sprite) -> None:
        self.name = name
        self.sprite = sprite
        # стартовое позиционирование задаем по-умолчанию
        self.x = 100
        self.y = 100
        self.hunger_indicator = HungerIndicator()
        self.health = HealthIndicator()
        self.storage = Storage()
        self._damage_status = self.DAMAGE_NIL
        self._recuperate_status = self.RECUPERATE_NIL
        self._get_item_status = self.GET_ITEM_STATUS_NIL
        self._use_item_status = self.USE_ITEM_STATUS_NIL

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

    def use_item(self, item: AbstractItem) -> None:
        if item not in self.storage.get_items():
            print('Предмета нет в хранилище.')
            return
        self.storage.delete_item(item)
        if self.storage.get_delete_item_status():
            item.use()  # вызываем метод use предмета
            self._use_item_status = self.USE_ITEM_STATUS_OK
            print(f'Предмета {item.name} успешно использован.')
            return
        self._use_item_status = self.USE_ITEM_STATUS_ERR

    def get_item(self, item: AbstractItem) -> None:
        self.storage.add_item(item)  # Добавление предмета в хранилище
        if self.storage.get_add_item_status():
            self._get_item_status = self.GET_ITEM_STATUS_OK
            return
        self._get_item_status = self.GET_ITEM_STATUS_ERR

    def get_name(self) -> str:
        return self.name

    def get_damage_status(self) -> int:
        return self._damage_status

    def get_recuperate_status(self) -> int:
        return self._recuperate_status

    def get_get_item_status(self) -> int:
        return self._get_item_status

    def draw(self) -> None:
        self.sprite.center_x = self.x
        self.sprite.center_y = self.y
        self.sprite.draw()


# Реализация класса врага
class Enemy(AbstractEnemy):

    # Статусы
    DAMAGE_NIL = 0  # damage() не вызывался
    DAMAGE_OK = 1  # успешно нанесен урон на n-единиц
    DAMAGE_ERR = 2  # показатель здоровья меньше нуля

    def __init__(self, name: str, x: float, y: float,
                 sprite: arcade.Sprite) -> None:
        self.name = name
        self.sprite = sprite
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
        self.sprite.center_x = self.x
        self.sprite.center_y = self.y
        self.sprite.draw()
        # Отрисовка индикатора здоровья игрока
        arcade.draw_text(f"Player Health: {self.health.get_info()}",
                         10, 10, arcade.color.WHITE, 14)
