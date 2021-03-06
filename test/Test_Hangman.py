import unittest
from unittest import TestCase
from unittest.mock import patch, call

from src.Hangman import game_turn, game_loop, create_lookup_set


class HangmanTests(TestCase):

    @patch('builtins.input', return_value='c')
    def test_when_user_guesses_input(self, mock_get_input):
        self.assertTrue(game_turn(create_lookup_set('christian'), set()))
        self.assertTrue(mock_get_input.called)

    @patch('builtins.input', side_effect=['a', 'b', 'c'])
    def test_when_user_guesses_three_wrong_letters_game_is_over(self, mock_get_input):
        self.assertFalse(game_loop("xyz"))
        self.assertEqual(3, mock_get_input.call_count)

    @patch('builtins.input', side_effect=['x', 'y', 'z'])
    def test_when_user_guesses_all_letters_game_is_over(self, mock_get_input):
        self.assertTrue(game_loop('xyz'))
        self.assertEqual(3, mock_get_input.call_count)

    @patch('builtins.input', return_value='X')
    def test_when_user_guesses_uppercase_letters_game_checks_lower(self, mock_get_input):
        self.assertTrue(game_turn(create_lookup_set('xyz'), set()))
        self.assertTrue(mock_get_input.called)

    @patch('builtins.input', side_effect=['x', 'y', 'z'])
    @patch('builtins.print')
    def test_when_game_word_has_uppercase_letters_user_can_guess_lowercase_letters(self, mock_print, mock_get_input):
        self.assertTrue(game_loop('XYZ'))
        self.assertEqual(3, mock_get_input.call_count)
        calls = [call('___'), call('x__'), call('xy_'), call('Congratulations, you win! The word was xyz')]
        mock_print.assert_has_calls(calls, any_order=True)

    @patch('builtins.input', side_effect=['x', 'y', 'x', 'z'])
    @patch('builtins.print')
    def test_when_user_enters_same_letter_multiple_times_game_tells_user(self, mock_print, mock_get_input):
        self.assertTrue(game_loop('xyz'))
        mock_print.assert_any_call("You already guessed 'x'! Try again")
        self.assertEqual(4, mock_get_input.call_count)

    @patch('builtins.input', side_effect=['x', 'y', 'z'])
    @patch('builtins.print')
    def test_when_user_begins_turn_game_tells_how_many_are_guessed_correctly(self, mock_print, mock_get_input):
        self.assertTrue(game_loop('xyz'))
        self.assertEqual(3, mock_get_input.call_count)
        mock_print.assert_any_call('___')
        mock_print.assert_any_call('x__')
        mock_print.assert_any_call('xy_')
        mock_print.assert_any_call('Congratulations, you win! The word was xyz')


if __name__ == '__main__':
    unittest.main()
