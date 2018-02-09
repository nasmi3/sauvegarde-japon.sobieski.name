import csv

def convertisseur(fichier):
    """
    Convertit un fichier en listes de listes python et renvoie la grande liste
    Input :
        Chemin/Fichier.csv

    Output :
        Liste
    """
    with open('fichier', 'r') as f:
        reader = csv.reader(f)
        liste_CSV = list(reader)

    print(liste_CSV)
