import unittest

# Базовый класс "Геометрическая фигура"
class GeometricShape:
    def area(self):
        pass

# Класс "Треугольник"
class Triangle(GeometricShape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Класс "Прямоугольник"
class Rectangle(GeometricShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Тесты
class TestGeometry(unittest.TestCase):
    def test_triangle_area(self):
        triangle = Triangle(3, 4)
        self.assertEqual(triangle.area(), 6.0)

    def test_rectangle_area(self):
        rectangle = Rectangle(5, 7)
        self.assertEqual(rectangle.area(), 35)

if __name__ == "__main__":
    unittest.main()
