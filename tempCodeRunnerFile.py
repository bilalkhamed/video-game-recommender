  gradient_part = "video game recommender"
  colors = ["cyan", "blue", "magenta"]

  text = Text()
  text.append(white_part, style="white")

  for i, char in enumerate(gradient_part):
      text.append(char, style=f"bold {colors[i % len(colors)]}")