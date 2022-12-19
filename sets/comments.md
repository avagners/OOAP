# Отличия с эталонным решением

Отличается формулировка комментриев к запросам. 
Например,

Решение
```python
# Запросы:
# пересечение текущего множества с множеством set
@abstractmethod
def intersection(self, set: PowerSet) -> PowerSet: ...
# объединение двух множеств
@abstractmethod
def union(self, set: PowerSet) -> PowerSet: ...
# подмножество текущего множества из элементов, которые не входят set
@abstractmethod
def difference(self, set: PowerSet) -> PowerSet: ...
# входят ли все элементы set в текущее множество
@abstractmethod
def issubset(self, set: PowerSet) -> bool: ...
```

Эталон:
```java
// запросы
// возвращает пересечение текущего множества
// с множеством set
public PowerSet<T> Intersection(PowerSet<T> set);

// возвращает объединение текущего множества
// и множества set
public PowerSet<T> Union(PowerSet<T> set);

// возвращает разницу между текущим множеством
// и множеством set
public PowerSet<T> Difference(PowerSet<T> set);

// проверка, будет ли set подмножеством
// текущего множества
public bool IsSubset(PowerSet<T> set);
```