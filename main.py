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
# THIS WAS LAST UPDATED ON 4/28/23 THE UP TO DATE GITHUB IS github.com/niiccoo2/NDX


# imports
from time import sleep
from editor import *
from calc import *
import math
# NOTE: Need to fix sound
from pydub import AudioSegment
from pydub.playback import play
# Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
#Setting vars
# NOTE: Need to fix sound part
song = AudioSegment.from_wav("oxp.wav")
# Printing nice NDX logo
print(RED+" .-----------------. .----------------.  .----------------. ")
sleep(0.15)
print(RED+"| .--------------. || .--------------. || .--------------. |")
sleep(0.15)
print(RED+"| | ____  _____  | || |  ________    | || |  ____  ____  | |")
sleep(0.15)
print(RED+"| ||_   \|_   _| | || | |_   ___ `.  | || | |_  _||_  _| | |")
sleep(0.15)
print(RED+"| |  |   \ | |   | || |   | |   `. \ | || |   \ \  / /   | |")
sleep(0.15)
print(RED+"| |  | |\ \| |   | || |   | |    | | | || |    > `' <    | |")
sleep(0.15)
print(RED+"| | _| |_\   |_  | || |  _| |___.' / | || |  _/ /'`\ \_  | |")
sleep(0.15)
print(RED+"| ||_____|\____| | || | |________.'  | || | |____||____| | |")
sleep(0.15)
print(RED+"| |              | || |              | || |              | |")
sleep(0.15)
print(RED+"| '--------------' || '--------------' || '--------------' |")
sleep(0.15)
print(RED+" '----------------'  '----------------'  '----------------' ")
sleep(0.5)
# NOTE: Need to fix sound
play(song)
while True:
  print(BLUE + "\n\n1. Text Editor\n2. Calculator\n3. Random Number Game\n" + RESET)
  i = input("Where do you want to go? (Type 1 for Item 1, 2 for 2, etc)\n")
  i=int(i)
  if i==1:
    tedit()
  if i==2:
    calc()
  if i==3:
    print("how are you?")
    #do next thing here
