def snake():
  #    ____              _        
  #   / ___| _ __   __ _| | _____ 
  #   \___ \| '_ \ / _` | |/ / _ \
  #    ___) | | | | (_| |   <  __/
  #   |____/|_| |_|\__,_|_|\_\___|
  #                               
  # Imports
  #import os # Not used
  import time
  import turtle
  import random
  # Setting vars
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'
  #turtle.setup(550, 550)
  t=turtle.Turtle()
  turtle.tracer(0, 0)
  home = [0,0]
  t.speed(0)
  t.screen.title("Snake (NDX)")
  t.shape("blank")
  clock=0
  move = 'a'
  global bre
  bre=0
  global location
  location = 14
  apple = 4
  # Changed grid to gridcs; Saving grid as color strings not numbers getting changed to strings
  #grid = [0] * 30
  global gridcs
  gridcs = ['yellow'] * 30  # Initialize the color list with yellow for all squares
  gridpos = [[1,-1], [42,-1], [83,-1], [124,-1], [165,-1], [206,-1], [1,-42], [42,-42], [83,-42], [124,-42], [165,-42], [206,-42], [1,-83], [42,-83], [83,-83], [124,-83], [165,-83], [206,-83], [1,-124], [42,-124], [83,-124], [124,-124], [165,-124], [206,-124], [1,-165], [42,-165], [83,-165], [124,-165], [165,-165], [206,-165]]
  # Asking about replit
  rep=input("Are you on replit? (Y/n)\n")
  if rep == "n":
    rep = 0
  else:
    rep = 1
  # Functions
  def goto(one, two):
    t.penup()
    t.goto(one, two)
    t.pendown()
  def drawgrid(grid):
    #gridcs = ['yellow'] * 30  # Initialize the color list with yellow for all squares
    global gridcs
    for l in range(30):
        c = gridcs[l]
        c = str(c)
        t.color(c)
        x, y = gridpos[l][0], gridpos[l][1]
        goto(x, y)
        t.begin_fill()
        for i in range(4):
          t.fd(40)
          t.rt(90)
        t.end_fill()
    turtle.update()
  def left():
    global location
    save=location
    location = location-1
    if location <= -1:
       location=save
  def right():
    global location
    save=location
    location = location+1
    if location >= 30:
       location=save
  def up():
    global location
    save=location
    location = location-6
    if location <= -1:
       location=save
  def down():
    global location
    save=location
    location = location+6
    if location >= 30:
       location=save
  def qu():
     global bre
     bre=1
  # Telling replit users to open the "Output"
  if rep == 1:
    ran = input("Open the 'Output' window. (Press 'enter' to continue.)")
  #time.sleep(5)
  # Making Grid outline
  goto(0,0)
  for i in range(2):
    t.fd(247)
    t.rt(90)
    t.fd(206)
    t.rt(90)
    #location=location-1
  while True:
    gridcs = ['light gray']*30
    t.screen.onkey(left, "Left")
    t.screen.onkey(right, "Right")
    t.screen.onkey(up, "Up")
    t.screen.onkey(down, "Down")
    t.screen.onkey(qu, "q")
    t.screen.listen()
    gridcs[location]='green'
    if apple == location:
      while True:
        apple = random.randint(0,29)
        if apple != location:
          break
    gridcs[apple]='red'
    if bre==1:
       break
    drawgrid(gridcs)
  # Telling repit users to close the "Output"
  if rep == 1:
    ran = input("Press enter to close the output!")
    print("Closing the output window...")
    turtle.bye()