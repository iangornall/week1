from word_split import create_words_list
from histogram import create_histogram

def main():
  sentence = raw_input('Sentence: ').lower()
  words = create_words_list(sentence)
  histogram = create_histogram(words)
  print top3(histogram)

def top3(histogram):
  key_value = []
  top3 = ''
  for key in histogram:
    key_value.append([histogram[key], key])
    key_value.sort()
    key_value.reverse()
  for i in range(3):
    top3 += key_value[i][1] + ': ' + str(key_value[i][0]) + '\n'
  return top3[:-1]

main()