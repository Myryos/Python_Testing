import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Parse du fichier XML
tree = ET.parse("coverage.xml")
root = tree.getroot()

# Initialisation des listes pour les données
files = []
line_rates = []
branch_rates = []

# Parcourir chaque package et chaque classe pour extraire les données
for package in root.findall("packages/package"):
    for class_ in package.findall("classes/class"):
        filename = class_.get("filename")
        line_rate = float(class_.get("line-rate", 0))
        branch_rate = float(class_.get("branch-rate", 0))

        files.append(filename)
        line_rates.append(line_rate * 100)  # Convertir en pourcentage
        branch_rates.append(branch_rate * 100)  # Convertir en pourcentage

# Créer un graphique à barres pour le taux de couverture des lignes
plt.figure(figsize=(12, 6))
plt.bar(files, line_rates, color="b", label="Line Coverage (%)")
plt.xlabel("Files")
plt.ylabel("Coverage (%)")
plt.title("Line Coverage by File")
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig("line_coverage.png")
plt.show()

# Créer un graphique à barres pour le taux de couverture des branches
plt.figure(figsize=(12, 6))
plt.bar(files, branch_rates, color="g", label="Branch Coverage (%)")
plt.xlabel("Files")
plt.ylabel("Coverage (%)")
plt.title("Branch Coverage by File")
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig("branch_coverage.png")
plt.show()
