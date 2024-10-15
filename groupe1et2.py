
import re
texte = "20% de réduction sur un produit à 100€, et 30% sur un autre à 250€"
# Regex pour capturer les pourcentages suivis d'un prix
pattern = r'(\d+)%.*?(\d+)€'

matches = re.finditer(pattern, texte)

for match in matches:
    pourcentage = match.group(1)  # Correspond au nombre avant %
    prix = match.group(2)         # Correspond au nombre après €
    print(f"Pourcentage : {pourcentage}%, Prix : {prix}€")

