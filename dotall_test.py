import re

texte = "Hello\nWorld"
pattern = r"Hello.*World"

match = re.search(pattern, texte, re.DOTALL)
print(match.group())  # Affiche "Hello\nWorld"

match = re.search(pattern, texte)
print(match)  # Affiche "None" car '.' ne correspond pas à '\n'