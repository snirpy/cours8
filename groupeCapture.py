import re

# Chaîne de texte à analyser
texte = "Port: 80, Port: 443, Port: 22"

# Motif regex avec capture des numéros de port
pattern = r"Port: (\d+)"

# Utilisation de finditer pour obtenir un itérateur d'objets match
matches = re.finditer(pattern, texte)

# Parcourir les correspondances trouvées
for match in matches:
    # Accéder au contenu du groupe capturé
    port = match.group(1)
    
    # Obtenir la position dans la chaîne
    start_pos = match.start()
    end_pos = match.end()
    
    print(f"Port trouvé: {port}, Position: {start_pos}-{end_pos}")
