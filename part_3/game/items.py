from typing import List
import arcade
from abstract_classes.Items import AbstractItem, AbstractStorage


# Реализация игрового предмета "Монета"
class Coin(AbstractItem):

    # Статусы
    USE_NIL = 0
    USE_OK = 1
    USE_ERR = 2

    GET_NIL = 0
    GET_OK = 1
    GET_ERR = 2

    DELETE_NIL = 0
    DELETE_OK = 1
    DELETE_ERR = 2

    def __init__(self, x: int, y: int) -> None:
        self.name = 'Монета'
        self.sprite = arcade.Sprite('resources/img/items/coinGold_ll.png')
        self.x = x
        self.y = y
        self.cost = 1
        self._use_status = self.USE_NIL
        self._get_status = self.USE_NIL
        self._delete_status = self.DELETE_NIL

    def use(self) -> None:
        print(f'Предмет {self.name} использован')

    def get(self) -> None:
        print(f'Предмет {self.name} получен')
        self._get_status = self.GET_OK

    def delete(self) -> None:
        print(f'Предмет {self.name} удален')
        self._delete_status = self.DELETE_OK

    def get_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost
        }

    def get_name(self) -> str:
        return self.name

    def get_use_status(self) -> int:
        return self._use_status

    def get_get_status(self) -> int:
        return self._get_status

    def get_delete_status(self) -> int:
        return self._delete_status

    def draw(self):
        self.sprite.center_x = self.x
        self.sprite.center_y = self.y
        self.sprite.draw()


# Реализация хранилища предметов персонажа
class Storage(AbstractStorage):

    # Статусы
    DELETE_ITEM_NIL = 0  # delete_item() не вызывался
    DELETE_ITEM_OK = 1  # предмет успешно удален из хранилища
    DELETE_ITEM_ERR = 2  # предмета нет в хранилище

    ADD_ITEM_NIL = 0  # add_item() не вызывался
    ADD_ITEM_OK = 1  # предмет успешно добавлен в хранилища
    ADD_ITEM_ERR = 2  # нет свободного места в хранилище

    SELL_ITEM_NIL = 0  # sell_item() не вызывался
    SELL_ITEM_OK = 1  # предмет успешно продан
    SELL_ITEM_ERR = 2  # предмета нет в хранилище

    def __init__(self) -> None:
        self.items: List[AbstractItem] = []
        self.max_length_storage: int = 50
        self._delete_item_status: int = self.DELETE_ITEM_NIL
        self._add_item_status: int = self.ADD_ITEM_NIL
        self._sell_item_status: int = self.SELL_ITEM_NIL

    def delete_item(self, item: AbstractItem) -> None:
        if item in self.items:
            self.items.remove(item)
            self._delete_item_status = self.DELETE_ITEM_OK
            return
        self._delete_item_status = self.DELETE_ITEM_ERR

    def add_item(self, item: AbstractItem) -> None:
        if len(self.items) < self.max_length_storage:
            self.items.append(item)
            self._add_item_status = self.ADD_ITEM_OK
            return
        self._add_item_status = self.ADD_ITEM_ERR

    def sell_item(self, item: AbstractItem) -> None:
        if item in self.items:
            self.items.remove(item)
            # Логика продажи предмета и увеличения кол-ва
            # монет у персонажа
            self._sell_item_status = self.SELL_ITEM_OK
            return
        self._sell_item_status = self.SELL_ITEM_ERR

    def get_items(self) -> List[AbstractItem]:
        return self.items

    def get_delete_item_status(self) -> int:
        return self._delete_item_status

    def get_add_item_status(self) -> int:
        return self._add_item_status

    def get_sell_item_status(self) -> int:
        return self._sell_item_status
