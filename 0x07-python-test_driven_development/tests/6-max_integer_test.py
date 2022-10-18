#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """a class that define unittests for max_integer([..])."""

    def test_string(self):
        """Tests a string."""
        string = "ALX"
        self.assertEqual(max_integer(string), 'X')

    def test_list_of_strings(self):
        """Tests a list of strings."""
        strings = ["Dagi", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Tests an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_ordered_list(self):
        """Tests an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Tests an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Tests a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Tests an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Tests a list with a single element."""
        one_element = [3]
        self.assertEqual(max_integer(one_element), 3)

    def test_floats(self):
        """Tests a list of floats."""
        floats = [1.53, 6.33, -9.123, 23.6, 6.0]
        self.assertEqual(max_integer(floats), 23.6)

    def test_ints_and_floats(self):
        """Tests a list of ints and floats."""
        ints_and_floats = [11.53, 20.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 20.5)


if __name__ == '__main__':
    unittest.main()
