import re
# lookahead
pattern = re.compile(r'\d+(?=%)')

chaine = "15% de réduction sur le prix initial de  100€ "
result = pattern.match(chaine)
if result:
    print(result.group())
else:
    print("Motif nom trouvé")

