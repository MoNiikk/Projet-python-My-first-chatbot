import os

#Fonction
def list_of_files(directory, extension):
    files_names =[]
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
directory = "C:/Users/rafaf/OneDrive/pythonProject2/speeches"
files_names = list_of_files(directory, ".txt")
print(files_names)


def pres_names(files_names):
    list_pres_names1 = []
    for name in files_names :
        if 'Chirac2' in name or 'Mitterrand2' in name:
            del(name)
        else :
            list_pres_names1.append(name.split('_')[1])
    list_pres_names = []
    for name in list_pres_names1 :
        if 'Chirac' in name or 'Mitterrand' in name:
            list_pres_names.append(name.split("1")[0])
        else :
            list_pres_names.append(name.split('.')[0])
    return(list_pres_names)


list = pres_names(files_names)
print(list)


def prenom_pres(list) :
    liste_prenoms = ["Jacques", "Valérie", "François", "Manu", "François", "Nico"]
    for i in range (len(list)) :
        liste_prenoms[i] = liste_prenoms[i] + ' ' + list[i]
    return(liste_prenoms)


liste_prenoms = prenom_pres(list)
print(liste_prenoms)


def minuscule (directory, directory2):
    for filename in os.listdir(directory):
        with open(directory +'/' + filename, "r") as f1, open(directory2 + '/' + filename + '2', "x") as f2:
            for lettre in f1.read():
                if ord(lettre)>64 and ord(lettre)<91:
                    lettre=chr(ord(lettre)+32)
                f2.write(lettre)
directory2 = "C:/Users/rafaf/OneDrive/pythonProject2/cleaned"

minuscule(directory, directory2)
def suppr_ponct(directory, directory2) :
    liste_ponct = [',', '.', ';', '-', ':', '!', '_', '?', "'", '(', ')', '[', ']']
    for name in os.listdir(directory2) :
        with open(directory2 + '/' + name, 'r') as f :
            with open(directory + '/' + name + '3', 'x') as f2 :
                for lettre in f.read() :
                    if lettre not in liste_ponct :
                        f2.write(lettre)
                    elif lettre == "'" or lettre == '-' :
                        f2.write(' ')
                    else :
                        f2.write('')

suppr_ponct(directory, directory2)
