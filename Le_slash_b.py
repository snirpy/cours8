
import re 

chaine = "le langagae python3 est excellent!"

# regex = re.compile(r'python') # trouve le motif python

regex = re.compile(r'\bpython\b') # Ne touve pas le motif

resultat = regex.search(chaine)
if resultat:
    print(resultat.group())
else:
    print("Motif non trouvé")
