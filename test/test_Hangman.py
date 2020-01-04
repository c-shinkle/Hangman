import unittest
from unittest.mock import patch, Mock, call
from src.Hangman import check, game_turn, game_loop, createLookupDict

class HangmanTests(unittest.TestCase):
  test_string = "Christian"
  def test_when_letter_is_guessed_it_returns_true(self):
    self.assertTrue(check(createLookupDict(self.test_string), "c"))

  def test_when_all_letter_are_guessed_they_all_return_true(self):
    letters = createLookupDict(self.test_string)
    for letter in self.test_string.lower():
      with self.subTest(letter=letter):
        self.assertTrue(check(letters, letter))

  @patch("src.Hangman.get_input", return_value="c")
  def test_when_user_guesses_letter_game_checks_letter(self, mock_get_input):
    self.assertTrue(game_turn(createLookupDict(self.test_string), set()))
    self.assertTrue(mock_get_input.called)
  
  @patch("src.Hangman.get_input", side_effect=['a', 'b', 'c'])
  def test_when_user_guesses_three_wrong_game_is_over(self, mock_get_input):
    self.assertFalse(game_loop("xyz"))
    self.assertEquals(3, mock_get_input.call_count)

  @patch("src.Hangman.get_input", side_effect=['x', 'y', 'z'])
  def test_when_user_guesses_all_letters_game_is_over(self, mock_get_input):
    self.assertTrue(game_loop("xyz"))
    self.assertEquals(3, mock_get_input.call_count)

  @patch("src.Hangman.get_input", return_value="x")
  def test_when_user_guesses_uppercase_letters_game_allows_it(self, mock_get_input):
    self.assertTrue(game_turn(createLookupDict("XYZ"), set()))
    self.assertTrue(mock_get_input.called)
  
  @patch("src.Hangman.get_input", side_effect=['x', 'y', 'x', 'z'])
  @patch("builtins.print")
  def test_when_user_enters_same_letter_multiple_times_game_tells_user(self, mock_print, mock_get_input):
    self.assertTrue(game_loop("xyz"))
    mock_print.assert_any_call("You already guessed 'x'! Try again")
    self.assertEquals(4, mock_get_input.call_count)

  @patch("src.Hangman.get_input", side_effect=['x', 'y', 'z'])
  @patch("builtins.print")
  def test_when_user_begins_turn_game_tells_how_many_are_guessed_correctly(self, mock_print, mock_get_input):
    self.assertTrue(game_loop("xyz"))
    mock_print.assert_any_call("___")
    mock_print.assert_any_call("x__")
    mock_print.assert_any_call("xy_")

if __name__ == '__main__':
    unittest.main()