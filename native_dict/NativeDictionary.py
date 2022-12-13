from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


# АТД NativeDictionary
class AbsNativeDictionary(ABC, Generic[T]):

    # Конструктор
    # постусловие: создан ассоциативный массив
    def __init__(self) -> None: ...

    # Команды:
    # постусловие: если ключа нет в массиве, то
    # новая пара ключ-значение добавлена в массив;
    # если ключ есть в массиве, то обновлено значение ключа
    @abstractmethod
    def put(self, key: str, value: T) -> None: ...
    # предусловие: в массиве есть запрашиваемый ключ
    # постусловие: пара "ключ-значение" удалена из массива
    @abstractmethod
    def remove(self, key: str) -> None: ...

    # Запросы:
    @abstractmethod
    def is_key(self, key: str) -> bool: ...  # есть ключ в массиве или нет
    @abstractmethod
    def size(self) -> int: ...  # кол-во пар "ключ-значение" в массиве
    # предусловие: запрашиваемый ключ есть в массиве
    @abstractmethod
    def get(self, key: str) -> T: ...  # получено значение по ключу

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_put_status(self) -> int: ...  # успешно добавлена новая пара
    # "ключ-значение"; успешно обновлено значение по ключу

    @abstractmethod
    def get_remove_status(self) -> int: ...  # успешно удалена пара
    # "ключ-значение"; в массиве нет запрашиваемого ключа

    @abstractmethod
    def get_get_status(self) -> int: ...  # успешно получено значение по ключу;
    # в массиве нет запрашиваемого ключа


# Реализация NativeDictionary
class NativeDictionary(AbsNativeDictionary):

    PUT_NIL = 0  # put() не вызывался
    PUT_OK_1 = 1  # успешно добавлена новая пара "ключ-значение" в массив
    PUT_OK_2 = 2  # успешно обновлено значение по ключу

    REMOVE_NIL = 0  # remove() не вызывался
    REMOVE_OK = 1  # успешно удалена пара "ключ-значение" из массива
    REMOVE_ERR = 2  # в массиве нет запрашиваемоего ключа

    GET_NIL = 0  # get() не вызывался
    GET_OK = 1  # успешно получено значение по ключу
    GET_ERR = 2  # в массиве нет запрашиваемоего ключа

    def __init__(self) -> None:
        super().__init__()
        self.__count = 0
        self.__capacity = 16
        self._slots = [None] * self.__capacity
        self._values = [None] * self.__capacity
        self.__put_status = self.PUT_NIL
        self.__remove_status = self.REMOVE_NIL
        self.__get_status = self.GET_NIL

    def __resize(self, new_capacity):
        new_slots = [None] * new_capacity
        new_values = [None] * new_capacity
        for i in range(self.__count):
            new_slots[i] = self._slots[i]
            new_values[i] = self._values[i]
        self._slots = new_slots
        self._values = new_values
        self.__capacity = new_capacity

    def _hash_fun(self, key):
        hash = sum([ord(sym) for sym in key]) % self.__capacity
        return hash

    def __remove_key_value(self, index: int) -> None:
        for j in range(index, self.__capacity - 1):
            self._slots[j] = self._slots[j + 1]
            self._values[j] = self._values[j + 1]
        decrease_capacity = int(self.__capacity / 1.5)
        if self.__count < self.__capacity * 0.5:
            self.__resize(decrease_capacity if decrease_capacity >= 16 else 16)

    def is_key(self, key) -> bool:
        return key in self._slots

    def put(self, key: str, value: T) -> None:
        index = self._hash_fun(key)
        if not self.is_key(key) and self.__count == self.__capacity:
            self.__resize(2 * self.__capacity)
        count = 0
        while count < self.__capacity:
            if self.is_key(key) and self._slots[index] == key:
                self._values[index] = value
                self.__put_status = self.PUT_OK_2
                return
            if not self.is_key(key) and not self._slots[index]:
                self._slots[index] = key
                self._values[index] = value
                self.__count += 1
                self.__put_status = self.PUT_OK_1
                return
            index += 1
            if index >= self.__capacity:
                index %= self.__capacity
            count += 1

    def remove(self, key: str) -> None:
        if not self.is_key(key):
            self.__remove_status = self.REMOVE_ERR
            return
        index = self._hash_fun(key)
        count = 0
        while count < self.__capacity:
            if self._slots[index] == key:
                self.__remove_key_value(index)
                self.__count -= 1
                self.__remove_status = self.REMOVE_OK
                return
            index += 1
            if index >= self.__capacity:
                index %= self.__capacity
            count += 1

    def size(self) -> int:
        return self.__count

    def get(self, key: str) -> T:
        if not self.is_key(key):
            self.__get_status = self.GET_ERR
            return
        index = self._hash_fun(key)
        count = 0
        while count < self.__capacity:
            if self._slots[index] == key:
                self.__get_status = self.GET_OK
                return self._values[index]
            index += 1
            if index >= self.__capacity:
                index %= self.__capacity
            count += 1

    def get_put_status(self) -> int:
        return self.__put_status

    def get_remove_status(self) -> int:
        return self.__remove_status

    def get_get_status(self) -> int:
        return self.__get_status
