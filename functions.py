from rich.console import Console


console = Console()

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