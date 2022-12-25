from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class AbsQueue(ABC, Generic[T]):

    # Конструктор
    # постусловие: создана пустая очередь
    def __init__(self) -> None: ...

    # Команды:
    # постусловие: новый элемент добавлен в конец очереди
    @abstractmethod
    def enqueue(self, value: T) -> None: ...
    # предусловие: очередь не пустая
    # постусловие: элемент удален из головы очереди
    @abstractmethod
    def dequeue(self) -> T: ...  # элемент из головы очереди

    # Запросы:
    @abstractmethod
    def size(self) -> int: ...  # размер очереди

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_dequeue_status(self) -> int: ...  # успешно; пустая очередь


# Реализация очереди
class Queue(AbsQueue):

    DEQUEUE_NIL = 0  # dequeue() еще не вызывался
    DEQUEUE_OK = 1  # успешно получили элемент из головы очереди с последующим удалением
    DEQUEUE_ERR = 2  # очередь пустая

    def __init__(self) -> None:
        super().__init__()
        self.queue = []
        self._dequeue_status = self.DEQUEUE_NIL

    def enqueue(self, value: T) -> None:
        self.queue.append(value)

    def dequeue(self) -> T:
        if not self.queue:
            self._dequeue_status = self.DEQUEUE_ERR
            return
        self._dequeue_status = self.DEQUEUE_OK
        return self.queue.pop(0)

    def size(self) -> int:
        return len(self.queue)

    def get_dequeue_status(self) -> int:
        return self._dequeue_status
