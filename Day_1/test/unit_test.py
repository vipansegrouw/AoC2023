import unittest
from parameterized import parameterized

from src.utils import get_first_and_last_number_from_string


class CalibrationCheckerTest(unittest.TestCase):
    @parameterized.expand([
        ("asdhj1ahfjjdskkh2ahajkhdshfkj5hjashjkasdfjkh3hjasdjhk", 13),
        ("sshnxbjrt1", 11)
    ])
    def test_get_first_and_last_number_from_string(self, input_string, expected):
        actual = get_first_and_last_number_from_string(input_string)
        self.assertEqual(expected, actual)

    @parameterized.expand([
        ("asdfaeightauiafuiew21837ainasdf3ahfjd", 83),
        ("stwoneshnxbjrt1asd", 21)
    ])
    def test_get_first_and_last_number_from_string_when_spelled(self, input_string, expected):
        actual = get_first_and_last_number_from_string(input_string)
        self.assertEqual(expected, actual)

    def test_throws_exception_when_no_numbers(self):
        self.assertRaises(Exception, get_first_and_last_number_from_string, "asdjfhauwiefhasldfjklh")


if __name__ == '__main__':
    unittest.main()
