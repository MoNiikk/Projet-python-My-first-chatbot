import os
import Fonctions as fct


def menu():
    choice = int(input(" ___________________________________________________________________________ \n|                    Quelles actions voulez vous faire ?                     | \n|                                  | \n|                                   | \n|                      | \n|        4. Afficher les présidets ayant dit le mot 'Nation'.                |  \n|        5. Afficher le premier président qui parle du climat.               | \n|        6. Afficher les mots les plus répétés en dehors des non importants. |  \n|____________________________________________________________________________|\n"))
    if choice == 1:
        print("yes")
    else:
        print(choice)
    return choice