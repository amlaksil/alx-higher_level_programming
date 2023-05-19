#!/usr/bin/python3
"""Rectangle class test module"""
from io import StringIO
import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
import pycodestyle


class TestRectangleClass(unittest.TestCase):
    """Tests Rectangle class"""
    def setUp(self):
        """Invoked for each test """
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Check proper instance is created """
        r = Rectangle(2, 10)
        self.assertIsInstance(r, Rectangle)

    def test_subclass(self):
        """Check Rectangle class is a subclass of Base class """
        self.assertEqual(True, issubclass(Rectangle, Base))

    def test_rectangle_id(self):
        """Test id """
        r1 = Rectangle(20, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_rectangle_parameter(self):
        """Make sure all rectangle parameter is accessable """
        r = Rectangle(3, 5)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_access_private_attrs(self):
        """Make sure all attributes are private """
        r = Rectangle(3, 5, 1, 0, 12)
        str_f = "'Rectangle' "
        str_m = "object has no attribute "
        str_l = "'_TestRectangleClass__width'"

        with self.assertRaisesRegex(AttributeError, str_f + str_m + str_l):
            r.__width

        str_l = "'_TestRectangleClass__height"
        with self.assertRaisesRegex(AttributeError, str_f + str_m + str_l):
            r.__height

        str_l = "'_TestRectangleClass__x'"
        with self.assertRaisesRegex(AttributeError, str_f + str_m + str_l):
            r.__x

        str_l = "'_TestRectangleClass__y'"
        with self.assertRaisesRegex(AttributeError, str_f + str_m + str_l):
            r.__y

    def test_width(self):
        """Make sure error is raised if height is not integer """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("3", 2)

    def test_height(self):
        "Make sure error is raised if height is not integer """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(3, "2")

    def test_x(self):
        "Make sure error is raised if x is not integer """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(3, 2, "4", 2)

    def test_y(self):
        "Make sure error is raised if y is not integer """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(3, 2, 4, "2")

    def test_is_width_positive(self):
        """Make sure error is raised if width is less than zero """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-3, 2, 4, 7)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 2)

    def test_is_height_positive(self):
        """Make sure error is raised if width is less than zero """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(3, -2, 4, 7, 21)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_is_x_greater_than_zero(self):
        """Make sure error is raised if x is not >= 0"""

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(3, 2, -2, 7, 21)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 2, -3)

    def test_is_y_greater_than_orEqualto_zero(self):
        """Make sure error is raised if y is not >= 0"""

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(3, 2, 4, -7, 5)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        """Area of rectangle """
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)

        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_display(self):
        """Test printed output """
        r = Rectangle(4, 6)
        f_str = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), f_str)

        r = Rectangle(2, 2)
        f_str = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), f_str)

    def test_str(self):
        """Test __str__"""
        r = Rectangle(4, 6, 2, 1, 12)
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

        r = Rectangle(5, 5, 1)
        with patch('sys.stdout', new=StringIO()) as out:
            print(r)
            self.assertEqual(out.getvalue(), "[Rectangle] (1) 1/0 - 5/5\n")

    def test_display_update(self):
        """Test printed output """
        r = Rectangle(2, 3, 2, 2)
        f_str = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), f_str)

        r = Rectangle(3, 2, 1, 0)
        f_str = " ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), f_str)

    def test_update(self):
        """Make sure update is successful for no-keyword argument """
        r1 = Rectangle(10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as out:
            r1.update(89)
            print(r1)
            fs = "[Rectangle] (89) 10/10 - 10/10\n"
            self.assertEqual(out.getvalue(), fs)

        with patch('sys.stdout', new=StringIO()) as out:
            r1.update(89, 2)
            print(r1)
            fs = "[Rectangle] (89) 10/10 - 2/10\n"
            self.assertEqual(out.getvalue(), fs)

        with patch('sys.stdout', new=StringIO()) as out:
            r1.update(89, 2, 3)
            print(r1)
            fs = "[Rectangle] (89) 10/10 - 2/3\n"
            self.assertEqual(out.getvalue(), fs)

        with patch('sys.stdout', new=StringIO()) as out:
            r1.update(89, 2, 3, 4)
            print(r1)
            fs = "[Rectangle] (89) 4/10 - 2/3\n"
            self.assertEqual(out.getvalue(), fs)

        with patch('sys.stdout', new=StringIO()) as out:
            r1.update(89, 2, 3, 4, 5)
            print(r1)
            fs = "[Rectangle] (89) 4/5 - 2/3\n"
            self.assertEqual(out.getvalue(), fs)

    def test_update_with_key_worded_argument(self):
        """Make sure update is successful """
        r1 = Rectangle(10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as out:
            r1.update(height=1)
            print(r1)
            self.assertEqual(out.getvalue(), "[Rectangle] (1) 10/10 - 10/1\n")

        with patch('sys.stdout', new=StringIO()) as out:
            r1.update(width=1, x=2)
            print(r1)
            self.assertEqual(out.getvalue(), "[Rectangle] (1) 2/10 - 1/1\n")

        with patch('sys.stdout', new=StringIO()) as out:
            r1.update(y=1, width=2, x=3, id=89)
            print(r1)
            self.assertEqual(out.getvalue(), "[Rectangle] (89) 3/1 - 2/1\n")

        with patch('sys.stdout', new=StringIO()) as out:
            r1.update(x=1, height=2, y=3, width=4)
            print(r1)
            self.assertEqual(out.getvalue(), "[Rectangle] (89) 1/3 - 4/2\n")

    def test_to_dictionary(self):
        """Check dictionary """
        r1 = Rectangle(10, 2, 1, 9)
        dic_rep = "{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}\n"
        with patch('sys.stdout', new=StringIO()) as out:
            dict_ = r1.to_dictionary()
            print(dict_)
            self.assertEqual(out.getvalue(), dic_rep)

    def test_pycodestyle(self):
        """Check PEP 8 style"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")
