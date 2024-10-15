import re

pattern = re.compile(r'\d+(?=%)')

chaine = "Le prix est 100€ avec 15% de réduction"
result = pattern.search(chaine)
if result:
    print(result.group())
else:
    print("Motif nom trouvé")

