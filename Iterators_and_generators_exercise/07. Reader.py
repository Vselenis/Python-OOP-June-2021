def read_next(*args):
  for x in args:
    for element in x:
      yield element
