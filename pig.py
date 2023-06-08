def pig():
  length = 0
  print("Welcome to the Pig Latin Translator")
  while True:
    org = input("What would you like to Translate?\n")
    org = org.lower()
    split = [*org]
    first = split[0]
    split.pop(0)
    length = len(split)
    len = len-1
    split[len] = first
    print(split)