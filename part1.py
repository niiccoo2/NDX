#-------------------------------------- Magic 8 Ball --------------------------------------#

def ball8():
  import random
  responselist = [
    "Yes", "No", "It is decidedly so", "Dont count on it",
    "You may rely on it", "Ask again later", "Can't respond now",
    "Reply hazy, try again", "Output not so good", "Without a doubt",
    "It is certain", "Yes, definitely", "As I see it, yes", "Most likely",
    "Outlook good", "Signs point to yes", "Better not tell you know",
    "Cannot predict now", "Concentrate and ask again", "My reply is no",
    "My sources say no", "Very doubtful"]
  responcelen = len(responselist)
  responcelen = responcelen - 1
  
  input("What is your question? ")
  print(responselist[random.randint(0, responcelen)])

#-------------------------------------- Calc --------------------------------------#

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
    else:
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
        print(number1**number2)
      else:
        print(RED + "Wrong Operation!" + RESET)
    print("")

#-------------------------------------- ChatGPT --------------------------------------#

def chatGPT():
  import openai
  openai.api_key = "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"
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'
  messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
  while True:
      message = input(YELLOW+">>>"+RESET)
      if message == "q":
        break
      if message:
          messages.append(
              {"role": "user", "content": message},
          )
          chat = openai.ChatCompletion.create(
              model="gpt-3.5-turbo", messages=messages
          )
      reply = chat.choices[0].message.content
      print(GREEN+"\n"+f"{reply}"+"\n"+RESET)
      messages.append({"role": "assistant", "content": reply})

#-------------------------------------- Density --------------------------------------#

def den():
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'
  mass = input(GREEN+"Mass: "+RESET)
  vol = input(YELLOW+"Volume: "+RESET)
  mass = int(mass)
  vol = int(vol)
  den = mass/vol
  print(MAGENTA+"The density is: "+CYAN+str(den)+MAGENTA+" g/mL"+RESET)
  g = input(MAGENTA+"Press 'enter' to continue."+RESET)

#-------------------------------------- Text Editor --------------------------------------#

def tedit():
    import os
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    CLEAR = '\l'
    
    while True:
        file_name = input("Enter a file name to create or edit, 'l' to list text files, or 'q' to quit: ")
        if file_name == 'q':
            break
        elif file_name == 'l':
            print(YELLOW + "Text files in current directory:" + RESET)
            for filename in os.listdir():
                if filename.endswith(".txt"):
                    print(GREEN + filename + RESET)
            print("-" * 20)
            continue

        if not file_name.endswith(".txt"):
            file_name += ".txt"

        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                file_contents = file.read()
        else:
            file_contents = ""

        while True:
            print(BLUE + "File Contents:" + RESET)
            print(file_contents)
            print("-" * 20)
            print(CYAN + "1. Edit file" + RESET)
            print(CYAN + "2. Save and exit" + RESET)
            choice = input("Enter choice: ")

            if choice == "1":
                file_contents = input("Enter file contents: ")
            elif choice == "2":
                with open(file_name, 'w') as file:
                    file.write(file_contents)
                break
            else:
                print(RED + "Invalid choice. Try again." + RESET)

    print("Exiting text editor...")

#-------------------------------------- Gambl --------------------------------------#

def gambl():
  money=50
  money=int(money)
  import random
  print("Your mother gave you 50 dollars to bet on the line races. Your goal is to  come baack with $50,000,000.")
  while money>0:
    money=int(money)
    ilovenumbers=50000000
    ilovenumbers=int(ilovenumbers)
    while money < max:
      numberracers=input("do you want 3, 5, or 10 line racers in the race you are betting on? The    more racers there are the more money you make. ")
      money=50
      max3=0
      money=int(money)
      if numberracers == "3":
        bet3=input("whitch line do you want to bet on. 1, 2 or 3 from the top? ")
        bet=input("How much do you want to bet? ")
        top3=random.randint(10, 20)
        middle3=random.randint(10, 20)
        bottom3=random.randint(10, 20)
        print("-"*top3)
        print("-"*middle3)
        print("-"*bottom3)
        if top3 > middle3:
          max2nd3="top3"
        else:
          max2nd3="middle3"
          if bottom3 > max2nd3 :
            max3="bottom3"
        if bet3 == max(top3, bottom3, middle3):
          money=(bet*numberracers)+money
          money=str(money)
          print("You won "+(bet*numberracers)+money+" money!")
          print("You now have $"+money)
          money=int(money)
        else:
          print("You lost $"+bet)
          bet=int(bet)
          money=money-bet
          money=str(money)
          print("You have $"+money)
    print("You got $50000000!!! Your mother is very proud!")
  print("You went broke :( your mother is disappointed...")

#-------------------------------------- Help --------------------------------------#

def display_help():
  from rich.console import Console
  from rich.markdown import Markdown
  import sys

  console = Console()


  with open("README.md", "r+") as help_file:
    console.print(Markdown(help_file.read()))
  r=input("\nPress enter to continue:")

#-------------------------------------- Pig Latin --------------------------------------#

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

#-------------------------------------- Reaction Tester --------------------------------------#

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

#-------------------------------------- Random Number Guessing Game --------------------------------------#

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

#-------------------------------------- Rock Paper Scissors --------------------------------------#

def rps():
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'
  import random
  while True:
    RPS=input(MAGENTA+"Rock, Paper, or Scissors. Press q to quit\n"+RESET)
    RPS=RPS.lower()
    if RPS=="q":
      break
    if RPS != "rock":
      if RPS != "paper":
        if RPS != "scissors":
          if RPS != "q":
            print(RED+"Print Rock, Paper, or Scissors please. No capitals."+RESET)
            break
    ComputerRPS=random.randint(1.,3)
    if ComputerRPS==1:
      ComputerRPS=str(ComputerRPS)
      ComputerRPS="rock"
    elif ComputerRPS==2:
      ComputerRPS=str(ComputerRPS)
      ComputerRPS="paper"
    elif ComputerRPS==3:
      ComputerRPS=str(ComputerRPS)
      ComputerRPS="scissors"
    print(YELLOW+"The computer said "+ComputerRPS+RESET)
    if ComputerRPS==RPS:
      print(BLUE+"It's a tie!"+RESET)
    elif ComputerRPS=="rock":
      if RPS=="paper":
        print(GREEN+"You win!"+RESET)
      elif RPS=="scissors":
        print(RED+"You lose..."+RESET)
    elif ComputerRPS=="paper":
      if RPS=="scissors":
        print(GREEN+"You win!"+RESET)
      elif RPS=="rock":
        print(RED+"You lose..."+RESET)
    elif ComputerRPS=="scissors":
      if RPS=="rock":
        print(GREEN+"You win!"+RESET)
      elif RPS=="paper":
        print(RED+"You lose..."+RESET)
    if RPS != "rock":
      if RPS != "paper":
        if RPS != "scissors":
          print(RED+"Print Rock, Paper, or Scissors please. No capitals"+RESET)

#-------------------------------------- Signout --------------------------------------#

def signout():
  import pickle
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'
  filename = "signout.pickle"
  with open(filename, "rb") as f:
    list = pickle.load(f)
  while True:
    name = input("Name: ")
    name = name.lower()
    if name == "show":
      print(list)
      name = input("Name: ")
    if name == "quit":
      break
    if name == 'reset':
      list = ["nico", "bathroom", "8:40", "8:47"]
      name = input("Name: ")
    location = input("Destination: ")
    location = location.lower()
    timeout = input("Time Out: ")
    timeout = timeout.lower()
    timein = input("Time In: ")
    timein = timein.lower()
    list = [list, name, location, timeout, timein]
    with open(filename, "wb") as f:
        pickle.dump(list, f)
    print(MAGENTA+"Thank you!\n\n"+RESET)

#-------------------------------------- Tic Tac Toe --------------------------------------#

def tic():
  (lambda: [[[list(iter(lambda: ((userinput() and False or check_state() == -1 and [state[y].__setitem__(x, 2) for x, y in [aimove()]]) and False or check_state() != -1), True)) and display(False) or print(["Draw!", "You won!", "Computer won!"][check_state()]) for userinput, aimove in [[lambda: [(list(iter(lambda: (display(True) or xin.__setitem__(0, input(">> ")) or True) and xin[0] in valid, True)) and False) or [state[y].__setitem__(x, 1) for x, y in [num_to_cell(int(xin[0]))]] for xin, valid in [([""], [str(cell_to_num(j, i)) for i in range(3) for j in range(3) if state[i][j] == 0])]], lambda: ([(k, j) for i in [2, 1] for j in range(3) for k in range(3) for l in range(4) if (l == 0 and state[j][k] == 0 and state[j][(k+1)%3] == i and state[j][(k+2)%3] == i) or (l == 1 and state[j][k] == 0 and state[(j+1)%3][k] == i and state[(j+2)%3][k] == i) or (l == 2 and j == k and state[j][k] == 0 and state[(j+1)%3][(k+1)%3] == i and state[(j+2)%3][(k+2)%3] == i) or (l == 3 and j + k == 2 and state[j][k] == 0 and state[(j+1)%3][(k+2)%3] == i and state[(j+2)%3][(k+1)%3] == i)] + ([(1, 1)] if True and state[1][1] == 0 else []) + [list(iter(lambda: (value[0] is not None and state[value[0][1]][value[0][0]] == 0 or value.__setitem__(0, (random(), random())) and False), True)) and False or value[0] for value, random in [([None], lambda: __import__("random").randint(0, 2))]])[0]]]] for display, check_state in [[lambda numbers: print("\033c" if ansi else "", end='') or ([print(("---+---+---\n" if i > 0 else "") + "|".join([" " + (("\033[36m" if ansi else "") + str(cell_to_num(j, i)) + ("\033[0m" if ansi else "") if numbers and x == 0 else " XO"[x]) + " " for j, x in enumerate(state[i])])) for i in range(3)] and None), lambda: ([row[0] for row in state if row == [1] * 3 or row == [2] * 3] or [col[0] for col in zip(*state) if col == (1,) * 3 or col == (2,) * 3] or ([state[0][0]] if state[0][0] == state[1][1] == state[2][2] != 0 else []) or ([state[2][0]] if state[2][0] == state[1][1] == state[0][2] != 0 else []) or [-1 if any([state[y][x] == 0 for x in range(3) for y in range(3)]) else 0])[0]]]] for state, num_to_cell, cell_to_num, ansi in [([[0 for _ in range(3)] for _ in range(3)], (lambda num: ((num - 1) % 3, 2 - (num - 1) // 3)), (lambda x, y: (2 - y) * 3 + x + 1), True)]] and None)()

#-------------------------------------- Word Guessing --------------------------------------#

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
  mode = input("Hard or Easy? (1/2) ")
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


def madlib():
  #intro
  a=input("Welcome to Mad-Libs (Press Enter To Continue)")
  a=input("First let's get your input for the story!")
  
  #Getting inputs
  number1=input("Any Number: ")
  place1=input("The name of a place: ")
  noun1=input("Noun: ")
  adjective1=input("Adjective: ")
  number2=input("Number From 0 to 99: ")
  adjective2=input("Adjective: ")
  interjection1=input("Interjection: ")
  nameofcandy1=input("Name of candy: ")
  number3=input("Number: ")
  number4=input("Number: ")
  
  a=input("\n\n\n----------TIME-FOR-THE-STORY----------\n")
  
  #printing story
  print('One day I was taking a '+number1+' Mile walk, when I walked by '+place1+' I saw a '+noun1+' by the path, But I kept walking, then I got tired of walking so I got in the '+adjective1+' Car that I found. I was driving the '+adjective1+' Car and I needed to eat so I stopped at a '+number2+'-11. The '+adjective2+' Worker Said “'+interjection1+', I never thought I would see YOU!” “That was odd,” I said under my breath. I continued until I saw tons of '+nameofcandy1+'’s I grabbed '+number3+' '+nameofcandy1+'’s and brought them to the counter, “That will be $'+number4+'” said the worker. “OK!” I said')
  ran = input("Press Enter to Continue")