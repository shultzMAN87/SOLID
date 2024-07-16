import math

# Базовый класс
class Shape:
    # Атрибут класса
    count = 0

    # Это конструктор класса
    def __init__(self, x, y, z: int, color, material):
        self.x = int(x)  # неявная типизация
        self.y = y
        self.z = z
        self.color = self._validate_color(color)
        self._material = material  # Используем приватный атрибут для material
        Shape.count += 1  # Увеличиваем атрибут класса

    # приватный метод "_" перед именем метода
    def _validate_color(self, value):
        if not isinstance(value, str):
            raise ValueError('Цвет должен быть строкой')
        return value

    def get_basic_point(self):
        return {'x': self.x, 'y': self.y, 'z': self.z}

    def get_nature_material(self) -> str:
        if self._material in ['steel', 'cooper', 'aluminium']:
            return 'metal'
        else:
            return 'unknown'

    # Геттер
    @property
    def material(self):
        return self._material

    # Сеттер
    @material.setter
    def material(self, value):
        if not isinstance(value, str):
            raise ValueError('Материал задается строкой')
        self._material = value  # устанавливаем значение для приватного атрибута

    # Представление
    def __str__(self):
        return f'x={self.x} y={self.y} z={self.z} colour={self.color} material={self.material} count={Shape.count}'


# класс-наследник
class Cylinder(Shape):
    def __init__(self, x, y, z, color, material, radius=1, height=1):
        super().__init__(x, y, z, color, material)
        self.radius = radius
        self.height = height

    # переопределение метода
    def get_basic_point(self):
        return {'x': self.x, 'y': self.y}

    def increase_count(self):
        Shape.count += 1

    def cylinder_volume(self):
        return pow(self.radius, 2) * math.pi * self.height

    def get_nature_material(self) -> str:
        if self._material == 'wood':
            return 'wood'
        else:
            return 'metal'


# создание класса Shape
shape = Shape(8, 7, 15, 'red', 'wood')
print(shape)

shape = Cylinder(5, 5, 3, 'blue', 'steel')
print(shape.__dir__())

# print(shape.get_basic_point())
#
# # создание экземпляра класса Cylinder
# cylinder = Cylinder(5, 5, 3, 'blue', 'steel')
# cylinder.increase_count() # метод базового класса, не реализован в наследнике
# print(cylinder.get_basic_point())
# print(cylinder)
#
# try:
#     cylinder.material = 15
#
#     print(cylinder)
#
#     print(f'Объем цилиндра равен: {cylinder.cylinder_volume()}')
# except Exception as e:
#     print(f'Ошибка: {e}')
#
# cylinder1 = Cylinder(5, 8, 3, 'blue', 'steel')
# print(cylinder1)
# print(f'Объем цилиндра #2 равен: {cylinder.cylinder_volume()}')
