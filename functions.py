from rich.console import Console
import questionary

from Game import Game

console = Console()

def find_game(query, data):
    counter = 0
    for game in data.keys():
        if query.lower().strip() in game.lower():
            console.print(f"\n🎮 [bold magenta]{game}[/]")
            console.print(f"  [cyan]Developer:[/]    {data[game].developer}")
            console.print(f"  [cyan]Release Year:[/] {data[game].release_year}")
            console.print(f"  [cyan]Metacritic:[/]   {data[game].metacritic}")
            counter += 1
    if counter == 0:
        console.print("No game found with that name. Please try again.", style="red")
    else:
        console.print(f'\n✅ Found [bold green]{counter}[/] game(s)')

def min_metacritic(minimum,data):
    counter = 0
    for game in data.keys():

        score = None
        try: 
            score = int(data[game].metacritic)
        except:
            continue
            
        if score >= minimum:
            console.print(f"\n🎮 [bold magenta]{game}[/]")
            console.print(f"  [cyan]Metacritic:[/]   {score}")
            counter += 1
    if counter == 0:
        console.print("No game with higher or equal metacritic score. Please try with a different filter.", style="red")
    else:
        console.print(f'\n✅ Found [bold green]{counter}[/] game(s)')

def max_price(maximum,data):
    counter = 0
    for game in data.keys():

        # if a price does not exist (None), then skip
        price = None
        try:
            price = float(data[game].price)
        except:
            continue
    
        if price<=maximum:
            console.print(f"\n🎮 [bold magenta]{game}[/]")
            console.print(f"  [cyan]Price:[/]        ${price}")
            counter += 1
    if counter == 0:
        console.print("No game with lower or equal price. Please try with a different filter.", style="red")
    else:
        console.print(f'\n✅ Found [bold green]{counter}[/] game(s)')
       
def recommend_game(game_name, data):
    dic = {}

    # check if the tags is None or an empty list
    if data[game_name].tags is None or data[game_name].tags == []:
        console.print('This game has no tags.', style='red')
        return

    for game in data:

        # skip the games which do not have tags
        if data[game].tags is None or data[game].tags == []:
            continue
        
        intersect = set([tag.lower() for tag in data[game_name].tags]) & set([tag.lower() for tag in data[game].tags])
        union = set([tag.lower() for tag in data[game_name].tags]) | set([tag.lower() for tag in data[game].tags])
        jaccard = len(intersect) / len(union)
        dic[game] = jaccard
    lst = sorted([(v, k) for (k, v) in dic.items()], reverse=True)

    console.print("🎮 Top 3 Recommended Games for you:", style="white")
    console.print(f"  [cyan]1.[/] [bold magenta]{lst[1][1]}[/]")
    console.print(f"  [cyan]2.[/] [bold magenta]{lst[2][1]}[/]")
    console.print(f"  [cyan]3.[/] [bold magenta]{lst[3][1]}[/]")

def add_game():
    console.print("\n🎮 [bold white]Add a New Game[/]")

    name = questionary.text("Game name:").ask()
    developer = questionary.text("Developer (or None if it does not exist):").ask()
    release_year = questionary.text("Release year (or None if it does not exist):").ask()

    # here we are validating each value to ensure its a number, otherwise default to None
    try:
        if release_year and release_year != 'None':
            release_year = int(release_year)
        else:
            release_year = None
    except ValueError:
        console.print('Release year must be a number. Defaulting to None.', style='red')
        release_year = None
        
    metacritic = questionary.text("Metacritic score (or None if it does not exist):").ask()
    try:
        if metacritic and metacritic != 'None':
            metacritic = float(metacritic)
        else:
            metacritic = None
    except ValueError:
        console.print('Metacritic score must be a number. Defaulting to None.', style='red')
        metacritic = None

    price = questionary.text("Price (or None if it does not exist):").ask()
    try:
        if price and price != 'None':
            price = float(price)
        else:
            price = None
    except ValueError:
        console.print('Price must be a number. Defaulting to None.', style='red')
        price = None

    tags = questionary.text("Tags separated by commas (or None if it does not exist):").ask()

    # if there are tags, store them in a list (split by commas)
    if tags and tags != 'None':
        tags = [tag.strip() for tag in tags.strip().split(",")]
    else:
        tags = None
    
    new_game = Game(name, tags, release_year, metacritic, price, developer)
    try:
        new_game.save('games_database.json')
        console.print('Game saved successfuly', style='green')
    except:
        console.print('An error occurred', style='red')

