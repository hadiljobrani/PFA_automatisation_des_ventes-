import csv
import os

# chemin fichier
file_path = os.path.join("data", "ventes.csv")

# création fichier + données
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # header
    writer.writerow(['ID', 'Prix', 'Quantite', 'Remise'])
    
    # données
    writer.writerow([101, 15.0, 3, 10])
    writer.writerow([102, 25.0, 2, 5])
    writer.writerow([103, 10.0, 5, 0])

print("Fichier ventes.csv créé avec succès ✅")