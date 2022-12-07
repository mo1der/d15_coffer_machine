def add(*args):
    suma = 0
    for i in args:
        suma += i
    return print(suma)

add(2,3, 4,5, 6)


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    #
    # print(kwargs["nazwa_klucza"])

    n+= kwargs["add"]
    n*= kwargs["multiply"]

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kw.get("model")  #zaleta że zwraca None jak odwołujemy się do niego zamiast Error