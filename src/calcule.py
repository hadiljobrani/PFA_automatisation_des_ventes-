import csv
import os
def calcul_ca_brut(data):
    for row in data:
        row['CA_Brut'] = row['Prix'] * row['Quantite']

    return data
def calcul_ca_net(data):
    for row in data:
        row['CA_Net'] = row['CA_Brut'] * (1 - row['Remise']/100)

    return data
def calcul_tva(data):
    for row in data:
        row['TVA'] = row['CA_Net'] * 0.2

    return data
def calcul_total(data):
    total = 0

    for row in data:
        total += row['CA_Net']

    return total
def best_produit(data):
    max_ca = 0
    best_id = None

    for row in data:
        if row['CA_Net'] > max_ca:
            max_ca = row['CA_Net']
            best_id = row['ID']

    return best_id


def export_resultats(data):
    file_path = os.path.join("data", "resultats_final.csv")

    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['ID','Prix','Quantite','Remise','CA_Brut','CA_Net','TVA']

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

