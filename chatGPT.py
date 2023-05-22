def chatGPT():
  import openai
  openai.api_key = "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"
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  RESET = '\033[0m'
  messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
  while True:
      message = input(YELLOW+">>>"+RESET)
      if message == "q":
        break
      if message:
          messages.append(
              {"role": "user", "content": message},
          )
          chat = openai.ChatCompletion.create(
              model="gpt-3.5-turbo", messages=messages
          )
      reply = chat.choices[0].message.content
      print(GREEN+"\n"+f"{reply}"+"\n"+RESET)
      messages.append({"role": "assistant", "content": reply})