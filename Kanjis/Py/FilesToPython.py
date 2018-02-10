from os import listdir
from os.path import isfile, join
import CsvToList

def ListeDeFichiers(chemin):
    """
    Lit l'ensemble des fichiers présents dans le répertoire présenté et en sort la liste_fichiers
    Input :
        chemin
    Output :
        Liste : ['[Kanjis] Modèle.csv', '[Kanjis] Nombres.csv']
    """
    liste_fichiers = [f for f in listdir(chemin) if isfile(join(chemin, f))]

    # Debug
    # print(liste_fichiers)

    # Return
    return liste_fichiers

path = "E:\Alexandre\Sites\Wordpress\Sauvegardes\sauvegarde-japon.sobieski.name\Kanjis\CSV\\"

liste_fichiers = ListeDeFichiers(path)
# Liste : ['[Kanjis] Modèle.csv', '[Kanjis] Nombres.csv']

for fichier in liste_fichiers:
    fichier_csv = path + fichier
    print(fichier_csv)

    liste_CSV = CsvToList.convertisseur(fichier_csv)
    print(liste_CSV)
