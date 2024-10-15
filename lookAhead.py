import re

regex = re.compile(r'(?=.*[A-Z]).*')

chaine = r"une majuscule dans la phrase "

resultat = regex.search(chaine)
if resultat:
    print(resultat.group())
else:
    print("Motif non trouvé")
