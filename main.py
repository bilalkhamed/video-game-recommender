from rich.console import Console
from rich.text import Text
import questionary

from functions import recommend_game
from data import load_data

console = Console()

while True:

  database = load_data('games_database.json')

  white_part = "Welcome to the ultimate "
  gradient_part = "video game recommender"
  colors = ["cyan", "blue", "magenta"]


  text = Text()
  text.append(white_part, style="white")

  for i, char in enumerate(gradient_part):
      text.append(char, style=f"bold {colors[i % len(colors)]}")
  
  console.print(text)
    
  choice = questionary.select(
    "What do you want to do?",
    choices=[
        "Find similar games",
        "Search for a game",
        "Exit"
    ]
    ).ask()
  
  if choice == 'Find similar games':
     name = questionary.text('Enter the game\'s name: ').ask()
     if name not in database:
        console.print('[red]Game not found in our database.')
     else: 
        recommend_game(name, database)
     

  break
