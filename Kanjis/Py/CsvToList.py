import csv

def convertisseur(fichier):
    """
    Convertit un fichier en listes de listes python et renvoie la grande liste
    Input :
        Chemin/Fichier.csv

    Output :
        Liste
    """
    # print(fichier)
    with open(str(fichier), 'r', encoding="utf8") as f:
        reader = csv.reader(f)
        liste_CSV = list(reader)

        # Retire le header !
        liste_CSV = liste_CSV[1:]

    # print(liste_CSV)
    return(liste_CSV)
