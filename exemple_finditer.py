import re

pattern = re.compile(r'\d+')

liste = []
chaine = "15% de réduction sur le prix initial de  100€"
result = pattern.finditer(chaine)
if result:
    for element in result:
        liste.append(element.group())
else:
    print("Motif nom trouvé")

# element.group()
print("Les motifs trouvés sont "+" et ".join(liste))
