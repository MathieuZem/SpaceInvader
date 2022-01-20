from tkinter import *
from PIL import Image, ImageTk
import random
import projectile as project
class Enemy:
    def __init__(self,monde,fenetre,tag,VITESSE,posX, posY,DY):
        self.fenetre = fenetre
        self.tag=tag
        self.loadShuriken = None
        self.loaddedShuriken = None
        self.loadLance = None
        self.loaddedLance = None
        self.posX=posX
        self.posY=posY
        self.VITESSE=VITESSE
        self.DY=DY
        self.ProjectileEnemy = []
        self.monde = monde

        self.image()

    def getTag(self):
        return self.tag

    def getPosX(self):
        self.posX
        return self.posX

    def getPosY(self):
        return self.posY

    def getVITESSE(self):
        return self.VITESSE

    def getDY(self):
        return self.DY

    def deplacer(self, NewposX, NewposY):
        self.posX = NewposX
        self.posY = NewposY
        """ print("Position actuelle", self.posX, " ", self.posY,) """
    
    def tirer(self):
        print("Je tire")


    def image(self):

        self.loadShuriken = Image.open("image/Shuriken/Shuriken.png")
        self.loaddedShuriken =ImageTk.PhotoImage(self.loadShuriken)

        self.loadLance = Image.open("image/Shieldmaiden/Lance1.png")
        self.loaddedLance =ImageTk.PhotoImage(self.loadLance)

    def deplacementEnemy(self,VITESSE,DY,enemy_list_object,enemy_list_image,LARGEUR,ennemy_liste_object,rectangle,CANVAS_WIDTH,CANVAS_HEIGHT):
        
        DX = VITESSE
        DY = 0
        most_right = 0
        most_left = CANVAS_WIDTH

        for ennemie in enemy_list_object:
            ennemie_pos_x = ennemie.getPosX()
            if ennemie_pos_x > most_right:
                most_right = ennemie_pos_x

        for ennemie in enemy_list_object:
            ennemie_pos_x = ennemie.getPosX()
            if ennemie_pos_x < most_left:
                most_left = ennemie_pos_x

        """ most_left = enemy_list_object[0].getPosX()
        most_right = enemy_list_object[-1].getPosX() """

        posy=enemy_list_object[-1].getPosY()

        most_left += DX
        most_right += DX    

        if posy >= CANVAS_HEIGHT-30:
            k=0
            for i in range(len(ennemy_liste_object)):
                del self.myEnemyList[k]
                self.ZoneDeJeu.delete(self.myEnemy[k])
                del self.myEnemy[k]
                

        else:
            for i in range(len(ennemy_liste_object)):
                posx=enemy_list_object[i].getPosX()
                posy=enemy_list_object[i].getPosY()
                for o in rectangle:
                    coords_protection=self.ZoneDeJeu.coords(o)
                    verif_collision=self.fenetre.collision_enemy_protection(coords_protection[0],coords_protection[1],32/2,posx,posy)
                    if verif_collision==True:
                        self.ZoneDeJeu.delete(o)
                        self.rectangle.remove(o)

            if most_right + 20 > CANVAS_WIDTH:
                most_right= 2*CANVAS_WIDTH - most_right
                VITESSE = -DX
                DY = 60

            if most_left -20 < 0:
                most_left = -most_left
                VITESSE = -DX
                DY = 60

            for i,val in enumerate(enemy_list_image):
                self.fenetre.ZoneDeJeu.move(enemy_list_image[i],DX,DY)
                enemy_list_object[i].deplacer(enemy_list_object[i].getPosX()+DX,enemy_list_object[i].getPosY()+DY)


        self.fenetre.FrameGauche.after(20,self.deplacementEnemy,VITESSE,self.DY,enemy_list_object,enemy_list_image,LARGEUR,ennemy_liste_object,rectangle,CANVAS_WIDTH,CANVAS_HEIGHT)




    def autoTir(self,difficulty,enemy_list_object,enemy_list_image,HAUTEUR):
     
        frameCntProj = 2
        """ imageProj = [PhotoImage(file='image/Shuriken/Shuriken.gif',format = 'gif -index %i' %(i)) for i in range(frameCntProj)] """
        if len(enemy_list_object) > 1:
            max = len(enemy_list_image)-1

            rand=random.randint(0,max)

            coordsEnemyX = enemy_list_object[rand].getPosX()
            coordsEnemyY = enemy_list_object[rand].getPosY()
            

            

            
            self.fenetre.FrameGauche.after(750,self.autoTir,difficulty,enemy_list_object,enemy_list_image,HAUTEUR)

            projectile_enemy=project.Projectile(self,self.monde,self.fenetre,self.getPosX,self.getPosY,20,self.VITESSE)
            ProjectileEnemylast=self.fenetre.ZoneDeJeu.create_image(coordsEnemyX,coordsEnemyY, image = self.loaddedShuriken)
            self.ProjectileEnemy.append(ProjectileEnemylast)
            projectile_enemy.deplacementProjectEautoTir(ProjectileEnemylast,coordsEnemyY,self.ProjectileEnemy,HAUTEUR)


        else:
            max = len(enemy_list_image)-1

            rand=random.randint(0,max)

            coordsEnemyX = enemy_list_object[rand].getPosX()
            coordsEnemyY = enemy_list_object[rand].getPosY()

            ProjectileEnemylast=self.fenetre.ZoneDeJeu.create_image(coordsEnemyX,coordsEnemyY, image = self.loaddedLance)

            self.ProjectileEnemy.append(ProjectileEnemylast)
            self.fenetre.FrameGauche.after(750,self.autoTir,difficulty,enemy_list_object,enemy_list_image,HAUTEUR)

            projectile_enemy=project.Projectile(self,self.monde,self.fenetre,self.getPosX,self.getPosY,20,self.VITESSE)
            projectile_enemy.deplacementProjectEautoTir(ProjectileEnemylast,coordsEnemyY,self.ProjectileEnemy,HAUTEUR)

