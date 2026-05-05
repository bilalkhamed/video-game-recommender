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
        if int(data[game].metacritic) >= minimum:
            console.print(f"\n🎮 [bold magenta]{game}[/]")
            console.print(f"  [cyan]Metacritic:[/]   {data[game].metacritic}")
            counter += 1
    if counter == 0:
        console.print("No game with higher or equal metacritic score. Please try again.", style="red")
    else:
        console.print(f'\n✅ Found [bold green]{counter}[/] game(s)')

def max_price(maximum,data):
    counter = 0
    for game in data.keys():
        if int(data[game].price)<=maximum:
            console.print(f"\n🎮 [bold magenta]{game}[/]")
            console.print(f"  [cyan]Price:[/]        ${data[game].price}")
            counter += 1
    if counter == 0:
        console.print("No game with lower or equal price. Please try again.", style="red")
    else:
        console.print(f'\n✅ Found [bold green]{counter}[/] game(s)')
       
def recommend_game(game_name, data):
    dic = {}
    for game in data:
        intersect = set(data[game_name].tags) & set(data[game].tags)
        union = set(data[game_name].tags) | set(data[game].tags)
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
    release_year = int(questionary.text("Release year (or None if it does not exist):").ask())
    metacritic = float(questionary.text("Metacritic score (or None if it does not exist):").ask())
    price = float(questionary.text("Price (or None if it does not exist):").ask())
    tags = questionary.text("Tags separated by commas (or None if it does not exist):").ask()

    if tags:
        tags = [tag.strip() for tag in tags.split(",")]
    else:
        tags = None
    
    new_game = Game(name, tags, release_year, metacritic, price, developer)
    new_game.save('games_database.json')
    try:
        console.print('Game saved successfuly', style='green')
    except:
        console.print('An error occurred', style='red')

