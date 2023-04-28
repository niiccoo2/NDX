def calc():
  import math
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'
  while True:
    number1=input(GREEN + "What is the first number?\n" + RESET)
    operation=input(YELLOW + "What operation are you using? (A, S, M, D, E, F, MAN or q to quit)\n" + RESET)
    operation=operation.upper()
    number1=int(number1)
    if operation=="Q":
      break
    elif operation=="F":
      print(math.factorial(number1))
    elif operation=="MAN":
      print("TEST")  
    number2=input(GREEN + "What is your second number?\n" + RESET)
    print("")
    number2=int(number2)
    if operation=="A":
      print(number1+number2)
    elif operation=="S":
      print(number1-number2)
    elif operation=="M":
      print(number1*number2)
    elif operation=="D":
      print(number1/number2)
    elif operation=="E":
      print(number1^number2)
    else:
      print(RED + "Wrong Operation!" + RESET)
    print("")
