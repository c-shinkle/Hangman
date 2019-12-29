def check(letters, guess):
  return letters[guess]

def get_input():
  return input("What's your guess? ")

def game_turn(letters):
  guess = get_input()
  if check(letters, guess):
    print("Good job! '{}' is in the word".format(guess))
    letters[guess] = False
    return True
  else:
    print("Tough luck, '{}' is not the word".format(guess))
    return False

def createLookupDict(word):
  letters = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', False)
  for letter in word:
    letters[letter] = True
  return letters

def game_loop(word):
  misses = 0
  letters = createLookupDict(word)
  while (misses < 3):
    correct = game_turn(letters)
    if (correct):
      if (all(not value for value in letters.values())):
        return True
    else:
      misses+=1
  return False