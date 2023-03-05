import os
import sys
import unittest
import string

from character_type import CharacterType
from error_message import ErrorMessage

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class TestCharacterType(unittest.TestCase):

    def setUp(self):
        self.uppercase = CharacterType(string.ascii_uppercase.split())

    def test_create_empty_condidate(self):
        expected = ErrorMessage.EMPTY_CANDIDATE.value

        with self.assertRaises(TypeError):
            self.uppercase = CharacterType()

        with self.assertRaisesRegex(ValueError, expected):
            self.uppercase = CharacterType([])

    def test_set_min_greater_than_max(self):
        expected = ErrorMessage.MIN_MAX_INVALID_RANGE.value

        for min in range(1, 10):
            with self.assertRaisesRegex(ValueError, expected):
                self.uppercase.min = min
                self.uppercase.max = min - 1

    def test_set_non_numberic_min_max(self):
        nums = ["123", "d", 'A', "$"]
        expected = ErrorMessage.MIN_MAX_NOT_NUMBERIC.value

        for num in nums:
            with self.assertRaisesRegex(ValueError, expected):
                self.uppercase.min = num

            with self.assertRaisesRegex(ValueError, expected):
                self.uppercase.max = num

    def test_set_negative_number_min_max(self):
        nums = [-1, -3, -11]
        expected = ErrorMessage.MIN_MAX_NAGATIVE.value

        for num in nums:
            with self.assertRaisesRegex(ValueError, expected):
                self.uppercase.min = num

            with self.assertRaisesRegex(ValueError, expected):
                self.uppercase.max = num

    def test_generate_characters(self):
        generate_length = self.uppercase.min
        self.uppercase.generate(generate_length)

        self.assertEqual(len(self.uppercase.characters), generate_length)

        for char in self.uppercase.characters:
            self.assertTrue(char in self.uppercase._candidate)


if __name__ == '__main__':
    unittest.main()
