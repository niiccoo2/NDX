def display_help():
  from rich.console import Console
  from rich.markdown import Markdown
  import sys

  console = Console()


  with open("README.md", "r+") as help_file:
    console.print(Markdown(help_file.read()))
  r=input("\nPress enter to continue:")