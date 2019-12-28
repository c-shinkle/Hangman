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
    print("Good job! {} is in the word".format(guess))
    return True
  else:
    print("Tough luck, {} is not the word".format(guess))
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