import re

chaine = r'\Le back slash'

regex = re.compile('\\\\')
# regex = re.compile(r'\\') # plus simple avec les raw string 

resulat = regex.search(chaine)



if resulat:
    print(resulat.group())
else:
    print("Motif non trouvé")
