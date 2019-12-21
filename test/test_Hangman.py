import unittest
from src.Hangman import check

class HangmanTests(unittest.TestCase):
  def test_check_if_letter_is_in_word(self):
    containsLetter = check("Christian", "C")
    self.assertEqual(containsLetter, True)

  def test_when_all_letter_are_guessed_they_all_return_true(self):
    for letter in "Christian":
      self.assertTrue(check("Christian", letter))

if __name__ == '__main__':
    unittest.main()