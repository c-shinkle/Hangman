def check(word, guess):
  for i in range(len(word)):
    if (guess == word[i]):
      return True
  return False

def get_input():
  return input("What's your guess? ")

def game_turn(word, letters):
  guess = get_input()
  if check(word, guess):
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
    correct = game_turn(word, letters)
    if (correct):
      if (all(not value for value in letters.values())):
        return True
    else:
      misses+=1
  return False