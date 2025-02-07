from datetime import datetime

# Fichier d'entrée contenant les dates
input_file = "satoshi_commits.txt"
# Fichier de sortie pour les timestamps
output_file = "timestamps.txt"

# Format de la date à convertir
date_format = "%a, %d %b %Y %H:%M:%S %z"

# Liste pour stocker les timestamps
timestamps = []

# Lire les dates à partir du fichier d'entrée
with open(input_file, "r", encoding='utf-8') as file:
    for line in file:
        date_str = line.strip()[:-1]
        if date_str:  # Vérifier que la ligne n'est pas vide
            # Convertir la date en timestamp
            timestamp = int(datetime.strptime(date_str, date_format).timestamp())
            timestamps.append(timestamp)

# Écrire les timestamps dans le fichier de sortie
with open(output_file, "w", encoding='utf-8') as file:
    for ts in timestamps:
        file.write(f"{ts}\n")

print(f"Timestamps have been written to {output_file}.")
