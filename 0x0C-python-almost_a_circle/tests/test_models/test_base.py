#!/usr/bin/python3
"""this file is created to test base.py file"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test Base class"""
    pass

    def setUp(self):
        """Test private class attribute"""
        Base.__nb_objects = 0

    def test_init(self):
        """Test init"""
        test1 = Base()
        self.assertEqual(type(test1), Base)
        test2 = Base(8)
        self.assertEqual(type(test2), Base)

    def test_id(self):
        """Test id"""
        test1 = Base()
        self.assertEqual(test1.id, 1)
        test2 = Base(8)
        self.assertEqual(test2.id, 8)

    def test_to_json(self):
        """Test from Python to JSON"""
        test1 = Base.to_json_string([])
        self.assertEqual(test1, "[]")
        test2 = Base.to_json_string(None)
        self.assertEqual(test2, "[]")
        test3 = Base.to_json_string([{'width': 2}])
        self.assertEqual(test3, '[{"width": 2}]')
        test4 = Base.to_json_string([{'id': 10, 'x': 1}])
        self.assertEqual(test4, '[{"id": 10, "x": 1}]')

    def test_from_json(self):
        """Test from JSON to Python"""
        test1 = Base.from_json_string("[]")
        self.assertEqual(test1, [])
        test2 = Base.from_json_string(None)
        self.assertAlmostEqual(test2, [])
        test3 = Base.from_json_string('[{"id": 10, "width": 3, "height": 6}]')
        self.assertEqual(test3, [{"id": 10, "width": 3, "height": 6}])
        self.assertEqual(type(test3), list)
