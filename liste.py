# Les listes

une_liste = [8, 3, 1, 14, 22]
une_autre_liste = ["Bonjour", "Salut", "Hello"]
longueur_liste_un = len(une_liste)
print(longueur_liste_un)
liste_dans_l_ordre = sorted(une_liste, reverse=True)
print(liste_dans_l_ordre)
# Les deux listes dans une autre liste

toute_liste = [une_liste, une_autre_liste]
print(toute_liste)
print(toute_liste[1][1])
# Ajouter un élément a une liste
toute_liste[1].append("Coucou")
print(toute_liste)
toute_liste[1].insert(3, "Hi")
print(toute_liste)
toute_liste[0].append(36)
print(toute_liste)  

"""
# Supprimer un élément d'une liste
toute_liste[1].remove("Salut") 
print(toute_liste)
toute_liste[1].pop(0) # Supprime le premier élément de la liste
toute_liste[1].pop() # Supprime le dernier élément de la liste
toute_liste[1].clear() # Supprime tous les éléments de la liste
toute_liste[1].extend(["Bonjour", "Salut", "Hello"]) # Ajoute plusieurs éléments a la liste
toute_liste[1].insert(0, "Bonjour") # Ajoute un élément a la liste a l'index 0
print(toute_liste)
"""