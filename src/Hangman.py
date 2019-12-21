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