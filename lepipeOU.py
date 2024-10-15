import re
logs_reseau = """
2024-10-12 10:15:32 Protocole: TCP Connexion établie
2024-10-12 10:16:45 Protocole: UDP Connexion établie
2024-10-12 10:17:58 Protocole: TCP Connexion terminée
"""
pattern = r"TCP|UDP"

result = re.findall(pattern, logs_reseau)
print(result)  # ['TCP', 'UDP', 'TCP']

