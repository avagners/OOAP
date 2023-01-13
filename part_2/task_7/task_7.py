from abc import ABC


class Status(ABC):

    # Конструктор
    # постусловие: установлен статус
    def __init__(self, status: str) -> None:
        self.status = status

    # Запросы:
    # получен статус
    def get_status(self) -> str:
        return self.status


class StatusOk(Status):

    def __init__(self) -> None:
        super().__init__(status='OK')


class StatusError(Status):

    def __init__(self) -> None:
        super().__init__(status='SOME_ERROR')


# в зависимости от ответа создаем объект определенного класса
def response(code: int) -> Status:
    if code != 200:
        return StatusError()
    return StatusOk()


if __name__ == '__main__':
    response_codes = [200, 404, 503]
    for code in response_codes:
        status = response(code).get_status()
        print(status)
