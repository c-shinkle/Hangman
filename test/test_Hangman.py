import unittest
from unittest.mock import patch, Mock, call
from src.Hangman import check, game_turn, game_loop, createLookupDict

class HangmanTests(unittest.TestCase):
  def test_when_letter_is_guessed_it_returns_true(self):
    self.assertTrue(check(createLookupDict("Christian"), "c"))

  def test_when_all_letter_are_guessed_they_all_return_true(self):
    letters = createLookupDict("Christian")
    for letter in "christian":
      self.assertTrue(check(letters, letter))

  @patch("src.Hangman.get_input", return_value="c")
  def test_when_user_guesses_letter_game_checks_letter(self, mock_get_input):
    self.assertTrue(game_turn(createLookupDict("Christian")))
  
  @patch("src.Hangman.get_input", side_effect=['a', 'b', 'c'])
  def test_when_user_guesses_three_wrong_game_is_over(self, mock_get_input):
    self.assertFalse(game_loop("xyz"))

  @patch("src.Hangman.get_input", side_effect=['x', 'y', 'z'])
  def test_when_user_guesses_all_letters_game_is_over(self, mock_get_input):
    self.assertTrue(game_loop("xyz"))

  @patch("src.Hangman.get_input", return_value="x")
  def test_when_user_guesses_uppercase_letters_game_allows_it(self, mock_get_input):
    self.assertTrue(game_turn(createLookupDict("XYZ")))

if __name__ == '__main__':
    unittest.main()