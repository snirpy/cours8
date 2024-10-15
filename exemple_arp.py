import re

# La chaîne contenant les adresses IP
chaine = """
? (192.168.1.11) at b8:27:eb:8f:44:82 on en0 ifscope [ethernet]
? (192.168.1.31) at 3e:82:42:73:d5:de on en0 ifscope [ethernet]
? (192.168.1.120) at 0:e0:4c:68:ed:f9 on en0 ifscope [ethernet]
? (192.168.1.123) at 82:aa:48:1:19:d3 on en0 ifscope [ethernet]
? (192.168.1.127) at d2:23:9b:54:e1:3 on en0 ifscope [ethernet]
? (192.168.1.131) at 72:57:f:ee:dd:da on en0 ifscope [ethernet]
? (192.168.1.153) at 6e:95:a4:e:27:3c on en0 ifscope [ethernet]
? (192.168.1.188) at 8:e3:6c:5:d2:7e on en0 ifscope [ethernet]
? (192.168.1.254) at 38:7:16:a2:a7:9a on en0 ifscope [ethernet]
? (192.168.1.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
mdns.mcast.net (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]
"""

# Expression régulière pour correspondre aux adresses IP (IPv4)
regex_ip = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

mac_regex = r'\b(?:[0-9a-fA-F]{1,2}:){5}[0-9a-fA-F]{1,2}\b'



# Extraction des adresses IP
adresses_ip = re.findall(regex_ip, chaine)
adresses_mac = re.findall(mac_regex, chaine)
# print(adresses_mac)
# Affichage des adresses IP
for i in range(len(adresses_ip)):
    print(f"{i+1}:\t{adresses_ip[i]} \t {adresses_mac[i]}")
