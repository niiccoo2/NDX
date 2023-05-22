def reac():
  from time import sleep
  from time import time
  import random
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'
  wait=random.randint(1,15)
  sleep(wait)
  timer=0
  shamwow="10"
  letterlist=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
  letterlen = len(letterlist)
  letterlen = letterlen - 1
  letter=letterlist[random.randint(0, letterlen)]
  print("Type the letter: "+letter)
  start_time=time( )
  shamwow=input("")
  end_time=time( )
  seconds=end_time-start_time
  if shamwow==letter:
    final=round(seconds, 2)
    final=str(final)
    print(GREEN+"You got the letter in "+MAGENTA+""+final+""+GREEN+" seconds!"+RESET)
  if shamwow != letter:
    print(RED+"NO!"+RESET)