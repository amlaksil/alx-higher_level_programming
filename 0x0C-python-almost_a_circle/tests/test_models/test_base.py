#!/usr/bin/python3
"""
This module consists of all the possible
test conditions for the class `Base`
"""
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    """This test class contains all test methods """
    def setUp(self):
        """Invoked for each tests """
        Base._Base__nb_objects = 0

    def test_id_attr(self):
        """Test id """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_not_none(self):
        """If id is not None """
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base(7)
        self.assertEqual(b4.id, 7)

    def test_class_attr(self):
        """Access private class attribute """
        b5 = Base()
        with self.assertRaises(AttributeError):
            b5.__nb_objects
