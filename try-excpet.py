import re 
texte = 'Ce texte contient un motif.'

try:
    # (?m) est une erreur dan sla regex
    pattern = re.compile(r'motif(?m)')   
    result = pattern.search(texte)
    print(result.group())
except:
    print("Erreur dans l'expression régulière")

