import re 

chaine = "koRri"

regex = re.compile(r'^(?=.*[A-Z]).*')

resultat = regex.search(chaine)
if resultat:
    print(resultat.group())
else:
    print("Motif non trouvé")


    