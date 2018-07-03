from word_split import create_words_list
from histogram import create_histogram

def main():
  sentence = raw_input('Sentence: ').lower()
  words = create_words_list(sentence)
  print create_histogram(words)

main()