import os
import math


# Fonction d'extraction du nom des fichiers
def list_of_files(directory, extension):
    files_names = []
    # use regex in the 'for' to avoid the if
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


# Fonction pour lister les noms des présidents
def pres_names(files_names):
    list_pres_names1 = []
    for name in files_names:
        if '2' not in name:
            list_pres_names1.append(name.split('_')[1])
    list_pres_names = []
    for name in list_pres_names1:
        list_pres_names.append(name.split("1")[0] if 'Chirac' in name or 'Mitterrand' in name else name.split('.')[0])
    return list_pres_names


# Fonction pour associer les prénoms aux noms
def prenom_pres(liste):
    liste_prenoms = ["Jacques", "Valérie", "François", "Emanuel", "François", "Nicolas"]
    # use enumerate to avoid range func
    for i in range(len(liste)):
        liste_prenoms[i] = liste_prenoms[i] + ' ' + liste[i]
    return liste_prenoms


# Fonction pour mettre en minuscules les documents
def minuscule(directory, directory2):
    for filename in os.listdir(directory):
        with open(directory + '/' + filename, "r") as f1, open(directory2 + '/' + filename, "w") as f2:
            for lettre in f1.read():
                if ord(lettre) > 64 and ord(lettre) < 91:
                    lettre = chr(ord(lettre)+32)
                f2.write(lettre)


# Fonction pour enlever les signes de ponctuations
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
        f.close()


def TF(f):
    tf = {}
    for mot in f.split():
        if mot in tf:
            tf[mot] += 1
        else:
            tf[mot] = 1
    return tf


def idf(directory2):
    dic_idf = {}
    nb_doc = 0
    liste_mot = []
    for name in os.listdir(directory2):
        nb_doc += 1
        with open(directory2 + '/' + name, 'r') as f:
            for ligne in f:
                for mot1 in ligne.split():
                    if mot1 not in liste_mot :
                        liste_mot.append(mot1)
                        n = 0
    for mot in liste_mot :
        n = 0
        for name in os.listdir(directory2):
            with open(directory2 + '/' + name, 'r') as f2:
                v = 0
                for ligne2 in f2:
                    for mot2 in ligne2.split():
                        if mot == mot2:
                            v = 1
                            break
                n += v
        idfval = math.log10((nb_doc / n)+1)
        dic_idf[mot] = idfval
    return dic_idf

def tf_idf(directory2) :
    M = []
    IDF = idf(directory2)
    for name in os.listdir(directory2):
        L = []
        with open(directory2 + '/' + name, 'r') as f:
            tf = TF(f.read())
            for key in IDF.keys() :
                if key in tf.keys() :
                    L.append(tf[key]*IDF[key])
                else :
                    L.append(0.00)
        M.append(L)
    tfidf = []
    for i in range(len(M[0])):
        L = []
        for j in range(8):
            L.append(M[j][i])
        tfidf.append(L)
    return tfidf

def mots_NI(tfidf, IDF):
    L = []
    for i in range(len(tfidf)):
        cpt = 0
        for j in range(8):
            if int(tfidf[i][j]) == 0:
                cpt += 1
        if cpt == 7:
            cpt = 0
            for key in IDF:
                cpt += 1
                if cpt == i:
                    L.append(key)
    return L

def tf_idf_max(tfidf, IDF):
    max = 0
    for i in range(len(tfidf)):
        for j in range(8):
            if tfidf[i][j] > max:
                val = i
                max = tfidf[i][j]
    cpt = 0
    for key in IDF:
        cpt += 1
        if cpt == val:
            return key, max

def tf_idf_chirac(tfidf, IDF):
    max = 0
    for i in range(len(tfidf)):
        for j in range(2):
            if tfidf[i][j] > max:
                val = i
                max = tfidf[i][j]
    cpt = 0
    for key in IDF:
        cpt += 1
        if cpt == val:
            return key, max

def nation(tfidf, IDF, liste_prenom):
    cpt = 0
    for key in IDF.keys():
        cpt += 1
        if key == "nation":
            print(tfidf[cpt][6])
            for i in range(7):
                if tfidf[cpt][i] != 0:
                    print(liste_prenom[i - 2 if i>2 else i])

def tfidf_phrase(f):
    tfidfmot = {}
    with open(f, "w") as f :
        tf = TF(f)
        for key in d.keys():
            idfval = math.log10((1 / tf[key]) + 1)
            tfidfmot[key] = idfval * tf[key]
    return tfidfmot

def questionuser ():
    quest= str(input("Veuillez saisir une question a poser."))
    L=quest.split(" ")
    return L


def recherche_question(L, IDF):
    liste_mot = []
    for key in IDF.keys():
        if key in L :
            liste_mot.append(key)
    return liste_mot

def gestion_question (IDF):
    questionlist=questionuser()
    listprio=recherche_question(questionlist, IDF)
    return listprio