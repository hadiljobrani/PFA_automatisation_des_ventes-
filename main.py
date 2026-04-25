from src.data_loader import load_data
from src.calcule import *
import matplotlib.pyplot as plt


data = load_data()

print(data)


data = load_data()

data = calcul_ca_brut(data)
print("Après CA_Brut:", data)

data = calcul_ca_net(data)
print("Après CA_Net:", data)
data = calcul_tva(data)
print("Après TVA:", data)

total = calcul_total(data)
best = best_produit(data)

export_resultats(data)

print("CA Total =", total)
print("Best produit =", best)


# IDs و CA_Net
ids = [row['ID'] for row in data]
ca_net = [row['CA_Net'] for row in data]

plt.figure()
plt.bar(ids, ca_net)

plt.title("Graph des ventes (CA Net par produit)")
plt.xlabel("Produit ID")
plt.ylabel("CA Net")

plt.show()