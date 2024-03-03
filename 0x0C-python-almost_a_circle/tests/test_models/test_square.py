#!/usr/bin/python3
"""Test module for `Square` class """
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
import pycodestyle


class TestSquareClass(unittest.TestCase):
    """Test class for Square class """
    def setUp(self):
        """Invoked for each test """
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Make sure s1 is an instance of squre class"""
        s1 = Square(2, 10, 8)
        self.assertIsInstance(s1, Square)

    def test_subclass(self):
        """Check Rectangle class is a subclass of Base class """
        self.assertEqual(True, issubclass(Square, Rectangle))

    def test_square_parameters(self):
        """Make sure all square parameter is accessable """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_square_parameters_1(self):
        """Make sure all square parameter is accessable """
        s1 = Square(3, 1, 3, 4)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.height, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 4)

    def test_size(self):
        """Make sure size is integer """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square("5")

    def test_x(self):
        """Make sure error is raised if x is not integer """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(5, "2", 4)

    def test_y(self):
        """Make sure error is raised if y is not integer """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s2 = Square(5, 2, "4")

    def test_is_size_greater_than_zero(self):
        """Make sure size is greater than zero """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1 = Square(0)

    def test_size_is_positive(self):
        """Make sure size is positive"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1 = Square(-1)

    def test_is_x_greater_than_or_equal_to_zero(self):
        """Make sure error is raised if x is not less than or equal to zero"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1 = Square(5, -2, 4)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1 = Square(1, -2)

    def test_is_y_greater_than_orEqualto_zero(self):
        """Make sure error is raised if y is not less than or equal to zero """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1 = Square(5, 2, -4)

    def test_str(self):
        """Test __str__ """
        s1 = Square(3, 1, 3)
        with patch('sys.stdout', new=StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), "[Square] (1) 1/3 - 3\n")

        s1 = Square(5, 2, 6)
        with patch('sys.stdout', new=StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), "[Square] (2) 2/6 - 5\n")

    def test_area(self):
        """Check area of square """
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_display(self):
        """Check display """
        s1 = Square(5)
        f_str = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            s1.display()
            self.assertEqual(out.getvalue(), f_str)

        s1 = Square(2, 2)
        f_str = "  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as out:
            s1.display()
            self.assertEqual(out.getvalue(), f_str)

        s1 = Square(3, 1, 3)
        f_str = "\n\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as out:
            s1.display()
            self.assertEqual(out.getvalue(), f_str)

    def test_update(self):
        """Make sure updated is done """
        s1 = Square(5)
        s1.update(10)
        with patch('sys.stdout', new=StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), "[Square] (10) 0/0 - 5\n")

        s1.update(1, 2)
        with patch('sys.stdout', new=StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), "[Square] (1) 0/0 - 2\n")

        s1.update(1, 2, 3)
        with patch('sys.stdout', new=StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), "[Square] (1) 3/0 - 2\n")

        s1.update(1, 2, 3, 4)
        with patch('sys.stdout', new=StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), "[Square] (1) 3/4 - 2\n")

        s1.update(x=12)
        with patch('sys.stdout', new=StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), "[Square] (1) 12/4 - 2\n")

        s1.update(size=7, y=1)
        with patch('sys.stdout', new=StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), "[Square] (1) 12/1 - 7\n")

        s1.update(size=7, id=89, y=1)
        with patch('sys.stdout', new=StringIO()) as out:
            print(s1)
            self.assertEqual(out.getvalue(), "[Square] (89) 12/1 - 7\n")

    def test_to_dictionary(self):
        """Check dictionary """
        s1 = Square(10, 2, 1)
        s1_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dict, s1_dictionary)

        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertFalse(s1 == s2)

    def test_Square_save_to_file_none_2(self):
        """Check file"""
        r1 = Square(10, 5)
        Square.save_to_file(None)

        with open("Square.json", "r") as f:
            content = f.read()
            self.assertEqual(content, '[]')
            
    def test_pycodestyle(self):
        """Check PEP 8 style """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")
