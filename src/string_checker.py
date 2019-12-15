def check(word, guess):
  for i in range(len(word)):
    if (guess == word[i]):
      return True
  return False
