#!/usr/bin/python3
"""this file is created to test square.py file"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square class"""
    pass

    def setUp(self):
        """Test private class attribute"""
        Base._Base__nb_objects = 0

    def test_str(self):
        """Test str"""
        test = Square(6).area()
        self.assertEqual(test, 36)

    def test_update1(self):
        """Test update args"""
        test = Square(57)
        self.assertEqual(test.size, 57)
        test.update(5, 6, 1, 7)
        self.assertEqual(test.id, 5)
        self.assertEqual(test.size, 6)
        self.assertEqual(test.x, 1)
        self.assertEqual(test.y, 7)

    def test_update2(self):
        """Test update kwargs"""
        test = Square(57)
        test.update(x=3)
        self.assertEqual(test.x, 3)
        test.update(id=2)
        self.assertEqual(test.id, 2)
        test.update(size=9)
        self.assertEqual(test.height, 9)
        test.update(y=1)
        self.assertEqual(test.y, 1)

    def test_dictionary(self):
        """Test Dictionary"""
        test = Square(6, 2, 3, 1).to_dictionary()
        result = {'id': 1, 'x': 2, 'size': 6, 'y': 3}
        self.assertEqual(test, result)
