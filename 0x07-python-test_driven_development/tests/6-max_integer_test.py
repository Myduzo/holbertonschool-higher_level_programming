#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list(self):
        """Empty list test"""
        self.assertEqual(max_integer([5, 0, 2, 9]), 9)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-5, -1, 0]), 0)
        self.assertEqual(max_integer([-2, -3, -7]), -2)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([-4]), -4)
        self.assertEqual(max_integer([1.5, 3.9, 4.25, 2.7]), 4.25)
    
    def test_empty(self):
        """Empty list test"""
        self.assertIsNone(max_integer([]), None)
    
    def test_error(self):
        with self.assertRaises(TypeError):
            max_integer(7)
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([4, "", 1, 6])
        with self.assertRaises(TypeError):
            max_integer([4, "x", 1, 6])
