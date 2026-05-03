import json
class Game:
  def __init__(self, name, tags, release_year, metacritic, price, developer):
    self.tags = tags
    self.release_year = release_year
    self.metacritic = metacritic
    self.price = price
    self.developer = developer
    self.name = name

  def save(self, filename):
    # Load existing data
    try:
        with open(filename, 'r') as f:
            database = json.load(f)
    except:
        database = {}

    # Save using the game name as the key
    database[self.name] = {
      "name": self.name,
        "tags": self.tags,
        "release_year": self.release_year,
      "metacritic": self.metacritic,
        "price": self.price,
        "developer": self.developer
    }

    # Write back to file
    with open(filename, 'w') as f:
        json.dump(database, f, indent=4)

    print("Game saved to database!")