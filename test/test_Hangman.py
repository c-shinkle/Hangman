import unittest
from src import Hangman

class HangmanTests(unittest.TestCase):
  def test_check_if_letter_is_in_word(self):
    containsLetter = Hangman.check("Christian", "C")
    self.assertEqual(containsLetter, True)

if __name__ == '__main__':
    unittest.main()