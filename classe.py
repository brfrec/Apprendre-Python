# -*- coding: utf-8 -*-
# Création de la classe 'gateau'
class gateau:
    def __init__(self, parfum, taille):# self + recette de la classe 'gateau
        self.parfum = parfum
        self.taille = taille

    def CouperEnPpart(self, part = 4):# Que fait on avec ce 'gateau'
        self.part = part
        print("Le gateau est coupé en ", self.part, "parts")

# Création d'un objet 'gateau' au chocolat de grande taille 

gateauChoc = gateau("chocolat", "grand")
print ("Le ", (gateauChoc.taille), "gateau est au ", (gateauChoc.parfum))
      
gateauChoc.CouperEnPpart(6)# Le grand 'gateau' sera coupé en 6 parts

gateauBanane = gateau("banane", "minuscule")#Création d'un objet minuscule 'gateau' a la banane
print ("Le ", (gateauBanane.taille), "gateau est a la ", (gateauBanane.parfum))
gateauBanane.CouperEnPpart(2)# Coupé en deux parts

class Voiture:
    def __init__(self, marque, couleur, puissance):
        self.marque = marque
        self.couleur = couleur
        self.puissance = puissance

    def Accelerer(self, vitesse):
        self.vitesse = vitesse
        print("La voiture ", (self.marque), "accélère à", (self.vitesse), "km/h") 
    
    def Freiner(self, vitesse):
        self.vitesse = vitesse
        print("La voiture ", (self.marque), "freine à", (self.vitesse), "km/h")

QL = Voiture("Renault 4L", "orange", "180 ch")
print("La voiture est une ", (QL.marque), "de couleur ", (QL.couleur), "et de puissance ", (QL.puissance))
QL.Accelerer(280)
QL.Freiner(0)
