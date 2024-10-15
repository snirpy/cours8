import re

chaine = '^ :au début et fini par: $'

regex = re.compile(r'^\^.*\$$')

resulat = regex.search(chaine)


if resulat:
    print(resulat.group())
else:
    print("Motif non trouvé")
