import csv
import os

def load_data():
    file_path = os.path.join("data", "ventes.csv")
    
    data = []
    
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # convertir types
            row['Prix'] = float(row['Prix'])
            row['Quantite'] = int(row['Quantite'])
            row['Remise'] = float(row['Remise'])
            
            data.append(row)
    
    return data