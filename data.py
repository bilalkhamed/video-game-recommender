from Game import Game
import json

def load_data(filename):
    try:
        with open(filename, 'r') as file:
          data = json.load(file)
          return {
              name: Game(
                  values['name'],
                  values['tags'],
                  values['release_year'],
                  values['metacritic'],
                  values['price'],
                  values['developer']
              )
              for name, values in data.items()
          }
    except FileNotFoundError:
        return {}