from typing import Any
from abstract_classes.Settings import AbstractSettings


class Settings(AbstractSettings):

    # Статусы
    ADD_NIL = 0  # add() не вызывался
    ADD_OK = 1  # успешно добавлена пара ключ-значение
    ADD_ERR = 2  # ключ есть в словаре

    CHANGE_NIL = 0  # change() не вызывался
    CHANGE_OK = 1  # успешно обновлено значение по ключу
    CHANGE_ERR = 2  # ключа нет в словаре

    def __init__(self, **kwargs) -> None:
        self.settings: dict = kwargs
        self._change_status = self.CHANGE_NIL
        self._add_status = self.ADD_NIL

    def is_key(self, key: str) -> bool:
        return key in self.settings.keys()

    def add(self, key: str, value: Any) -> None:
        if not self.is_key(key):
            self.settings[key] = value
            self._add_status = self.ADD_OK
            return
        self._add_status = self.ADD_ERR

    def change(self, key: str, value: Any) -> None:
        if self.is_key(key):
            self.settings[key] = value
            self._change_status = self.CHANGE_OK
            return
        self._change_status = self.CHANGE_ERR

    def get_value(self, key: str) -> Any:
        return self.settings[key]

    def get_change_status(self) -> int:
        return self._change_status

    def get_add_status(self) -> int:
        return self._add_status
