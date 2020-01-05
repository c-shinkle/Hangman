def check(letters, guess):
  return guess in letters

def get_input():
  return input("What's your guess? ")

def game_turn(letters_left_to_guess, guessed_letters):
  guess = get_input().lower()
  if guess in guessed_letters:
    print("You already guessed '{}'! Try again".format(guess))
    return guess
  elif check(letters_left_to_guess, guess):
    print("Good job! '{}' is in the word".format(guess))
    letters_left_to_guess.remove(guess)
    guessed_letters.add(guess)
    return guess
  else:
    print("Tough luck, '{}' is not the word".format(guess))
    return False

def create_lookup_set(word):
  return set(char for char in word.lower())

def create_letter_indices_list(word, letter):
  return list(pos for pos, char in enumerate(word) if char == letter)

def game_loop(word):
  misses = 0
  letters_left_to_guess = create_lookup_set(word)
  guessed_letters = set()
  so_far = list('_' * len(word))
  while misses < 3:
    print("".join(so_far))
    result = game_turn(letters_left_to_guess, guessed_letters)
    if result:
      indices = create_letter_indices_list(word, result)
      for index in indices:
        so_far[index] = result
      if not letters_left_to_guess:
        return True
    else:
      misses+=1
  return False