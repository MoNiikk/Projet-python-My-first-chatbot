import os
import Fonctions as fct

directory2 = "./cleaned"
directory = "./speeches"
files_names = fct.list_of_files(directory, ".txt")

liste = fct.pres_names(files_names)

liste_prenoms = fct.prenom_pres(liste)

fct.minuscule(directory, directory2)

fct.suppr_ponct(directory2)

tfidf = fct.tf_idf(directory2)

IDF = fct.idf(directory2)




print("                                  __________________                                    ")
print(" ________________________________/__________________\__________________________________")
print("|                _____     _____  ________   ____      __   __      __                |")
print("|               |     \  /     | |   _____| |     \   |  | |  |    |  |               |")
print("|               |  |\  \/  /|  | |  |____   |  |\  \  |  | |  |    |  |               |")
print("|               |  | \____/ |  | |   ____   |  | \  \ |  | |  |    |  |               |")
print("|               |  |        |  | |  |_____  |  |  \  \|  | |  \____/  |               |")
print("|               |__|        |__| |________| |__|   \_____|  \________/                |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|           1.  Afficher les mots non-importants des textes.                          |")
print("|                                                                                     |")
print("|           2.  Afficher le mot ayant le score TF-IDF le plus important               |")
print("|                                                                                     |")
print("|           3.  Indiquer le mot le plus répété par M. Chirac.                         |")
print("|                                                                                     |")
print("|           4.  Indiquer les noms des présidents qui ont parlé de la « Nation »       |")
print("|               et celui qui l’a répété le plus de fois.                              |")
print("|                                                                                     |")
print("|           5.  Indiquer les noms des présidents qui ont parlé du climat ou           |")
print("|               de l’écologie.                                                        |")
print("|                                                                                     |")
print("|           6.  Poser une question au ChatBot                                         |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")

print("|_____________________________________________________________________________________|")

choix = int(input())
if choix == 1:
    liste_NI = fct.mots_NI(tfidf, IDF)
    print("Les mots les moins importants sont :", end=" ")
    for i in range (len(liste_NI)) :
        print(liste_NI[i], end=", ")
elif choix == 2:
    cle, max1 = fct.tf_idf_max(tfidf, IDF)
    print("Le mot ayant le score TF-IDF le plus élevé est : ", '"', cle, '"', "avec un score de :", max1)
elif choix == 3:
    cle2, max2 = fct.tf_idf_chirac(tfidf, IDF)
    print("Le mot le plus important dit par Chirac est : ", '"', cle2, '"', "avec un score de :", max2)
elif choix == 4:
    print("Les présidents ayant parlé de la Nation sont :")
    fct.nation(tfidf, IDF, liste_prenoms)
elif choix == 6:
    fct.gestion_question(IDF)