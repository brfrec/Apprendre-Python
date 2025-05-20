# -*- coding: utf-8 -*-

class Personnage:
    def __init__ (self, nom, genre, pdv):
        self.nom = nom
        self.genre = genre
        self.pdv = pdv
        
    def Attaque(self, nom, degats ):
        self.nom = nom
        self.degats = degats

    def Defence(self, soin, echec = 0):
        self.soin = soin
        self.echec = echec
# Personnage 1
print("HEROS 1 :")
Charloutre = Personnage("Charloutre", "Loutre divine", 250)
print("Nom:",Charloutre.nom)
print("Héros:",Charloutre.genre)
print(Charloutre.pdv, "Points de vie") 
# Personnage 2
print("HEROS 2 :")
Sandyne = Personnage("Sandyne", "Fleur saucisse", 200)
print("Nom:",Sandyne.nom)
print("Héros:",Sandyne.genre)
print(Sandyne.pdv, "Points de vie")

# Attaque de Charloutre
Charloutre.Attaque("morsure vivace", (20))
print (Charloutre.genre, "attaque", Sandyne.genre, "avec", Charloutre.nom, 
       "et cause",Charloutre.degats, "points de dégâts")
# Défense de Sandyne
Sandyne.Defence(4, -10)
print (Sandyne.genre, "utilise défence, et se soigne de", Sandyne.soin,
        "points de vie")
print("Défense de fleur saucisse echoue et cause empoisonnement", Sandyne.genre, "perd 10 points de vie")
# Mise a jour des points de vie
Sandyne.pdv = Sandyne.pdv - Charloutre.degats + Sandyne.echec
Sandyne.echec
print(Sandyne.genre, "a", Sandyne.pdv, "points de vie")
print(Charloutre.genre, "a", Charloutre.pdv, "points de vie")

# Attaque de Sandyne
Sandyne.Attaque("pollen boudinné", (15))
print (Sandyne.genre, "attaque", Charloutre.genre, "avec", Sandyne.nom,
       "et cause",Sandyne.degats, "points de dégâts")
# Défense de Charloutre
Charloutre.Defence(5, -1)  
print (Charloutre.genre, "utilise défence, et se soigne de", Charloutre.soin,
        "points de vie")   
print("Défense de loutre divine echoue et cause empoisonnement", Charloutre.genre, "perd 1 points de vie")
# Mise a jour des points de vie 
Charloutre.pdv = Charloutre.pdv - Sandyne.degats + Charloutre.echec
Charloutre.echec
print(Sandyne.genre, "a", Sandyne.pdv, "points de vie") 
print(Charloutre.genre, "a", Charloutre.pdv, "points de vie")
if Sandyne.pdv < Charloutre.pdv:
    print(Sandyne.genre, "a perdu le combat")
elif Sandyne.pdv > Charloutre.pdv:
    print(Charloutre.genre, "a perdu le combat")
# Fin du combat
print("Fin du combat")    
