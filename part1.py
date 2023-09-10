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

#def chatGPT():
#  import openai
#  openai.api_key = "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"
#  RED = '\033[91m'
#  GREEN = '\033[92m'
#  YELLOW = '\033[93m'
#  BLUE = '\033[94m'
#  MAGENTA = '\033[95m'
#  CYAN = '\033[96m'
#  RESET = '\033[0m'
#  messages = [ {"role": "system", "content": 
#              "You are a intelligent assistant."} ]
#  while True:
#      message = input(YELLOW+">>>"+RESET)
#      if message == "q":
#        break
#      if message:
#          messages.append(
#              {"role": "user", "content": message},
#          )
#          chat = openai.ChatCompletion.create(
#              model="gpt-3.5-turbo", messages=messages
#          )
#      reply = chat.choices[0].message.content
#      print(GREEN+"\n"+f"{reply}"+"\n"+RESET)
#      messages.append({"role": "assistant", "content": reply})

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
# import randomimport random
#  RED = '\033[91m'
#  GREEN = '\033[92m'
#  YELLOW = '\033[93m'
#  BLUE = '\033[94m'
#  MAGENTA = '\033[95m'
#  CYAN = '\033[96m'
#  RESET = '\033[0m'
#  cc=0
#  wordlist = ["balloon", "air", "spaceship", "person", "nico", "orange", "spell", "leaf", "compass", "bear", "code", "wilson", "ndx", "edit", "talk", "beach", "well", "stop", "annoying", "please", "wall", "smell", "smart", "fat", "bad", "mean", "grenade", "electric","aardvark","pencil"]
#  RED = '\033[91m'
#  GREEN = '\033[92m'
#  YELLOW = '\033[93m'
#  BLUE = '\033[94m'
#  MAGENTA = '\033[95m'
#  CYAN = '\033[96m'
#  RESET = '\033[0m'
#  cc=0
#  wordlist = ["balloon", "air", "spaceship", "person", "nico", "orange", "spell", "leaf", "compass", "bear", "code", "wilson", "ndx", "edit", "talk", "beach", "well", "stop", "annoying", "please", "wall", "smell", "smart", "fat", "bad", "mean", "grenade", "electric","aardvark","pencil"]
#  with open('wordlist.txt') as input_file:
#    long_list = [line.strip() for line in input_file]
#  mode = input("Hard or Easy? (1/2) ")
#  mode = int(mode)
#  if mode == 1:
#    wordlist=long_list
#  wordlen=len(wordlist)
#  wordlen=wordlen-1
#  correct=wordlist[random.randint(0, wordlen)]
#  cl=len(correct)
#  while True:
#    print("_"*cl)
#    guess=input("What do you think the word is? Want the word? Press 'w'\n")
#    if guess == "w" or guess == "W":
#      check = input("You want the word? y/N\n")
#      if check == "y" or check == "Y":
#        print(correct)
#        break
#    guess=guess.lower()
#    if guess==correct:
#      print (GREEN+"You guessed the word!!"+RESET)
#      break
#    if guess != correct:
#      print(RED+"You guessed the wrong word"+RESET)
  guesses=""
  wordlist = ["pizza", "orange", "purple", "happy", "super", "word", "long", "snorkel", "wheel", "gawky", "foggy", "rodeo", "cinch", "dream", "denial", "freind", "fuel", "layer", "brush", "classroom", "ticket", "unlawful", "impound", "book", "hit", "plead", "beach", "bleach", "surgeon", "stich", "stick", "scan", "instruction", "mobile", "series", "start", "tool", "act", "fame", "those", "black", 'dying', 'frump', 'might', 'world', 'space', 'junky', 'being', 'facts', 'jumpy', 'story', 'given', "supercalifragilisticexpialidocious"]
  #really long worklist
  #with open("10000 words.txt", "r") as file:
  with open ("wordlist.txt", "r") as file:
    lines=file.readlines()
  for line in lines:
      words=line.strip().split(",")
      wordlist.extend(words)
  
  print("There are ", len(wordlist), "possible words")
  randNum=random.randint(0,(len(wordlist)-1)) #choosing random word
  secret=wordlist[randNum]
  currentguess=""
  turns = len(secret)*2
  sofar = ["_"] * len(secret)
  #giving the player information and asking questions
  while turns > 0: 
    currentguess=""
    for i in range (len(secret)):
      
      currentguess=currentguess+" "+sofar[i]
    print("You have guessed the letters:", guesses)
    print("You have ", turns," guesses left")
    print("This is the part of the word that you know, ", currentguess)
    guess=input("guess a letter\n").lower()
  #seeing if the letter was already guessed
    if (guess in guesses):
        print("That letter was already guessed, try a different letter")
    else:
        guesses=guesses+" "+guess
        turns=turns-1
        if (guess in secret):
            for i in range(len(secret)):
                if secret[i]==guess:
                    sofar[i]=guess
  #win/lose code
    if ("_" not in sofar):
      print(currentguess)
      print("YOU WIN!")
      turns=0
    if turns==0 and ("_" in sofar):
        print("YOU FAILED XD")
        #for l in range(len(secret)):
            #if sofar[l]=="_":
            #    sofar[l]="?"
            #    if ("_" not in sofar):
        print("The word is: ", secret)
  
#-------------------------MAD LIBS------------------------------#
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

#-------------------------------------- Word Guessing --------------------------------------#

def weather():
  import asyncio
  import requests
  import json
  import tkinter as tk
  from PIL import ImageTk, Image
  window_closed = False
  #global current_unit
  current_unit = "F"
  def get_weather(current_unit):
      nonlocal window_closed  # Use nonlocal to modify the outer variable
      if not window_closed:
        location = ''
        location = location_entry.get()
        api_key = "e400d74e423bf565abbc9a72c38b5e84"  # replace with your actual API key
        if location == "":
          location='Seattle'
        # construct the API URL
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

        try:
            # send the HTTP request
            response = requests.get(url)
            response.raise_for_status()  # raise an exception if the HTTP request fails

            # parse the JSON response data into a Python dictionary
            data = json.loads(response.text)

            # extract the relevant weather information from the dictionary
            temperature_k = data["main"]["temp"]
            temperature_min_k = data["main"]["temp_min"]
            temperature_max_k = data["main"]["temp_max"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            if current_unit == "F":
                temperature_f = (temperature_k * 9/5) - 459.67
                temperature_min_f = (temperature_min_k * 9/5) - 459.67
                temperature_max_f = (temperature_max_k * 9/5) - 459.67

                temperature_label.config(text=f"Temperature: {temperature_f:.1f}°F")
                high_label.config(text=f"High: {temperature_max_f:.1f}°F")
                low_label.config(text=f"Low: {temperature_min_f:.1f}°F")
            else:
                temperature_c = temperature_k - 273.15
                temperature_min_c = temperature_min_k - 273.15
                temperature_max_c = temperature_max_k - 273.15

                temperature_label.config(text=f"Temperature: {temperature_c:.1f}°C")
                high_label.config(text=f"High: {temperature_max_c:.1f}°C")
                low_label.config(text=f"Low: {temperature_min_c:.1f}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            description_label.config(text=f"Description: {description.capitalize()}")
            area_label.config(text="Weather for: "+location)

        except requests.exceptions.HTTPError as e:
            # handle HTTP errors
            temperature_label.config(text="Temperature: N/A")
            high_label.config(text="High: N/A")
            low_label.config(text="Low: N/A")
            humidity_label.config(text="Humidity: N/A")
            description_label.config(text=f"Error: {e}")
            area_label.config(text="Weather for: N/A")

        except (KeyError, json.JSONDecodeError) as e:
            # handle JSON parsing errors
            temperature_label.config(text="Temperature: N/A")
            high_label.config(text="High: N/A")
            low_label.config(text="Low: N/A")
            humidity_label.config(text="Humidity: N/A")
            description_label.config(text=f"Error: Invalid location or API key")
            area_label.config(text="Weather for: N/A")

  def change_units():
      global current_unit
      if current_unit == "F":
          current_unit = "C"
      else:
          current_unit = "F"
      get_weather(current_unit)

  # print the weather information
  #print(f"The temperature in {location} is{temperature_f: .1f} degrees Fahrenheit.")
  #print(f"The high in {location} is{temperature_max_f: .1f} degrees Fahrenheit.")
  #print(f"The low in {location} is{temperature_min_f: .1f} degrees Fahrenheit.")
  #print(f"The humidity in {location} is {humidity}%.")
  #print(f"The weather in {location} is described as {description}.")

  def on_closing():
    nonlocal window_closed  # Use nonlocal to modify the outer variable
    window_closed = True
    root.destroy()

  root = tk.Tk()
  root.title("Nico's Weather App")

  img = Image.open("./download.ico")
  icon = ImageTk.PhotoImage(img)
  root.iconphoto(True, icon)

  location_label = tk.Label(root, text="Enter location:")
  location_entry = tk.Entry(root)
  get_weather_button = tk.Button(root, text="Get Weather", command=lambda: get_weather(current_unit))
  change_unit = tk.Button(root, text="Change Units", command=change_units)
  temperature_label = tk.Label(root, text="Temperature: ")
  high_label = tk.Label(root, text="High: ")
  low_label = tk.Label(root, text="Low: ")
  humidity_label = tk.Label(root, text="Humidity: ")
  description_label = tk.Label(root, text="Description: ")
  area_label = tk.Label(root, text="Weather for: ",)

  location_label.grid(row=0, column=0, padx=10, pady=10)
  location_entry.grid(row=0, column=1, padx=10, pady=10)
  get_weather_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
  change_unit.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
  temperature_label.grid(row=2, column=0, padx=10, pady=10)
  high_label.grid(row=3, column=0, padx=10, pady=10)
  low_label.grid(row=4, column=0, padx=10, pady=10)
  humidity_label.grid(row=5, column=0, padx=10, pady=10)
  description_label.grid(row=6, column=0, padx=10, pady=10)
  area_label.grid(row=7, column=0, padx=10, pady=10)

  root.protocol("WM_DELETE_WINDOW", on_closing)
  
  root.mainloop()

  #if __name__ == '__main__':
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    #if os.name == 'nt':
      #asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  if not window_closed:  
    asyncio.run(get_weather(current_unit))