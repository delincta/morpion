# Copyright (c) 2020 Copyright Mathis Poteau (delincta) All Rights Reserved.
# coding: utf-8
# un morpion tout ce qui a de plus classique bb

#ici on crée la fenetre
from tkinter import *
from tkinter.messagebox import *

def pointeur(event): #quand tu cliques tu vois, (event pas evennement // bilingue tu vois)
    global a,C1,C2,C3,C1RC,C1R,C2RC,C2R,C3RC,C3R,L1RC,L1R,L2RC,L2R,L3RC,L3R,L1,L2,L3
    # position du pointeur (pas le pointeur à la sortie du lycée, mais bel et bien celui de la souris)
    X = event.x
    Y = event.y

    #Si a == 1 on met une croix  (2 = pas 3 vu que c'est pas js)
    if a == 1:
        if X < 100:
            if Y < 100:
                if C1[0] == 2:
                    a = 0
                    C1[0] = 1
                    L1[0] = 1
                    Croix(50,50)
                else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')
            else :
                if Y < 200:
                    if C1[1] == 2:
                        a = 0
                        C1[1] = 1
                        L2[0] = 1
                        Croix(50,150)
                    else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')
                else :
                    if C1[2] == 2:
                        a = 0
                        C1[2] = 1
                        L3[0] = 1
                        Croix(50,250)
                    else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')

        if X < 200 and X > 100:
            if Y < 100:
                if C2[0] == 3:
                    a = 0
                    C2[0]=1
                    L1[1]=1
                    Croix(150,50)
                else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')
            else :
                if Y < 200:
                    if C2[1] == 3:
                        a = 0
                        C2[1] = 1
                        L2[1] = 1
                        Croix(150,150)
                    else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')
                else :
                    if C2[2] == 3:
                        a = 0
                        C2[2] = 1
                        L3[1] = 1
                        Croix(150,250)
                    else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')

        if X < 300 and X > 200:
            if Y < 100:
                if C3[0] == 4:
                    a = 0
                    C3[0] = 1
                    L1[2] = 1
                    Croix(250,50)
                else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')

            else :
                if Y < 200:
                    if C3[1] == 4:
                        a = 0
                        C3[1] = 1
                        L2[2] = 1
                        Croix(250,150)
                    else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')

                else :
                    if C3[2] == 4:
                        a = 0
                        C3[2] = 1
                        L3[2] = 1
                        Croix(250,250)
                    else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')

    #Des gigas ronds tmtc
    else:
        if X < 100:
            if Y < 100:
                if C1[0] == 2:
                    a = 1
                    C1[0] = 0
                    L1[0] = 0
                    Rond(50,50)
                else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')

            else :
                if Y < 200:
                    if C1[1] == 2:
                        a = 1
                        C1[1] = 0
                        L2[0] = 0
                        Rond(50,150)
                    else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')

                else :
                    if C1[2]==2:
                        a=1
                        C1[2]=0
                        L3[0]=0
                        Rond(50,250)
                    else :
                        showinfo(title='Non',message='Tu ne peux pas !')

        if X < 200 and X > 100:
            if Y < 100:
                if C2[0] == 3:
                    a = 1
                    C2[0] = 0
                    L1[1] = 0
                    Rond(150,50)
                else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')

            else :
                if Y < 200:
                    if C2[1] == 3:
                        a = 1
                        C2[1] = 0
                        L2[1] = 0
                        Rond(150,150)
                    else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')

                else :
                    if C2[2] == 3:
                        a = 1
                        C2[2] = 0
                        L3[1]=0
                        Rond(150,250)
                    else :
                        sshowinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')

        if X < 300 and X > 200:
            if Y < 100:
                if C3[0] == 4:
                    a = 1
                    C3[0] = 0
                    L1[2] = 0
                    Rond(250,50)
                else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')
            else :
                if Y < 200:
                    if C3[1] == 4:
                        a = 1
                        C3[1] = 0
                        L2[2] = 0
                        Rond(250,150)
                    else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')

                else :
                    if C3[2] == 4:
                        a = 1
                        C3[2] = 0
                        L3[2] = 0
                        Rond(250,250)
                    else :
                        showinfo(title = 'Non',message = 'On est où là? Tu peux pas fdp')

#fonction pour afficher les ronds
def Rond(x1,y1):
    global C1,C2,C3
    Canevas.create_oval(x1-45,y1-45,x1+45,y1+45)
    Verif()
#fonction pour afficher les croix (et pas celle des juifs)
def Croix(x1,y1):
    global C1,C2,C3
    Canevas.create_line(x1-45,y1-45,x1+45,y1+45)
    Canevas.create_line(x1+45,y1-45,x1-45,y1+45)
    Verif()
#fonction qui compte les points
def Verif():
    global C1, C2,C3,C1RC,C1R,C2RC,C2R,C3RC,C3R,L1RC,L1R,L2RC,L2R,L3RC,L3R,L1,L2,L3
    C1RC = C1.count(1)
    C1R = C1.count(0)
    C2RC = C2.count(1)
    C2R = C2.count(0)
    C3RC = C3.count(1)
    C3R = C3.count(0)

    L1RC = L1.count(1)
    L1R = L1.count(0)
    L2RC = L2.count(1)
    L2R = L2.count(0)
    L3RC = L3.count(1)
    L3R = L3.count(0)


    #joueur qui a gagné
    if C1RC == 3:
        showinfo(title='Gagne',message='Joueur 1 a gagné !')
    if C1R == 3:
        showinfo(title='Gagne',message='Joueur 2 a gagné !')
    if C2RC == 3:
        showinfo(title='Gagne',message='Joueur 1 a gagné !')
    if C2R == 3:
        showinfo(title='Gagne',message='Joueur 2 a gagné !')
    if C3RC == 3:
        showinfo(title='Gagne',message='Joueur 1 a gagné !')
    if C3R == 3:
        showinfo(title='Gagne',message='Joueur 2 a gagné !')

    if C1[0]==1 and C2[1]==1 and C3[2]==1:
        showinfo(title='Gagne',message='Joueur 1 a gagné !')
    if C1[2]==1 and C2[1]==1 and C3[0]==1:
        showinfo(title='Gagne',message='Joueur 1 a gagné !')

    if C1[0]==0 and C2[1]==0 and C3[2]==0:
        showinfo(title='Gagne',message='Joueur 2 a gagné !')
    if C1[2]==0 and C2[1]==0 and C3[0]==0:
        showinfo(title='Gagne',message='Joueur 2 a gagné !')

    if L1RC == 3:
        showinfo(title='Gagne',message='Joueur 1 a gagné !')
    if L1R == 3:
        showinfo(title='Gagne',message='Joueur 2 a gagné !')
    if L2RC == 3:
        showinfo(title='Gagne',message='Joueur 1 a gagné !')
    if L2R == 3:
        showinfo(title='Gagne',message='Joueur 2 a gagné !')
    if L3RC == 3:
        showinfo(title='Gagne',message='Joueur 1 a gagné !')
    if L3R == 3:
        showinfo(title='Gagne',message='Joueur 2 a gagné !')


#initialisation des colones et des lignes

C1RC,C1R,C2RC,C2R,C3RC,C3R,L1RC,L1R,L2RC,L2R,L3RC,L3R = 0,0,0,0,0,0,0,0,0,0,0,0



a=1

C1=[2,2,2]
L1=[2,2,2]

C2=[3,3,3]
L2=[3,3,3]

C3=[4,4,4]
L3=[4,4,4]

print(C1)




# Création de la fenêtre principale
window = Tk()
window.title("Morpion")
# Création d'un widget Canvas
Largeur = 300
Hauteur = 300
Canevas = Canvas(window, width = Largeur, height =Hauteur, bg ="white")
# La méthode bind() permet de lier un événement avec une fonction :
# un clic gauche sur la zone graphique provoquera l'appel de la fonction utilisateur pointeur()
Canevas.bind("<Button-1>", pointeur)
Canevas.pack(padx =5, pady =5)
#ici on créer les lignes qui délimite les colones et les cases
Canevas.create_line(0,100,300,100,fill="black",width=4)

Canevas.create_line(0,200,300,200,fill="black",width=4)

Canevas.create_line(100,300,300,-100000,fill="black",width=4)

Canevas.create_line(200,300,300,-100000,fill="black",width=4)


# (bouton Quitter)
Button(window, text ="Quitter", command = window.destroy).pack(side=LEFT,padx=5,pady=5)

window.mainloop()
