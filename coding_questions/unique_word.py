'''
Write a Python function that takes a string and returns a dictionary with the count of each unique word. Ignore case and punctuation.
Example:-
input_text = "Hello world! Hello Python."
output = {"hello": 2, "world": 1, "python": 1}

''' 

def get_unique_words(input_text):

  texts = input_text.split()
  words = [''.join([word for word in text if word.isalpha()]).lower()  for text in texts] 

  result = {}

  for word in words:
    result[word] = result.get(word,0) + 1

  return result


if __name__ == "__main__":
  input_texts = "Hello world! Hello Python."
  unique_word  = get_unique_words(input_texts)
  print(unique_word)  