def snake():
  #    ____              _        
  #   / ___| _ __   __ _| | _____ 
  #   \___ \| '_ \ / _` | |/ / _ \
  #    ___) | | | | (_| |   <  __/
  #   |____/|_| |_|\__,_|_|\_\___|
  #                               
  # Imports
  import os
  import time
  import turtle
  # Setting vars
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'
  turtle.setup(550, 550)
  t=turtle.Turtle()
  home = [0,0]
  t.speed(0)
  t.screen.title("Snake")
  t.shape("blank")
  clock=0
  grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  gridpos = [[1,-1], [42,-1], [83,-1], [124,-1], [165,-1], [206,-1], [1,-42], [42,-42], [83,-42], [124,-42], [165,-42], [206,-42], [1,-83], [42,-83], [83,-83], [124,-83], [165,-83], [206,-83], [1,-124], [42,-124], [83,-124], [124,-124], [165,-124], [206,-124], [1,-165], [42,-165], [83,-165], [124,-165], [165,-165], [206,-165]]
  # Asking about replit
  rep=input(+YELLOW+"Are you on replit? (Y/n)\n"+RESET)
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
    gridcs = ['yellow'] * 30  # Initialize the color list with yellow for all squares
    for k in range(30):
        if grid[k] == 0:
            gridcs[k] = 'light gray'
            #print("white")
        elif grid[k] == 1:
            gridcs[k] = 'dark green'
            #print("green")
        elif grid[k] == 2:
            gridcs[k] = 'red'
            #print("red")
    for l in range(30):
        c = gridcs[l]
        c = str(c)
        t.color(c)
        x, y = gridpos[l][0], gridpos[l][1]
        goto(x, y)
        t.begin_fill()
        for i in range(4):
          t.fd(40)
          #print("dawing squares")
          t.rt(90)
        t.end_fill()
  # Telling replit users to open the "Output"
  if rep == 1:
    ran = input(YELLOW+"Open the 'Output' window. (Press 'enter' to continue.)"+RESET)
  time.sleep(5)
  # Making Grid outline
  goto(0,0)
  for i in range(2):
    t.fd(247)
    t.rt(90)
    t.fd(206)
    t.rt(90)
  while True:
    # Grid list format (5x5) First row of 5 then next and next etc
    drawgrid(grid)
    time.sleep(2)
    if clock==0:
      clock=1
    else:
      clock=0
    if clock==0:
      grid = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    if clock==1:
      grid = [2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2]
  # Telling repit users to close the "Output"
  if rep == 1:
    ran = input(RED+"Press enter to close the output!")
    print("Closing the output window..."+RESET)
    turtle.bye()