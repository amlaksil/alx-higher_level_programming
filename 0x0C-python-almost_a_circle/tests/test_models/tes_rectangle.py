#!/usr/bin/python3
"""Rectangle class test file module """
import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleClass(unittest.TestCase):
    """Tests Rectangle class"""
    def setUp(self):
        """Invoked for each test """
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        """before defining """
        r1 = Rectangle(20, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_rectangle_parameter(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
