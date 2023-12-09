import os
import Fonctions as fct

directory2 = "C:/Users/rafaf/OneDrive/pythonProject2/cleaned"
directory = "C:/Users/rafaf/OneDrive/pythonProject2/speeches"
files_names = fct.list_of_files(directory, ".txt")
print(files_names)

list = fct.pres_names(files_names)
print(list)

liste_prenoms = fct.prenom_pres(list)
print(liste_prenoms)

fct.minuscule(directory, directory2)


fct.suppr_ponct(directory, directory2)