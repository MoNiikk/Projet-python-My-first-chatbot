import os
import Fonctions as fct

directory2 = "./cleaned"
directory = "./speeches"
files_names = fct.list_of_files(directory, ".txt")
print(files_names)

liste = fct.pres_names(files_names)
print(liste)

liste_prenoms = fct.prenom_pres(liste)
print(liste_prenoms)

fct.minuscule(directory, directory2)

fct.suppr_ponct(directory2)

fct.TF(directory2)
