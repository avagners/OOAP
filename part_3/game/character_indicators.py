from abstract_classes.Characters import CharacterIndicator


# Реализация показателя персонажа "Голод"
class HungerIndicator(CharacterIndicator[int]):

    # Статусы
    DECREASE_NIL = 0  # decrease() не вызывался
    DECREASE_OK = 1  # показатель успешно уменьшился на n-единиц
    DECREASE_ERR = 2  # показатель меньше нуля

    INCREASE_NIL = 0  # increase() не вызывался
    INCREASE_OK = 1  # показатель успешно увеличился на n-единиц
    INCREASE_ERR = 2  # показатель больше 100%

    def __init__(self) -> None:
        self.value = 1000
        self._decrease_status = self.DECREASE_NIL
        self._increase_status = self.INCREASE_NIL

    def decrease(self, n: int) -> None:
        self.value -= n
        self._decrease_status = self.DECREASE_OK
        if self.value < 0:
            self.value = 0
            self._decrease_status = self.DECREASE_ERR

    def increase(self, n: int) -> None:
        self.value += n
        self._increase_status = self.INCREASE_OK
        if self.value > 1000:
            self.value = 1000
            self._increase_status = self.INCREASE_ERR

    def get_info(self) -> int:
        return self.value

    def get_increase_status(self) -> int:
        return self._increase_status

    def get_decrease_status(self) -> int:
        return self._decrease_status


# Реализация показателя "Здоровье"
class HealthIndicator(CharacterIndicator[int]):

    # Статусы
    DECREASE_NIL = 0  # decrease() не вызывался
    DECREASE_OK = 1  # показатель успешно уменьшился на n-единиц
    DECREASE_ERR = 2  # показатель меньше нуля

    INCREASE_NIL = 0  # increase() не вызывался
    INCREASE_OK = 1  # показатель успешно увеличился на n-единиц
    INCREASE_ERR = 2  # показатель больше 100%

    def __init__(self) -> None:
        self.value = 100
        self._decrease_status = self.DECREASE_NIL
        self._increase_status = self.INCREASE_NIL

    def decrease(self, n: int) -> None:
        self.value -= n
        self._decrease_status = self.DECREASE_OK
        if self.value < 0:
            self.value = 0
            self._decrease_status = self.DECREASE_ERR

    def increase(self, n: int) -> None:
        self.value += n
        self._increase_status = self.INCREASE_OK
        if self.value > 100:
            self.value = 100
            self._increase_status = self.INCREASE_ERR

    def get_info(self) -> int:
        return self.value

    def get_increase_status(self) -> int:
        return self._increase_status

    def get_decrease_status(self) -> int:
        return self._decrease_status
