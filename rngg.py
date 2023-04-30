def RNGG():
  # Imports
  import pickle
  import random
  # Colors
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'
  # Seting vars and randoms
  RN=random.randint(1,1000)
  RN=int(RN)
  guess=0
  Guesses=0
  filename = "rnggh.pickle"
  # Reading file
  with open(filename, "rb") as f:
    Highscore = pickle.load(f)
  # Making things into ints
  guess=int(guess)
  Guesses=int(Guesses)
  # main while loop
  while guess != RN:
    Guesses=int(Guesses)
    Guesses=Guesses+1
    #Guesses=str(Guesses)
    guess=input(YELLOW+"Guess a number from one to one thousand! Guess the number to quit\n"+RESET)
    guess=int(guess)
    if RN == guess: 
      Highscore=int(Highscore)
      if Guesses < Highscore:
        Highscore=Guesses
      Guesses=str(Guesses)
      Highscore=str(Highscore)
      print(GREEN+"You got the number! Guesses: "+Guesses+"! Highscore: "+Highscore+"!"+RESET)
      with open(filename, "wb") as f:
        pickle.dump(Highscore, f)
    elif RN < guess: 
       print(MAGENTA+"Lower."+RESET)
    elif RN > guess:
       print (MAGENTA+"Higher."+RESET)
    if guess > 1000:
      print(RED+"But that is over the limit!"+RESET)
    elif guess < 1:
      print(RED+"But that is under the minimum!"+RESET)
