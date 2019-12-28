def check(word, guess):
  for i in range(len(word)):
    if (guess == word[i]):
      return True
  return False

def get_input():
  return input("What's your guess? ")

def game_turn(word):
  guess = get_input()
  if check(word, guess):
    return True
  else:
    return False

def game_loop(word):
  misses = 0
  while (misses < 3):
    isSuccessful = game_turn(word)
    if (not isSuccessful):
      misses+=1
    else:
      return True
  return False