from os import listdir, rename, makedirs
from os.path import isfile, join, exists
import CsvToList
import ListToMd


def ensure_dir(directory):
    """
Impossible de créer les fichiers si le dossier n'existe pas
Créé un dossier si il n'existe pas encore...
    """
    if not exists(directory):
        makedirs(directory)

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
ensure_dir(dossier + "Md\\")
path = dossier + "CSV\\"
ensure_dir(path + 'Done\\')

liste_fichiers = ListeDeFichiers(path)
# Liste : ['[Kanjis] Modèle.csv', '[Kanjis] Nombres.csv']

for fichier in liste_fichiers:
    if fichier != '[Kanjis] Modèle.csv':
        fichier_csv = path + fichier
        # print(fichier_csv)

        liste_CSV = CsvToList.convertisseur(fichier_csv)
        # print(liste_CSV)

        fichier_sans_ext = str(fichier)[:-4]
        contenu_page = '---\n'
        contenu_page +="post_title: '" + fichier_sans_ext + "'\n"
        contenu_page += 'author: Alexandre\n'
        contenu_page += 'layout: post\n'
        contenu_page += 'published: true\n'
        contenu_page += 'categories:\n'
        contenu_page += '  - Kanjis\n'
        contenu_page += '---\n'

        contenu_page += ListToMd.make_page(liste_CSV, list_colors_gradients)

        nom_fichier = dossier + "Md\\"+ f'{fichier_sans_ext}.md'
        md_file = open(str(nom_fichier), 'w', encoding="utf8")
        md_file.write(contenu_page)

        rename(path + fichier, path + 'Done\\' + fichier)

nbre_fichiers = len(liste_fichiers) -1
if nbre_fichiers > 1 :
    print(f"Terminé ! Au total {nbre_fichiers} articles ont été créés.")
elif nbre_fichiers == 1:
    print(f"Terminé ! Au total {nbre_fichiers} article a été créé.")
else:
    print("Aucun article n'a été créé. Le dossier CSV est-il vide ?")
