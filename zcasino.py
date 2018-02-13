#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Zcasino

import os
import random
import math
from testing.f2Test import *

joueur = 50
testMise = False
testNumero = False
depart = True

while depart == True and joueur != 0:
    
    while testMise == False:
        print("Votre pot s'élève a :",joueur,"$")
######################## FONCTION f2Test #############################
        mise = testIntMise()
#######################################################################
        if int(mise) > int(joueur):
            print("Vous n'avez pas autant d'argent")
        elif int(mise) <= 0:
            print("Vous ne pouvez pas miser cette somme")
        else:
            print("Entendu")
            joueur = int(joueur) - int(mise)
            testMise = True

    while testNumero == False:
######################## FONCTION f2Test #############################
        numero = testIntNum()
#######################################################################
        if int(numero) > 49 or int(numero) < 0:
            print("Vous n'avez pas choisi une bonne valeur, recommencez")
        else:
            print("Parfait, c'est partit !")
            testNumero = True

    roulette = random.randrange(50)
    print("Le numéro est ",roulette)

    if roulette == numero:
        print("Bravo, vous avez triplé votre mise !")
        joueur += (int(mise)*3)
    elif int(roulette)%2 == 0 and int(numero)%2 == 0:
        print("Vous êtes pair tout les deux, vous remportez la moitié de votre mise")
        moitie = int(mise)/2
        moitieMise = math.ceil(moitie)
        joueur += moitieMise
    elif int(roulette)%2 != 0 and int(numero)%2 != 0:
        print("Vous êtes impair tout les deux, vous remportez la moitié de votre mise")
        moitie = int(mise)/2
        moitieMise = math.ceil(moitie)
        joueur += moitieMise
    else:
        print("Vous avez perdu !")
    
    if joueur <= 0:
        print("Vous ne possèdez plus d'argent, au revoir")
    else:
        print("Votre pot s'élève dorénavant a :",joueur,"$")
######################## FONCTION f2Test #############################
        recommencer = testReponse()
#######################################################################
        if recommencer.lower() =="y":
            print("C'est repartit !")
            testMise = False
            testNumero = False
            testRecommencer = False
        else:
            depart = False

input("Taper entrer pour terminer le programme ...")
os.system("pause")
