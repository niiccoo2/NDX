def word():
  import random
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'
  cc=0
  wordlist = ["balloon", "air", "spaceship", "person", "nico", "orange", "spell", "leaf", "compass", "bear", "code", "wilson", "ndx", "edit", "talk", "beach", "well", "stop", "annoying", "please", "wall", "smell", "smart", "fat", "bad", "mean", "grenade", "electric","aardvark","pencil"]
  with open('wordlist.txt') as input_file:
    long_list = [line.strip() for line in input_file]
  mode = input("Hard or Easy? (1/2)")
  mode = int(mode)
  if mode == 1:
    wordlist=long_list
  wordlen=len(wordlist)
  wordlen=wordlen-1
  correct=wordlist[random.randint(0, wordlen)]
  cl=len(correct)
  while True:
    print("_"*cl)
    guess=input("What do you think the word is? Want the word? Press 'w'\n")
    if guess == "w" or guess == "W":
      check = input("You want the word? y/N\n")
      if check == "y" or check == "Y":
        print(correct)
        break
    guess=guess.lower()
    if guess==correct:
      print (GREEN+"You guessed the word!!"+RESET)
      break
    if guess != correct:
      print(RED+"You guessed the wrong word"+RESET)