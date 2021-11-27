def reverse_text(text):
  for el in range(len(text)-1, -1, -1):
    yield text[el]
