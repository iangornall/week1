from histogram import create_histogram

def init():
  word = raw_input('Word: ')
  print create_histogram(word)

init()