from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

'''
2.2 Операция tail не сводима к другим операциям, т.к. в структуре данных есть
указатели, которые всегда указывают на голову и хвост списка. По этой причине
доступ к хвосту получаем за O(1).

2.3 Операция поиска всех узлов с заданным значением не нужна, т.к.
есть методы find() и get(), с помощью которых последовательно перемещаем курсор
с запрашиваемым значением и получаем узлы.
'''


class LinkedList(ABC, Generic[T]):

    # Конструктор
    # постусловие: создан пустой связный список с курсором, указателями
    # на голову и хвост списка
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
    # постусловие: удален текущий узел
    # постусловие: курсор сдвигается вправо, если не хвост,
    # в противном случае влево
    @abstractmethod
    def remove(self) -> None: ...
    # постусловие: удалены все узлы
    @abstractmethod
    def clear(self) -> None: ...
    # постусловие: добавлен новый узел в хвост списка
    @abstractmethod
    def add_tail(self, T) -> None: ...
    # постусловие: заменен узел в списке на новый
    # постусловие: курсор указывает на новый узел
    @abstractmethod
    def replace(self, T) -> None: ...
    # предусловие: связный список не пустой
    # предусловие: в списке есть узел с запрашиваемым значением
    # постусловие: курсор перемещен на след. узел с искомым значением,
    # по отношению к текущему
    @abstractmethod
    def find(self, T) -> None: ...
    # предусловие: связный список не пустой
    # предусловие: в списке есть узлы с запрашиваемым значением
    # постусловие: удалены все узлы с указанным значением
    # постусловие: курсор сдвигается вправо, если не хвост,
    # в противном случае влево
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
    # проверка выполнения метода head()
    # True, если список не пустой и курсор указывает на голову списка,
    # иначе False
    @abstractmethod
    def get_head_status(self) -> bool: ...
    # проверка выполнения метода tail()
    # True, если список не пустой и курсор указывает на голову списка,
    # иначе False
    @abstractmethod
    def get_tail_status(self) -> bool: ...
    # проверка наличия узла справа
    # True, если список не пустой и есть узел справа, иначе False
    @abstractmethod
    def get_right_status(self) -> bool: ...
    # проверка вставки нового узла справа от курсора
    # True, если список не пустой, иначе False
    @abstractmethod
    def get_put_right_status(self) -> bool: ...
    # проверка вставки нового узла слева от курсора
    # True, если список не пустой, иначе False
    @abstractmethod
    def get_put_left_status(self) -> bool: ...
    # проверка удаления узла
    # True, если список не пустой, иначе False
    @abstractmethod
    def get_remove_status(self) -> bool: ...
    # проверка успешности замены узла
    # True, если список не пустой и искомый узел найден, иначе False
    @abstractmethod
    def get_replace_status(self) -> bool: ...
    # проверка поиска след. узла
    # True, если список не пустой и искомый узел есть правее курсора,
    # иначе False
    @abstractmethod
    def get_find_status(self) -> bool: ...
    # проверка получения узла
    # True, если список не пустой и получен узел, иначе False
    @abstractmethod
    def get_get_status(self) -> bool: ...
