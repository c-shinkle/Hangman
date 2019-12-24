import unittest
from unittest.mock import patch
from src.Hangman import check
from src.Hangman import game_turn

class HangmanTests(unittest.TestCase):
  def test_when_letter_is_guessed_it_returns_true(self):
    containsLetter = check("Christian", "C")
    self.assertTrue(containsLetter)

  def test_when_all_letter_are_guessed_they_all_return_true(self):
    for letter in "Christian":
      self.assertTrue(check("Christian", letter))

  @patch("src.Hangman.get_input", return_value="C")
  def test_when_user_guesses_letter_game_checks_letter(self, input):
    self.assertTrue(game_turn("Christian"))
  
  
if __name__ == '__main__':
    unittest.main()