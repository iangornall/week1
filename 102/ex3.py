def main():
  user_words = madlib_input()
  print build_sentence(user_words)

def madlib_input():
  user_words = {}
  print """Please fill in the blanks below:
  ____(name)____ likes to eat ____(food)____ ____(place phrase)____."""
  user_words['name'] = raw_input('Choose a name: ')
  user_words['food'] = raw_input('Choose a food: ')
  user_words['place'] = raw_input('Choose a place: ')
  return user_words

def build_sentence(words):
  return "%s likes to eat %s %s." % (words['name'], words['food'], words['place'])
  
main()
