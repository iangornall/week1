def create_words_list(sentence):
  words = []
  word = ''
  for i in range(len(sentence)):
    letter = sentence[i]
    if letter.isalpha():
      word += letter
    if letter == ' ' or i == len(sentence) - 1:
      words.append(word)
      word = ''
  return words