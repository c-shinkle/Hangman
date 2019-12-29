import unittest
from unittest.mock import patch, Mock, call
from src.Hangman import check, game_turn, game_loop

class HangmanTests(unittest.TestCase):
  def test_when_letter_is_guessed_it_returns_true(self):
    self.assertTrue(check("Christian", "C"))

  def test_when_all_letter_are_guessed_they_all_return_true(self):
    for letter in "Christian":
      self.assertTrue(check("Christian", letter))

  @patch("src.Hangman.get_input", return_value="C")
  def test_when_user_guesses_letter_game_checks_letter(self, input):
    self.assertTrue(game_turn("Christian", {}))
  
  @patch("src.Hangman.get_input")
  def test_when_user_guesses_three_wrong_game_is_over(self, mock_get_input):
    mock_get_input.side_effect = ['a', 'b', 'c']
    self.assertFalse(game_loop("xyz"))

  @patch("src.Hangman.get_input")
  def test_when_user_guesses_all_letters_game_is_over(self, mock_get_input):
    mock_get_input.side_effect = ['x', 'y', 'z']
    self.assertTrue(game_loop("xyz"))

if __name__ == '__main__':
    unittest.main()