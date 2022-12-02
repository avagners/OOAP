from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

'''
Исправленное решение после проверки с эталоном.
'''


class LinkedList(ABC, Generic[T]):

    # Конструктор
    # постусловие: создан пустой связный список
    def __init__(self) -> None:
        self.head_cursor: T = None
        self.tail_cursor: T = None
        self.cursor: T = None

    # Команды:
    # предусловие: связный список не пустой
    # постусловие: курсор установлен на первый узел в списке
    @abstractmethod
    def head(self) -> None: ...
    # предусловие: связный список не пустой
    # постусловие: курсор установлен на последний узел в списке
    @abstractmethod
    def tail(self) -> None: ...
    # предусловие: связный список не пустой
    # предусловие: курсор указывает не на хвост списка
    # постусловие: курсор сдвинут на один узел вправо
    @abstractmethod
    def right(self) -> None: ...
    # предусловие: связный список не пустой
    # постусловие: вставлен новый узел справа от курсора
    @abstractmethod
    def put_right(self, T) -> None: ...
    # предусловие: связный список не пустой
    # постусловие: вставлен новый узел слева от курсора
    @abstractmethod
    def put_left(self, T) -> None: ...
    # предусловие: связный список не пустой
    # постусловие: текущий узел удалён,
    # курсор смещён к правому соседу, если он есть,
    # в противном случае курсор смещён к левому соседу,
    # если он есть
    @abstractmethod
    def remove(self) -> None: ...
    # постусловие: удалены все узлы
    @abstractmethod
    def clear(self) -> None: ...
    # постусловие: добавлен новый узел в хвост списка
    @abstractmethod
    def add_tail(self, T) -> None: ...
    # предусловие: список не пуст;
    # постусловие: значение текущего узла заменено на новое
    @abstractmethod
    def replace(self, T) -> None: ...
    # постусловие: курсор установлен на следующий узел
    # с искомым значением, если такой узел найден
    @abstractmethod
    def find(self, T) -> None: ...
    # постусловие: в списке удалены все узлы с заданным значением
    @abstractmethod
    def remove_all(self) -> None: ...

    # Запросы:
    # предусловие: связный список не пустой
    @abstractmethod
    def get(self) -> T: ...
    @abstractmethod
    def size(self) -> int: ...
    @abstractmethod
    def is_head(self) -> bool: ...
    @abstractmethod
    def is_tail(self) -> bool: ...
    @abstractmethod
    def is_value(self) -> bool: ...

    # дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_head_status(self) -> int: ...  # успешно; список пуст
    @abstractmethod
    def get_tail_status(self) -> int: ...  # успешно; список пуст
    @abstractmethod
    def get_right_status(self) -> int: ...  # успешно; правее нету элемента
    @abstractmethod
    def get_put_right_status(self) -> int: ...  # успешно; список пуст
    @abstractmethod
    def get_put_left_status(self) -> int: ...  # успешно; список пуст
    @abstractmethod
    def get_remove_status(self) -> int: ...  # успешно; список пуст
    @abstractmethod
    def get_replace_status(self) -> int: ...  # успешно; список пуст
    @abstractmethod
    def get_find_status(self) -> int: ...  # следующий найден
    # следующий не найден; список пуст
    @abstractmethod
    def get_get_status(self) -> int: ...  # успешно; список пуст
