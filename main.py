from rich.console import Console
from rich.text import Text
import questionary

from functions import recommend_game, find_game, min_metacritic, max_price, add_game
from data import load_data

console = Console()

white_part = "Welcome to the ultimate "
gradient_part = "video game recommender"
colors = ["cyan", "blue", "magenta"]


text = Text()
text.append(white_part, style="white")

for i, char in enumerate(gradient_part):
      text.append(char, style=f"bold {colors[i % len(colors)]}")
  
console.print(text)

database = load_data('games_database.json')


while True:
  choice = questionary.select(
    "What do you want to do?",
    choices=[
        "Search for a game",
        "Get a game recommendation",
        "Search for games with filter",
        "Add a new game",
        "Exit"
    ]
    ).ask()
  
  if choice == 'Search for a game':
     query = questionary.text('Enter the game\'s name: ').ask()
     find_game(query, database)

  elif choice == 'Get a game recommendation':
     name = questionary.text('Enter the game\'s name: ').ask()
     if name not in database:
        console.print('[red]Game not found in our database.')
     else: 
        recommend_game(name, database)

  elif choice == 'Search for games with filter':
     filter = questionary.select(
        'Choose a filter:',
        choices=[
           'Minimum metacritic score',
           'Maximum price point'
        ]
     ).ask()

     if filter == 'Minimum metacritic score':
        score = int(questionary.text('Enter the minimum score:').ask())
        min_metacritic(score, database)
     else:
        price = int(questionary.text('Enter the maximum price:').ask())
        max_price(price, database)
    
  elif choice == 'Add a new game':
     add_game()
     database = load_data('games_database.json')
     
  elif choice == 'Exit': 
     console.print('Exiting the video game reccomender. See you again!')
     break   
