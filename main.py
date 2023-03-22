class ListMath:
    def __init__(self, lst=None):
        self.lst_math = lst if lst and type(lst) == list else []
        self.lst_math = list(filter(lambda x: type(x) in (int, float), self.lst_math))

    def __veryfy_value(self, val):
        if type(val) not in (int, float):
            raise ArithmeticError("операнд должен быть числом")

    def __add__(self, other):
        self.__veryfy_value(other)
        return ListMath([x + other for x in self.lst_math])

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.__veryfy_value(other)
        self.lst_math = [x + other for x in self.lst_math]
        return self

    def __sub__(self, other):
        self.__veryfy_value(other)
        return ListMath([x - other for x in self.lst_math])

    def __rsub__(self, other):
        return ListMath([other - x for x in self.lst_math])

    def __isub__(self, other):
        self.__veryfy_value(other)
        self.lst_math = [x - other for x in self.lst_math]
        return self

    def __mul__(self, other):
        self.__veryfy_value(other)
        return ListMath([x * other for x in self.lst_math])

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.__veryfy_value(other)
        self.lst_math = [x * other for x in self.lst_math]
        return self

    def __truediv__(self, other):
        self.__veryfy_value(other)
        return ListMath([x / other for x in self.lst_math])

    def __rtruediv__(self, other):
        return ListMath([other / x for x in self.lst_math])

    def __itruediv__(self, other):
        self.__veryfy_value(other)
        self.lst_math = [x / other for x in self.lst_math]
        return self