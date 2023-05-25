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