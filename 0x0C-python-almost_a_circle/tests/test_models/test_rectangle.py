#!/usr/bin/python3
"""this file is created to test rectangle.py file"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""
    pass

    def setUp(self):
        """Test private class attribute"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test id"""
        test1 = Rectangle(8, 5)
        self.assertEqual(test1.id, 1)
        test2 = Rectangle(6, 9, 4)
        self.assertEqual(test2.id, 2)
        test2_1 = Rectangle(6, 9, id=4)
        self.assertEqual(test2_1.id, 4)
        test3 = Rectangle(1, 2, 2, 5)
        self.assertEqual(test3.id, 3)
        test4 = Rectangle(7, 3, 1, 4, 59)
        self.assertEqual(test4.id, 59)

    def test_ValidationType(self):
        """Test ValidationType"""
        with self.assertRaises(TypeError):
            Rectangle("1", 1)
        with self.assertRaises(TypeError):
            Rectangle(9, "G")
        with self.assertRaises(TypeError):
            Rectangle(1, 3.65)
        with self.assertRaises(TypeError):
            Rectangle(3, None)
        with self.assertRaises(TypeError):
            Rectangle(5, 1, "M", 8)
        with self.assertRaises(TypeError):
            Rectangle(4, 1, 6, None)

    def test_ValidationValue(self):
        """Test ValidationValue"""
        with self.assertRaises(ValueError):
            Rectangle(-2, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -6)
        with self.assertRaises(ValueError):
            Rectangle(5, 0)
        with self.assertRaises(ValueError):
            Rectangle(7, 4, -6)
        with self.assertRaises(ValueError):
            Rectangle(1, 5, 3, -1)
        with self.assertRaises(ValueError):
            Rectangle(0, 4, 0, 5)

    def test_area(self):
        """Test area"""
        test1 = Rectangle(3, 5).area()
        self.assertEqual(test1, 15)

    def test_str(self):
        """Test str"""
        test1 = Rectangle(1, 4, 8, 5, 97).__str__()
        self.assertEqual(test1, "[Rectangle] (97) 8/5 - 1/4")
        test2 = Rectangle(3, 9, y=2).__str__()
        self.assertEqual(test2, "[Rectangle] (1) 0/2 - 3/9")

    def test_update1(self):
        """Test Update args"""
        test = Rectangle(89, 1, 2, 3, 4)
        test.update(8, 6, 5, 1, 7)
        self.assertEqual(test.id, 8)
        self.assertEqual(test.width, 6)
        self.assertEqual(test.height, 5)
        self.assertEqual(test.x, 1)
        self.assertEqual(test.y, 7)

    def test_update2(self):
        """Test Update kwargs"""
        test = Rectangle(5, 9, 3, 3, 1)
        test.update(x=6)
        self.assertEqual(test.x, 6)
        test.update(id=12)
        self.assertEqual(test.id, 12)
        test.update(height=30)
        self.assertEqual(test.height, 30)
        test.update(width=21)
        self.assertEqual(test.width, 21)
        test.update(y=48)
        self.assertEqual(test.y, 48)

    def test_dictionary(self):
        """Test Dictionary"""
        test = Rectangle(6, 2, 3, 1).to_dictionary()
        result = {'x': 3, 'y': 1, 'id': 1, 'height': 2, 'width': 6}
        self.assertEqual(test, result)
        test = Rectangle(9, 7, 4, 8, 60).to_dictionary()
        result = {'x': 4, 'y': 8, 'id': 60, 'height': 7, 'width': 9}
        self.assertEqual(test, result)
