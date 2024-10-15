import re

texte = "https://www.example.com/page"
pattern = r"https://www\.example\.com/page"

match = re.findall(pattern, texte)
print(match)  # Affiche ['https://www.example.com/page']
