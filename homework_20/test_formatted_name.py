import unittest

from formatted_name import formatted_name


class TestFormattedName(unittest.TestCase):

    def test_first_last_name(self):
        self.assertEqual(formatted_name('Igor', 'Samarsky'), 'Igor Samarsky')

    def test_first_middle_last_name(self):
        self.assertEqual(formatted_name('jane', 'smith', 'mary'), 'Jane Mary Smith')

    def test_first_last_name_with_empty_middle_name(self):
        self.assertEqual(formatted_name('Jane', 'Doe', ''), 'Jane Doe')

    def test_first_last_name_with_multiple_spaces(self):
        self.assertNotEqual(formatted_name('  Vasiliy   ', '   Laptev '), 'Jane Smith')

    def test_uppercase(self):
        self.assertEqual(formatted_name('ARTEM', 'KRASULIAK'), 'Artem Krasuliak')

    def test_empty_first_and_last_name(self):
        self.assertEqual(formatted_name('', ''), ' ')

    def test_numbers(self):
        with self.assertRaises(TypeError):
            formatted_name(2, 4)

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            formatted_name([], [])

    def test_string_and_number(self):
        with self.assertRaises(TypeError):
            formatted_name("Igor", 4)
