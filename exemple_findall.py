import re

pattern = re.compile(r'\d+')


chaine = "15% de réduction sur le prix initial de  100€"
result = pattern.findall(chaine)
if result:
    print(" et ".join(result))
else:
    print("Motif nom trouvé")

