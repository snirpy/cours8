import re

# Exemple de logs avec identifiants d'appareils IoT et consommation énergétique
logs = """
Device ID: IoT_123, Consumption: 150kW
Device ID: IoT_456, Consumption: 200kW
Device ID: IoT_789, Consumption: 300kW
"""

# Regex pour capturer l'identifiant de l'appareil et la consommation
pattern = r"Device ID: (IoT_\d+), Consumption: (\d+)kW"

# Utilisation de finditer pour capturer les informations d'appareils
matches = re.finditer(pattern, logs)

# Affichage des résultats
for match in matches:
    device_id = match.group(1)  # Capture l'ID de l'appareil
    consumption = match.group(2)  # Capture la consommation
    print(f"Appareil : {device_id}, Consommation : {consumption}kW")
