#!/usr/bin/python3
"""Unittest for max_integer({..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 6]), 6)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, -3, 4, 9, 8]), 9)

    def test_max_beginning(self):
        self.assertEqual(max_integer([6, -3, 0, 2, 1]), 6)
        self.assertEqual(max_integer([23, 3, 9, 21, 1]), 23)

    def test_max_single_element(self):
        self.assertEqual(max_integer([3]), 3)

    def test_max_all_negative_element(self):
        self.assertEqual(max_integer([-27, -30, -5, -4]), -4)
        self.assertEqual(max_integer([-5, -30, -35, 0]), -5)

    def test_max_all_same_element(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-8, -8, -8, -8]), -8)

    def test_types_list_contains_string(self):
        self.assertRaises(TypeError, max_integer, ['addgg', 3, -23, 'dss'])

    def test_types_bool(self):
        self.assertRaises(TypeError, max_integer, True)

    def test_types_string(self):
        self.assertRaises(TypeError, max_integer, "abc")

    def test_types_number(self):
        self.assertRaises(TypeError, max_integer, 123)

    def test_return(self):
        self.assertEqual(max_integer([]), None)
