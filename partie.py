from tkinter import *
from vaisseau import *
from projectile import *
from protection import *
import monde as m
import enemy as e
import Fenetre as ctk
import random,math
from PIL import Image, ImageTk


class Partie:

    def __init__(self, fenetre,DIFFICULTEE,DY,VITESSE,LARGEUR,HAUTEUR):
        self.DIFFICULTEE = DIFFICULTEE
        self.DY = DY
        self.VITESSE = VITESSE
        self.fenetre = fenetre
        self.LARGEUR = LARGEUR
        self.HAUTEUR = HAUTEUR

    def lancementPartie(self):
        
        self.fenetre.ZoneDeJeu.focus_force()
        
        """
        -AJOUTER LE RESET DU SCORE ET DES VIE DANS LE LABEL DE LA CLASSE TK
        """

        monde=m.Monde(self.fenetre,self.DIFFICULTEE, self.DY,self.VITESSE,self.LARGEUR,self.HAUTEUR)