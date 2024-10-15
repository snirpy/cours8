import re

texte = "Il y a 100€ et 200$ ici."

# Regex avec lookahead négatif
pattern = r'\b\d+\b(?!€)'

match = re.findall(pattern, texte)
print(match)  # Affiche ['200']
