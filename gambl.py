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