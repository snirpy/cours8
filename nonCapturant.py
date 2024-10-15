import re

texte = "apple, banana, orange"
pattern = r"(?:apple|banana), (orange)"

match = re.search(pattern, texte)
print(match.group(1))  # Affiche 'orange'
