#/usr/bin/python3
#   .-----------------. .----------------.  .----------------. 
#  | .--------------. || .--------------. || .--------------. |
#  | | ____  _____  | || |  ________    | || |  ____  ____  | |
#  | ||_   \|_   _| | || | |_   ___ `.  | || | |_  _||_  _| | |
#  | |  |   \ | |   | || |   | |   `. \ | || |   \ \  / /   | |
#  | |  | |\ \| |   | || |   | |    | | | || |    > `' <    | |
#  | | _| |_\   |_  | || |  _| |___.' / | || |  _/ /'`\ \_  | |
#  | ||_____|\____| | || | |________.'  | || | |____||____| | |
#  | |              | || |              | || |              | |
#  | '--------------' || '--------------' || '--------------' |
#   '----------------'  '----------------'  '----------------' 
# THIS WAS LAST UPDATED ON 11/17/2023 THE UP TO DATE GITHUB IS github.com/niiccoo2/NDX

# imports
from time import sleep
import math
import pickle
from part1 import *
from snake import *
#from playsound import playsound
# NOTE: Need to fix sound
#from pydub import Audiimport play
# Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
#Setting vars
passq="o"
passn=0
wrongpass=30
wrongpass=str(wrongpass)
passn=int(passn)
ndxfast=0
# NOTE: Need to fix sound part
#song = AudioSegment.from_wav("oxp.wav")
ndxfast=0
#ndxfast = global ndxfast
#ndxfast=1 # Uncoment this to change NDX Logo to fast mode.

# Settings

def settings():
  print('Settings:\n1. Fast Logo\nMore settings will be added!')
  pick=input('Pick a setting: ')

  if pick==1:
    print("Current value: "+ndxfast)
    ndxfast=input("Enter new value: ")



if ndxfast==1:
  #Printing fast NDX logo
  print(RED+r" .-----------------. .----------------.  .----------------. ")
  print(RED+r"| .--------------. || .--------------. || .--------------. |")
  print(RED+r"| | ____  _____  | || |  ________    | || |  ____  ____  | |")
  print(RED+r"| ||_   \|_   _| | || | |_   ___ `.  | || | |_  _||_  _| | |")
  print(RED+r"| |  |   \ | |   | || |   | |   `. \ | || |   \ \  / /   | |")
  print(RED+r"| |  | |\ \| |   | || |   | |    | | | || |    > `' <    | |")
  print(RED+r"| | _| |_\   |_  | || |  _| |___.' / | || |  _/ /'`\ \_  | |")
  print(RED+r"| ||_____|\____| | || | |________.'  | || | |____||____| | |")
  print(RED+r"| |              | || |              | || |              | |")
  print(RED+r" '----------------'  '----------------'  '----------------' ")
else:
  # Printing nice NDX logo
  print(RED+r" .-----------------. .----------------.  .----------------. ")
  sleep(0.15)
  print(RED+r"| .--------------. || .--------------. || .--------------. |")
  sleep(0.15)
  print(RED+r"| | ____  _____  | || |  ________    | || |  ____  ____  | |")
  sleep(0.15)
  print(RED+r"| ||_   \|_   _| | || | |_   ___ `.  | || | |_  _||_  _| | |")
  sleep(0.15)
  print(RED+r"| |  |   \ | |   | || |   | |   `. \ | || |   \ \  / /   | |")
  sleep(0.15)
  print(RED+r"| |  | |\ \| |   | || |   | |    | | | || |    > `' <    | |")
  sleep(0.15)
  print(RED+r"| | _| |_\   |_  | || |  _| |___.' / | || |  _/ /'`\ \_  | |")
  sleep(0.15)
  print(RED+r"| ||_____|\____| | || | |________.'  | || | |____||____| | |")
  sleep(0.15)
  print(RED+r"| |              | || |              | || |              | |")
  sleep(0.15)
  print(RED+r"| '--------------' || '--------------' || '--------------' |")
  sleep(0.15)
  print(RED+r" '----------------'  '----------------'  '----------------' ")
  sleep(0.5)
# NOTE: Need to fix sound
#playsound('./windows-xp-startup-sound.mp3')
#readline
while True:
  print(BLUE + "\n\nQ: Quit\nS. Settings\n0. Help\n1. Text Editor\n2. Calculator\n3. Random Number Game\n4. Rock Paper Scissors\n5. Tic Tac Toe\n6. Word Guess\n7. Magic 8 Ball\n8. ChatGPT\n9. Reaction Tester\n10. Density Calc\n11. Snake\n12. Gambling >:\n13. Pig Latin Translator\n14. Sign Out\n15. Mad-Libs\n16. Weather" + RESET)
  i = input("Where do you want to go? (Type 1 for Item 1, 2 for 2, etc)\n")
  if i.lower()=='q':
    quit()
  if i.lower()=='s':
    settings()
  i=int(i)
  if i==0:
    display_help()
  if i==1:
    tedit()
  if i==2:
    calc()
  if i==3:
    RNGG()
  if i==4:
    rps()
  if i==5:
    tic()
  if i==6:
    word()
  if i==7:
    ball8()
  if i==8:
    passs = "dumb123"
    passg = input("What is the password?\n")
    if passg==passs:
      #chatGPT()
      print("Sorry this is not working right now...")
    print("Wrong")
    passn=passn+1
    if passn==3:
      print("Please wait and try again later.")
      wrongpass=int(wrongpass)
      sleep(100+(wrongpass*10))
      wrongpass=wrongpass+1
  if i==9:
    reac()
  if i==10:
    den()
  if i==11:
    snake()
  if i==12:
    print("Not working right now.")
  if i==13:
    pig()
  if i==14:
    signout()
  if i==15:
    madlib()
  if i==16:
    weather()
  