# -*- coding: utf-8 -*-

class Personnage:
    def __init__ (self, nom, genre, pdv):
        self.nom = nom
        self.genre = genre
        self.pdv = pdv
        
    def Attaque(self, degats ):
        self.degats = degats

    def Defence(self, soin):
        self.soin = soin

Charloutre = Personnage("Charloutre", "Loutre divine", 250)
Charloutre.Attaque(20)
Charloutre.Defence(5)
print("Nom:",Charloutre.nom)
print("Héros:",Charloutre.genre)
print(Charloutre.pdv, "Points de vie") 
Charloutre.Attaque(20)
print("Attaque:",Charloutre.degats, "Dégâts")
Sandyne = Personnage("Sandyne", "Fleur saucisse", 200)
print("Nom:",Sandyne.nom)
print("Héros:",Sandyne.genre)
print(Sandyne.pdv, "Points de vie")
Charloutre.Attaque(20)
Sandyne.Defence(4)
print("Soin:",Sandyne.soin, "Points de vie")
Sandyne.pdv =Sandyne.pdv - (Charloutre.degats -Sandyne.soin)
print("Il reste",Sandyne.pdv, "Points de vie")  