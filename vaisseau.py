from tkinter import *
from PIL import Image, ImageTk
import projectile as project
class Vaisseau:
    def __init__(self,monde,fenetre,POSX,POSY,TailleVaisseau,Vaisseau,LARGEUR,HAUTEUR,enemy_list_object,enemy_list_image):
        self.fenetre=fenetre
        self.POSX=POSX
        self.POSY=POSY
        self.TailleVaisseau=TailleVaisseau
        self.Vaisseau=Vaisseau
        self.LARGEUR = LARGEUR
        self.HAUTEUR = HAUTEUR
        self.projectile_list = []
        self.monde=monde
        self.enemy_list_object=enemy_list_object
        self.enemy_list_image=enemy_list_image


    def deplacer(self,u,v):
        self.POSX=self.POSX+u
        self.POSY=self.POSY+v
    
    def Clavier(self,event):
        u=0
        v=0
        coords_vaisseau=self.fenetre.ZoneDeJeu.coords(self.Vaisseau)
        """ if event.keysym=='z' and coords_vaisseau[1]>0:
            u=0
            v=-20
        if event.keysym=='s' and coords_vaisseau[1]<self.HAUTEUR+10:
            u=0
            v=20 """
        if event.keysym=='q' and coords_vaisseau[0]>0:
            u=-20
            v=0
        if event.keysym=='d' and coords_vaisseau[0]<self.LARGEUR:
            u=20
            v=0
        self.fenetre.ZoneDeJeu.move(self.Vaisseau,u,v)
    
    
    def creer_projectile(self,event):
        coords_vaisseau=self.fenetre.ZoneDeJeu.coords(self.Vaisseau)
        projectile=project.Projectile(self,self.monde,self.fenetre,(coords_vaisseau[0]+coords_vaisseau[0])/2,coords_vaisseau[1],20,20)
        
        Projectilelast=self.fenetre.ZoneDeJeu.create_image(projectile.px,projectile.py, image = self.fenetre.loaddedKatana)
        self.projectile_list.append(Projectilelast)
        projectile.bouger(Projectilelast,self.projectile_list,self.enemy_list_object)