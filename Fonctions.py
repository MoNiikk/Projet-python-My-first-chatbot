import os


#Fonction d'extraction du nom des fichiers
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


#Fonction pour lister les noms des présidents
def pres_names(files_names):
    list_pres_names1 = []
    for name in files_names:
        if 'Chirac2' in name or 'Mitterrand2' in name:
            del name
        else:
            list_pres_names1.append(name.split('_')[1])
    list_pres_names = []
    for name in list_pres_names1:
        if 'Chirac' in name or 'Mitterrand' in name:
            list_pres_names.append(name.split("1")[0])
        else:
            list_pres_names.append(name.split('.')[0])
    return list_pres_names

#Fonction pour associer les prénoms aux noms
def prenom_pres(liste):
    liste_prenoms = ["Jacques", "Valérie", "François", "Emanuel", "François", "Nicolas"]
    for i in range(len(liste)):
        liste_prenoms[i] = liste_prenoms[i] + ' ' + liste[i]
    return liste_prenoms

#Fonction pour mettre en minuscules les documents
def minuscule(directory, directory2):
    for filename in os.listdir(directory):
        with open(directory + '/' + filename, "r") as f1, open(directory2 + '/' + filename + '2', "w") as f2:
            for lettre in f1.read():
                if ord(lettre) > 64 and ord(lettre) < 91:
                    lettre = chr(ord(lettre)+32)
                f2.write(lettre)

#Fonction pour enlever les signes de ponctuations
def suppr_ponct(directory2):
    liste_ponct = [',', '.', ';', '-', ':', '!', '', '?', "'", '(', ')', '[', ']']
    for name in os.listdir(directory2):
        with open(directory2 + '/' + name, 'r') as f:
            file = f.read()
        with open(directory2 + '/' + name.split(".")[0] + ".txt", 'w') as f2:
            for lettre in file:
                if lettre not in liste_ponct:
                    f2.write(lettre)
                elif lettre == "'" or lettre == '-':
                    f2.write(" ")
            f2.seek(0, 2)


def TF(directory2):
    for name in os.listdir(directory2):
        tf = {}
        with open(directory2 + '/' + name, 'r') as f:
            for ligne in f :
                for mot in ligne.split():
                    cpt = 0
                    for mot2 in ligne.split():
                        if mot in tf :
                            tf[mot] += 1
                        else :
                            tf[mot] = 1
        print(tf)


