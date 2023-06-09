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
  #list = ["nico", "bathroom", "8:40", "8:47"]
  while True:
    name = input("Name: ")
    name = name.lower()
    if name == "show":
      print(list)
      name = input("Name: ")
    if name == "quit":
      break
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