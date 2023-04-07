#!/usr/bin/python3
"""Unittest for max_integer({..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        """Make sure the maximum value is equal to the value intended"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, -3, 4, 9, 8]), 9)
        self.assertEqual(max_integer([6, -3, 0, 2, 1]), 6)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([-27, -30]), -27)
        self.assertEqual(max_integer([0, 0]), 0)

    def test_types(self):
        """Make sure type errors are raised when necessary """
        self.assertRaises(TypeError, max_integer, ['addgg', 3, -23, 'dssss'])
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, "abc")
        self.assertRaises(TypeError, max_integer, 123)

    def test_return(self):
        """Make sure it returns None when the list is empty """
        self.assertEqual(max_integer([]), None)
