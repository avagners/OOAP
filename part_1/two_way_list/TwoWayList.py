from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

'''
Создана иерархия АТД: ParentList, LinkedList,  TwoWayList.
LinkedList,  TwoWayList наследуются от ParentList.
'''


class AbsParentList(ABC, Generic[T]):

    HEAD_NIL = 0  # head() еще не вызывался
    HEAD_OK = 1  # курсор успешно установлен на голову списка
    HEAD_ERR = 2  # список пуст, курсор не установлен

    TAIL_NIL = 0  # tail() еще не вызывался
    TAIL_OK = 1  # курсор успешно установлен на хвост списка
    TAIL_ERR = 2  # список пуст, курсор не установлен

    RIGHT_NIL = 0  # right() еще не вызывался
    RIGHT_OK = 1  # курсор успешно сдвинут на один узел вправо
    RIGHT_ERR = 2  # список пуст, курсор не установлен

    PUT_RIGHT_NIL = 0  # put_right() еще не вызывался
    PUT_RIGHT_OK = 1  # успешно вставлен новый узел справа от курсора
    PUT_RIGHT_ERR = 2  # список пуст, правее нет узла

    PUT_LEFT_NIL = 0  # put_left() еще не вызывался
    PUT_LEFT_OK = 1  # успешно вставлен новый узел слева от курсора
    PUT_LEFT_ERR = 2  # список пуст, левее нет узла

    REMOVE_NIL = 0  # remove() еще не вызывался
    REMOVE_OK = 1  # успешно удален узел из списка
    REMOVE_ERR = 2  # список пуст

    REPLACE_NIL = 0  # replace() еще не вызывался
    REPLACE_OK = 1  # успешно заменено значение текущего узла
    REPLACE_ERR = 2  # список пуст

    FIND_NIL = 0  # find() еще не вызывался
    FIND_OK = 1  # успешно курсор перемещен на узел с искомым значением
    FIND_NOT_FOUND = 2  # узел с искомым значением не найден
    FIND_ERR = 3  # список пуст

    GET_NIL = 0  # get() еще не вызывался
    GET_OK = 1  # успешно получили значение текущего узла
    GET_ERR = 2  # # список пуст

    # Конструктор
    # постусловие: создан пустой связный список
    def __init__(self) -> None:
        self.head_cursor = None
        self.tail_cursor = None
        self.cursor = None

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
    def put_right(self, value: T) -> None: ...
    # предусловие: связный список не пустой
    # постусловие: вставлен новый узел слева от курсора
    @abstractmethod
    def put_left(self, value: T) -> None: ...
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
    def add_tail(self, value: T) -> None: ...
    # предусловие: список не пуст;
    # постусловие: значение текущего узла заменено на новое
    @abstractmethod
    def replace(self, value: T) -> None: ...
    # постусловие: курсор установлен на следующий узел
    # с искомым значением, если такой узел найден
    @abstractmethod
    def find(self, value: T) -> None: ...
    # постусловие: в списке удалены все узлы с заданным значением
    @abstractmethod
    def remove_all(self, value: T) -> None: ...

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


# Реализация двунаправленного связного списка
class Node:
    def __init__(self, v):
        super().__init__()
        self.value = v
        self.prev = None
        self.next = None


class ParentList(AbsParentList):

    def __init__(self) -> None:
        self.head_cursor: Node = None
        self.tail_cursor: Node = None
        self.cursor: Node = None
        self._head_status: int = self.HEAD_NIL
        self._tail_status: int = self.TAIL_NIL
        self._right_status: int = self.RIGHT_NIL
        self._put_right_status: int = self.PUT_RIGHT_NIL
        self._put_left_status = self.PUT_LEFT_NIL
        self._remove_status = self.REMOVE_NIL
        self._replace_status = self.REPLACE_NIL
        self._find_status = self.FIND_NIL
        self._get_status = self.GET_NIL

    def head(self) -> None:
        if not self.head_cursor:
            self._head_status = self.HEAD_ERR
            return
        self.cursor = self.head_cursor
        self._head_status = self.HEAD_OK

    def tail(self) -> None:
        if not self.tail_cursor:
            self._tail_status = self.TAIL_ERR
            return
        self.cursor = self.tail_cursor
        self._tail_status = self.TAIL_OK

    def right(self) -> None:
        if not self.is_head() or self.is_tail():
            self._right_status = self.RIGHT_ERR
            return
        self.cursor = self.cursor.next
        self._right_status = self.RIGHT_OK

    def put_right(self, value: T) -> None:
        if not self.is_value():
            self._put_right_status = self.PUT_RIGHT_ERR
            return
        new_node = Node(value)
        if self.is_tail():
            self.cursor.next = new_node
            new_node.prev = self.cursor
            self._put_right_status = self.PUT_RIGHT_OK
            return
        self.cursor.next.prev = new_node
        new_node.next = self.cursor.next
        new_node.prev = self.cursor
        self.cursor.next = new_node
        self._put_right_status = self.PUT_RIGHT_OK

    def put_left(self, value: T) -> None:
        if not self.is_value():
            self._put_left_status = self.PUT_LEFT_ERR
            return
        new_node = Node(value)
        if self.is_head():
            self.cursor.prev = new_node
            new_node.next = self.cursor
            self._put_left_status = self.PUT_LEFT_OK
            return
        self.cursor.prev.next = new_node
        new_node.next = self.cursor
        new_node.prev = self.cursor.prev
        self.cursor.prev = new_node
        self._put_left_status = self.PUT_LEFT_OK

    def remove(self) -> None:
        if not self.is_value():
            self._remove_status = self.REMOVE_ERR
            return
        if not self.is_head() and not self.is_tail():
            self.cursor.next.prev = self.cursor.prev
            self.cursor.prev.next = self.cursor.next
        if self.is_head():
            self.cursor.next.prev = None
        if self.is_tail():
            self.cursor.prev.next = None
        if self.cursor.next:
            self.cursor = self.cursor.next
        else:
            self.cursor = self.cursor.prev
        self._remove_status = self.REMOVE_OK

    def clear(self) -> None:
        self.head_cursor = None
        self.tail_cursor = None
        self.cursor = None

    def add_tail(self, value: T) -> None:
        new_node = Node(value)
        if not self.is_value():
            self.head_cursor = new_node
            self.tail_cursor = new_node
            self.cursor = new_node
            return
        self.tail_cursor.next = new_node
        new_node.prev = self.tail_cursor
        self.tail_cursor = new_node

    def replace(self, value: T) -> None:
        if not self.is_value():
            self._replace_status = self.REPLACE_ERR
            return
        self.cursor.value = value
        self._replace_status = self.REPLACE_OK

    def find(self, value: T) -> None:
        if not self.is_value():
            self._find_status = self.FIND_ERR
            return
        while self.cursor:
            if self.cursor.value == value:
                self._find_status = self.FIND_OK
                return
            self.cursor = self.cursor.next
        self._find_status = self.FIND_NOT_FOUND

    def remove_all(self, value: T) -> None:
        if not self.head_cursor:
            return
        self.cursor = self.head_cursor
        while self.cursor.next:
            if self.cursor.value != value:
                continue
            if self.is_tail() and self.is_head():
                self.tail_cursor = None
                self.head_cursor = None
                self.cursor = None
                return
            if not self.is_head() and not self.is_tail():
                self.cursor.next.prev = self.cursor.prev
                self.cursor.prev.next = self.cursor.next
            if self.is_head():
                self.cursor.next.prev = None
                self.head_cursor = self.cursor.next
            if self.is_tail():
                self.cursor.prev.next = None
                self.tail_cursor = self.cursor.prev
            self.cursor = self.cursor.next

    def get(self) -> T:
        if not self.is_value():
            self._get_status = self.GET_ERR
            return
        self._get_status = self.GET_OK
        return self.cursor.value

    def size(self) -> int:
        node = self.head_cursor
        result = []
        while node:
            result.append(node)
            node = node.next
        return len(result)

    def is_head(self) -> bool:
        return self.cursor == self.head_cursor

    def is_tail(self) -> bool:
        return self.cursor == self.tail_cursor

    def is_value(self) -> bool:
        return isinstance(self.cursor, Node)

    def get_head_status(self) -> int:
        return self._head_status

    def get_tail_status(self) -> int:
        return self._tail_status

    def get_right_status(self) -> int:
        return self._right_status

    def get_put_right_status(self) -> int:
        return self._put_right_status

    def get_put_left_status(self) -> int:
        return self._put_left_status

    def get_remove_status(self) -> int:
        return self._remove_status

    def get_replace_status(self) -> int:
        return self._replace_status

    def get_find_status(self) -> int:
        return self._find_status

    def get_get_status(self) -> int:
        return self._get_status


class LinkedList(ParentList):

    # Конструктор
    # постусловие: создан пустой связный список
    def __init__(self) -> None:
        super().__init__()


class TwoWayList(ParentList):

    LEFT_NIL = 0  # left() еще не вызывался
    LEFT_OK = 1  # курсор успешно сдвинут на один узел влево
    LEFT_ERR = 2  # список пустой

    # Конструктор
    # постусловие: создан пустой двунаправленный связный список
    def __init__(self) -> None:
        super().__init__()
        self._left_status = self.LEFT_NIL

    # Команды:
    # предусловие: связный список не пустой
    # предусловие: курсор указывает не на головоу списка
    def left(self) -> None:
        if not self.is_value():
            self._left_status = self.LEFT_ERR
            return
        if self.is_head():
            self._left_status = self.LEFT_ERR
            return
        self.cursor = self.cursor.prev
        self._left_status = self.LEFT_OK

    def get_left_status(self) -> int:
        return self._left_status
