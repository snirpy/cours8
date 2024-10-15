import re

# Logs réseau simulés
logs_reseau = """
2024-10-12 10:15:32 IP: 192.168.1.1 Connexion établie
2024-10-12 10:16:45 IP: 10.0.0.5 Connexion refusée
2024-10-12 10:17:58 IP: 172.16.0.3 Connexion établie
"""

# Motif regex pour capturer les adresses IP
pattern = r"IP: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

# Utilisation de finditer pour parcourir les adresses IP trouvées
matches = re.finditer(pattern, logs_reseau)

# Parcourir les correspondances trouvées
for match in matches:
    # Récupérer l'adresse IP capturée
    ip_address = match.group(1)
    
    # Obtenir les positions des correspondances dans les logs
    start_pos = match.start()
    end_pos = match.end()
    
    print(f"Adresse IP trouvée: {ip_address}, Position: {start_pos}-{end_pos}")
