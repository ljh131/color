import unittest
from color import *

class TestColorMethods(unittest.TestCase):
	def assert_get_color_each(self, test_value):
		actual = get_color(test_value)
		
		if test_value.startswith('r'):
			expected = RED
		elif test_value.startswith('g'):
			expected = GREEN
		elif test_value.startswith('y'):
			expected = YELLOW 
		elif test_value.startswith('b'):
			expected = BLUE
		elif test_value.startswith('m'):
			expected = MAGENTA
		elif test_value.startswith('c'):
			expected = CYAN
		elif test_value.startswith('w'):
			expected = WHITE
		else:
			expected = WHITE		
		 
		self.assertEqual(expected, actual)
		
	def test_get_color(self):
		test_values_start_letter_it_self = ['r', 'g', 'y', 'b', 'm', 'c', 'w']
		test_values_full_text_starting_with_expected_letter = ['red', 'green', 'yello', 'blue', 'magenta', 'cyan', 'white']
		test_values_not_expected = ['aasdf', 'kasdg', 'tss']
		for test_value in test_values_start_letter_it_self:
			self.assert_get_color_each(test_value)			
			
		for test_value in test_values_full_text_starting_with_expected_letter:
			self.assert_get_color_each(test_value)
			
		for test_value in test_values_not_expected:
			self.assert_get_color_each(test_value)

if __name__ == '__main__':
    unittest.main()
 
