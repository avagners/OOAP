from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class AbsBoundedStack(ABC, Generic[T]):

    PUSH_NIL: int = 0  # push() ещё не вызывалась
    PUSH_OK: int = 1  # последняя push() отработала нормально
    PUSH_ERR: int = 2  # стек заполнен

    POP_NIL: int = 0  # pop() ещё не вызывалась
    POP_OK: int = 1  # последняя pop() отработала нормально
    POP_ERR: int = 2  # стек пуст

    PEEK_NIL: int = 0  # peek() ещё не вызывалась
    PEEK_OK: int = 1  # последняя peek() вернула корректное значение
    PEEK_ERR: int = 2  # стек пуст

    # Конструктор
    # постусловие: создан новый пустой ограниченный стек
    def __init__(self, size: int = 32):
        self._items: list = []
        self._size: int = size
        self._push_status: int = self.PUSH_NIL
        self._pop_status: int = self.POP_NIL
        self._peek_status: int = self.PEEK_NIL

    # Команды:
    # постусловие: в стек добавлено новое значение
    @abstractmethod
    def push(self, value: T) -> None: ...
    # предусловие: стек не пустой
    # постусловие: из стека удалён верхний элемент
    @abstractmethod
    def pop(self) -> None: ...
    # постусловие: из стека удалятся все значения
    @abstractmethod
    def clear(self) -> None: ...

    # Запросы:
    # предусловие: стек не пустой
    @abstractmethod
    def peek(self) -> T: ...
    @abstractmethod
    def size(self) -> int: ...

    # дополнительные запросы:
    # возвращает значение PUSH_*
    @abstractmethod
    def get_push_status(self) -> int: ...
    # возвращает значение POP_*
    @abstractmethod
    def get_pop_status(self) -> int: ...
    # возвращает значение PEEK_*
    @abstractmethod
    def get_peek_status(self) -> int: ...


class BoundedStack(AbsBoundedStack):

    def push(self, value: T) -> None:
        if len(self._items) == self._size:
            self._push_status = self.PUSH_ERR
            return
        self._items.append(value)
        self._push_status = self.PUSH_OK

    def pop(self) -> None:
        if not self._items:
            self._pop_status = self.POP_ERR
            return
        self._items.pop()
        self._pop_status = self.POP_OK

    def clear(self) -> None:
        self._items = []

    def peek(self) -> T:
        if not self._items:
            self._peek_status = self.PEEK_ERR
            return
        self._peek_status = self.PEEK_OK
        return self._items[-1]

    def size(self) -> int:
        return len(self._items)

    def get_pop_status(self) -> int:
        return self._pop_status

    def get_peek_status(self) -> int:
        return self._peek_status

    def get_push_status(self) -> int:
        return self._push_status
