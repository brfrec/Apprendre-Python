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

print("HEROS 1 :")
Charloutre = Personnage("Charloutre", "Loutre divine", 250)
print("Nom:",Charloutre.nom)
print("Héros:",Charloutre.genre)
print(Charloutre.pdv, "Points de vie") 
print("HEROS 2 :")
Sandyne = Personnage("Sandyne", "Fleur saucisse", 200)
print("Nom:",Sandyne.nom)
print("Héros:",Sandyne.genre)
print(Sandyne.pdv, "Points de vie")
Charloutre.Attaque("morsure vivace", (20))

 # Attaque de Charloutre
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
