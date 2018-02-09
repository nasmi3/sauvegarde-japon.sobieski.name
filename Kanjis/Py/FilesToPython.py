from os import listdir
from os.path import isfile, join
from CsvToList import convertisseur

chemin = "E:\Alexandre\Sites\Wordpress\Sauvegardes\sauvegarde-japon.sobieski.name\Kanjis\CSV"

liste_fichiers = [f for f in listdir(chemin) if isfile(join(chemin, f))]

# print(liste_fichiers)
