import re

chaine = 'Une phrase commence par une \nmajuscule et se termine par un point.'

regex = re.compile(r'^[A-Z].*\.$',re.DOTALL)

resulat = regex.search(chaine)


if resulat:
    print(resulat.group())
else:
    print("Motif non trouvé")
