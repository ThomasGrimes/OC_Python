#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

def testIntMise():
    """Test si la mise donné par le joueur est
    bien un chiffre
    """
    
    testInt = False
    while testInt == False:
        mise = input ("Indiquez votre mise : ")
        if mise.isdigit() == False:
            print("Ce n'est pas un nombre")
        else:
            testInt = True
            return mise

def testIntNum():
    """Test si le numéro donné par le joueur est
    bien un chiffre
    """
    
    testInt = False
    while testInt == False:
        numero = input("Choisissez un numéro entre 0 et 49 : ")
        if numero.isdigit() == False:
            print("Ce n'est pas un nombre")
        else:
            testInt = True
            return numero
        
def testReponse():
    """ Test si la lettre donné est bien 
    soit un Y ou un N
    """
    
    testRecommencer = False
    while testRecommencer == False:
        recommencer = input("Voulez-vous rejouer ? (Y/N)")
        if recommencer.lower() == "y" or recommencer.lower() == "n":
            testRecommencer = True
            return recommencer
        else:
            print("???")