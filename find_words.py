
# return a list contains all words in the text
def find_words(text: str):
  my_words = []
  i = 0
  len_text = len(text)

  while i < len_text:
    if text[i].isalpha():
      j = 0
      while i+j < len_text and (text[i+j].isalpha() or text[i+j] == '-'):
        j+=1
      my_words.append(text[i : i+j])
      i+=j
    i+=1
  
  return my_words

