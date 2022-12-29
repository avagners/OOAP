from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class ProcessSettings(ABC, Generic[T]):
    '''
    Класс содержит методы извлечения данных из настроек, которые
    были получены через API v.1.0.
    '''
    # Конструктор
    # постусловие: создан объект с настройками, полученными через API
    def __init__(self, settings: dict) -> None: ...

    # Запросы:

    # получены поля из спецификации
    @abstractmethod
    def get_spec_fields(self, spec_code: str) -> dict: ...

    @abstractmethod
    def get_email_list(self) -> list: ...  # получен список рассылки


class ProcessSettingsV2(ProcessSettings, dict):
    '''
    Класс содержит методы извлечения данных из настроек, которые
    были получены через API v.2.0.
    '''
    # Запросы:

    # Специализация класса-родителя - реализация под другую структуру json
    @abstractmethod
    def get_email_list(self) -> list: ...  # получен список рассылки

    # Расширение класса-родителя - данного метода нет в родительском классе
    @abstractmethod
    def get_distr_id(self) -> int: ...  # получен код дистрибьютора
