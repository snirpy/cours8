import re

chaine = "Je suis fort en Python"

regex = r'FORT'

resultat = re.search(regex, chaine,re.I)
print(resultat.group())

