import re 

chaine = "le langagae python3   est excellent!"

maListe = re .split(r'\s+',chaine)

print(maListe) #affiche  ['le', 'langagae', 'python3', 'est', 'excellent!']



# regex = re.compile(r'\s+\w+') # Ne touve pas le motif

# resultat = regex.findall(chaine)
# if resultat:
#     print(resultat)
# else:
#     print("Motif non trouvé")
