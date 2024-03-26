# class Position:
#     def __init__(self, x: float, y: float) -> None:
#         self._x = x
#         self._y = y

#     def get_x(self) -> float:
#         return self._x

#     def get_y(self) -> float:
#         return self._y

#     def set_x(self, value: float) -> None:
#         self._x = value

#     def set_y(self, value: float) -> None:
#         self._y = value


# coord = Position(x=10.1, y=11.1)

# print(coord.get_x())
# print(coord.get_y())

# coord.set_x(value=15.2)
# coord.set_y(value=13.2)

# print(coord.get_x())
# print(coord.get_y())


# from random import randint


# class Position:
#     def __init__(self, x: float, y: float) -> None:
#         self._position_x = x
#         self._position_y = y

#     @property
#     def position_x(self):
#         print("Getting position x ")
#         return self._position_x

#     @position_x.setter
#     def position_x(self, value: float):
#         print("Setting position x ")
#         random_numb = randint(0, 100)
#         self._position_x = value * random_numb

#     @property
#     def position_y(self):
#         print("Getting position y ")
#         return self._position_y

#     @position_y.setter
#     def position_y(self, value: float):
#         print("Setting position y ")
#         random_numb = randint(0, 100)
#         self._position_y = value * random_numb

#     @position_x.deleter
#     def position_x(self):
#         print("Deleting position x ")
#         del self._position_x

#     @position_y.deleter
#     def position_y(self):
#         print("Deleting position y ")
#         del self._position_y


# cord = Position(x=12.1, y=11.1)

# print(cord.position_x, cord.position_y)
# cord.position_x = 15.3
# cord.position_y = 17.3
# print(round(cord.position_x, 2), round(cord.position_y, 2))

# del cord.position_y
# del cord.position_x

# cord.position_x = 11.1
# cord.position_y = 11.1

# print(round(cord.position_x, 2), round(cord.position_y, 2))