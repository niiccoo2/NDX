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