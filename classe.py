# -*- coding: utf-8 -*-

class Personnage:
    def __init__ (self, nom, genre, pdv):
        self.nom = nom
        self.genre = genre
        self.pdv = pdv
        
    def Attaque(self, nom, degats ):
        self.nom = nom
        self.degats = degats

    def Defence(self, soin):
        self.soin = soin

Charloutre = Personnage("Charloutre", "Loutre divine", 250)
print("Nom:",Charloutre.nom)
print("Héros:",Charloutre.genre)
print(Charloutre.pdv, "Points de vie") 
Sandyne = Personnage("Sandyne", "Fleur saucisse", 200)
print("Nom:",Sandyne.nom)
print("Héros:",Sandyne.genre)
print(Sandyne.pdv, "Points de vie")
Charloutre.Attaque("morsure vivace", (20))

Sandyne.Defence(4)
print("Soin:",Sandyne.soin, "Points de vie")
Sandyne.pdv =Sandyne.pdv - (Charloutre.degats -Sandyne.soin)
print("Il reste",Sandyne.pdv, "Points de vie")  
print (Charloutre.genre, "attaque", Sandyne.genre, "avec", Charloutre.nom, "et cause",Charloutre.degats, "points de dégâts")
