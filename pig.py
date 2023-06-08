def pig():
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'
  print(YELLOW + "Welcome to the Pig Latin Translator!\n" + RESET)
  while True:
    org = input(GREEN +
                "What would you like to Translate? (One Word, q to Quit)\n" +
                RESET)
    org = org.lower()
    if org == "q":
      break
    split = [*org + 'h']
    first = split[0]
    split.pop(0)
    split[(len(split) - 1)] = first
    print(MAGENTA + ''.join(split) + 'ay' + RESET)
