def check(letters, guess):
  return letters[guess]

def get_input():
  return input("What's your guess? ")

def game_turn(letters_left_to_guess, guessed_letters):
  guess = get_input().lower()
  if guess in guessed_letters:
    print("You already guessed '{}'! Try again".format(guess))
    return guess
  elif check(letters_left_to_guess, guess):
    print("Good job! '{}' is in the word".format(guess))
    letters_left_to_guess[guess] = False
    guessed_letters.add(guess)
    return guess
  else:
    print("Tough luck, '{}' is not the word".format(guess))
    return False

def createLookupDict(word):
  letters = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', False)
  for letter in word.lower():
    letters[letter] = True
  return letters

def game_loop(word):
  misses = 0
  letters_left_to_guess = createLookupDict(word)
  guessed_letters = set()
  so_far = list('_' * len(word))
  print("".join(so_far))
  while misses < 3:
    result = game_turn(letters_left_to_guess, guessed_letters)
    if result:
      indices = [pos for pos, char in enumerate(word) if char == result]
      for index in indices:
        so_far[index] = result
      if all(not value for value in letters_left_to_guess.values()):
        return True
    else:
      misses+=1
    print("".join(so_far))
  return False