from os import listdir
from os.path import isfile, join
import CsvToList
import ListToMd

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



# Parameters
# Modèle [[couleur1, couleur 2, orientation],[...],...]

list_colors_gradients = [["#fc6076","#ff9a44","1deg"], ["#32a37b", "#0dc44a", "96deg"], ["#764ba2", "#667eea", "135deg"], ["#005bea", "#00c6fb", "0deg"], ["#13547a", "#80d0c7", "15deg"], ["#fc6076", "#09203f", "1deg"]]

dossier = "E:\Alexandre\Sites\Wordpress\Sauvegardes\sauvegarde-japon.sobieski.name\Kanjis\\"
path = dossier + "CSV\\"

liste_fichiers = ListeDeFichiers(path)
# Liste : ['[Kanjis] Modèle.csv', '[Kanjis] Nombres.csv']

for fichier in liste_fichiers:
    fichier_csv = path + fichier
    # print(fichier_csv)

    liste_CSV = CsvToList.convertisseur(fichier_csv)
    # print(liste_CSV)

    fichier_sans_ext = str(fichier)[:-4]
    contenu_page = '# ' + fichier_sans_ext + ' \n'
    contenu_page += ListToMd.make_page(liste_CSV, list_colors_gradients)

    nom_fichier = dossier + "Md\\"+ f'{fichier_sans_ext}.md'
    md_file = open(str(nom_fichier), 'w', encoding="utf8")
    md_file.write(contenu_page)

nbre_fichiers = len(liste_fichiers)
if nbre_fichiers > 1 :
    print(f"Terminé ! Au total {nbre_fichiers} articles ont été créés.")
elif nbre_fichiers == 1:
    print(f"Terminé ! Au total {nbre_fichiers} article a été créé.")
else:
    print("Aucun article n'a été créé. Le dossier CSV est-il vide ?")
