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
