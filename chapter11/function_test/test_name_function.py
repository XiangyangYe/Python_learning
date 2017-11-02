import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):

	def test_first_last_name(self):
		formatted_name = get_formatted_name('Janis', 'Joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_middle_last_name(self):
		formatted_name = get_formatted_name('Ye', 'Yang', 'Xiang')
		self.assertEqual(formatted_name, 'Ye Xiang Yang')

unittest.main()