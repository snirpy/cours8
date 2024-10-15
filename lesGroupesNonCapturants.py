import re
logs = """
Device IoT_123 | Status: ERROR 500
Device IoT_456 | Status: OK
Device IoT_789 | Status: ERROR 404
"""
pattern = r"Device (IoT_\d+) \| (?:Status: ERROR) (\d+)"
matches = re.finditer(pattern, logs)
for match in matches:
    device_id = match.group(1)  # Capture l'ID de l'appareil
    error_code = match.group(2)  # Capture le code d'erreur
    print(f"Appareil : {device_id}, Code d'erreur : {error_code}")




