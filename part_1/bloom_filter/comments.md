# Отличия с эталонным решением

Отсутсвует примечание для запроса is_value() о том, что возможно ложноположительное срабатывание.

Решение:
```python
# Запросы:
# есть ли значение в фильтре Блюма
def is_value(self, value: T) -> bool: ...
```

Эталон:
```java
// запросы
public bool is_value(T value);
// содержится ли значение в фильтре
// (допускаются ложноположительные срабатывания)
```