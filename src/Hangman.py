from typing import Optional, Set


def game_turn(letters_left_to_guess: Set[str], guessed_letters: Set[str]) -> Optional[str]:
    guess = input("What's your guess? ").lower()
    if guess in guessed_letters:
        print("You already guessed '{}'! Try again".format(guess))
        return guess
    elif guess in letters_left_to_guess:
        print("Good job! '{}' is in the word".format(guess))
        letters_left_to_guess.remove(guess)
        guessed_letters.add(guess)
        return guess
    else:
        print("Tough luck, '{}' is not the word".format(guess))
        return None


def game_loop(secret_word: str) -> bool:
    secret_word = secret_word.lower()
    misses: int = 0
    letters_left_to_guess: Set[str] = set(char for char in secret_word.lower())
    guessed_letters: Set[str] = set()
    so_far = list('_' * len(secret_word))

    while misses < 3:
        print("".join(so_far))
        letter = game_turn(letters_left_to_guess, guessed_letters)

        if letter is not None:
            indices = list(pos for pos, char in enumerate(secret_word) if char == letter)
            for index in indices:
                so_far[index] = letter
            if len(letters_left_to_guess) == 0:
                print("Congratulations, you win! The word was {}".format(secret_word))
                return True
        else:
            misses += 1
    return False


if __name__ == '__main__':
    word = 'adage'
    print("Variable type:", type(word[0]))
    game_loop(word)
