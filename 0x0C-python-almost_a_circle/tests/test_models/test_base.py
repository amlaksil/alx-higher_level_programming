#!/usr/bin/python3
"""
This module consists of all the possible
test conditions for the class `Base`
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import pycodestyle


class TestBaseClass(unittest.TestCase):
    """This test class contains all test methods """
    def setUp(self):
        """Invoked for each tests """
        Base._Base__nb_objects = 0

    def test_id_attr(self):
        """Make sure if id is None it should be incremented by one """
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
        """Make sure the private class attribute is not accessable """
        b5 = Base()
        with self.assertRaises(AttributeError):
            b5.__nb_objects

    def test_to_json_string(self):
        """Check JSON string representation """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = json.dumps([dictionary])
        json_dictionary = r1.to_json_string([dictionary])
        self.assertTrue(json_string == json_dictionary)

        json_dictionary = r1.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')

    def test_Rectangle_save_to_file(self):
        """Check file """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary_1 = r1.to_dictionary()
        r2 = Rectangle(2, 4)
        dictionary_2 = r2.to_dictionary()
        dict_list_1 = [dictionary_1, dictionary_2]
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as f:
            dict_list_2 = json.loads(f.read())
        self.assertTrue(dict_list_1 == dict_list_2)

    def test_Square_save_to_file(self):
        """Check file """
        s1 = Square(10, 7, 2, 2)
        dictionary_1 = s1.to_dictionary()
        s2 = Square(5, 4, 3, 3)
        dictionary_2 = s2.to_dictionary()
        dict_list_1 = [dictionary_1, dictionary_2]
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as f:
            dict_list_2 = json.loads(f.read())
        self.assertTrue(dict_list_1 == dict_list_2)

    def test_Rectangle_save_to_file_not_empty(self):
        """Check file"""
        Rectangle.save_to_file([Rectangle(1, 2)])
        
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, '[{"x": 0, "y": 0, "id": 1, "height": 2, "width": 1}]')
        
    def test_Rectangle_save_to_file_none(self):
        """Check file"""
        r1 = Rectangle(10, 5)
        Rectangle.save_to_file(None)
        
        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertEqual(content, '[]')
        
    def test_Rectangle_save_to_file_empty(self):
        """Check file"""
        r1 = Rectangle(10, 5)
        Rectangle.save_to_file(None)
        
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, '[]')
        
    def test_Square_save_to_file_none(self):
        """Check file"""
        s1 = Square(10, 5)
        Square.save_to_file(None)
        
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertEqual(content, '[]')

    def test_Square_save_to_file_empty(self):
        """Check file"""
        Square.save_to_file([])
        
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content, '[]')

    def test_Square_save_to_file_not_empty(self):
        """Check file"""
        Square.save_to_file([Square(1)])
        
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content, '[{"id": 1, "x": 0, "size": 1, "y": 0}]')

    def test_from_json_string(self):
        """Check a list of JSON string """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
            ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(list_input == list_output)

        list_output = Rectangle.from_json_string(None)
        self.assertTrue(list_output == [])

    def test_create(self):
        """Check create """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        """Check file """
        s1 = Square(5)
        s2 = Square(7, 9, 1)

        list_of_instance_1 = [s1, s2]
        Square.save_to_file(list_of_instance_1)
        list_of_instance_2 = Square.load_from_file()

        self.assertEqual(str(list_of_instance_1[0]), str(list_of_instance_2[0]))
        self.assertEqual(str(list_of_instance_1[1]), str(list_of_instance_2[1]))

    def test_pycodestyle(self):
        """Check PEP 8 style """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")
