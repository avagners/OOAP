1) Метод публичен в родительском классе А и публичен в его потомке B.

```python
class Parent:
    def my_method(self):
        print("This is a public method in Parent class")


class Child(Parent):
    pass


p = Parent()
p.my_method()  # print "This is a public method in Parent class"
c = Child()
c.my_method()  # print "This is a public method in Parent class"
```

2) Метод публичен в родительском классе А и скрыт в его потомке B.
```python
class Parent:
    def my_method(self):
        print("This is a public method in Parent class")


class Child(Parent):
    def __my_method(self):
        print("This is a hidden method in Child class")


p = Parent()
p.my_method()  # print "This is a public method in Parent class"
c = Child()
c.__my_method()  # raises an AttributeError
```

3) Метод скрыт в родительском классе А и публичен в его потомке B.
```python
class Parent:
    def __my_method(self):
        print("This is a hidden method in Parent class")


class Child(Parent):
    def my_method(self):
        print("This is a public method in Child class")

p = Parent()
p.__my_method()  # raises an AttributeError
c = Child()
c.my_method()  # print "This is a public method in Child class"
```

4) Метод скрыт в родительском классе А и скрыт в его потомке B.
```python
class Parent:
    def __my_method(self):
        print("This is a hidden method in Parent class")


class Child(Parent):
    def __my_method(self):
        print("This is a hidden method in Child class")


p = Parent()
p.__my_method()  # raises an AttributeError
c = Child()
c.__my_method()  # raises an AttributeError
```
`В случаях 2 и 4 метод не полностью скрыт, так как к нему можно получить доступ с помощью _ClassName__my_method, но использовать такой способ доступа не рекомендуется.`
