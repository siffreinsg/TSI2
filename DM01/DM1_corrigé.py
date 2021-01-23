# TSI Versailles
import os
os.chdir('I:\\DM1_seuillage+centre de gravité')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#affichage image couleur
img=mpimg.imread('im1.png')
plt.figure(0)
plt.imshow(img)

#seuillage a partir d'une image RGB
print(img[0,0])
print(img[200,300])
print(img.shape)

#Q1
s_rgb=[0.5,1,0,1,0,1]

#Q2
def seuillage_pixel(p,seuil):
    amin,amax,bmin,bmax,cmin,cmax=seuil
    if amin<p[0]<amax and bmin<p[1]<bmax and cmin<p[2]<cmax:
        p=[1,1,1] 
    else:
        p=[0,0,0] 
    return(p)

#Q3
def seuillage(im,seuil):       
    '''seuille l'image im en utilisant le tableau seuil=[hmin,hmax,smin,smax,vmin,vmax]'''
    a,b,c=im.shape    
    im_s=np.zeros([a,b,c]) 
    for i in range(a):
        for j in range(b):
            im_s[i,j]=seuillage_pixel(im[i,j],seuil)
    return(im_s)

#Q4
img_s=seuillage(img,s_rgb)
plt.figure(1)
plt.imshow(img_s)
plt.imsave("im_s0.png",img_s) 
#le résultat est perfectible, en effet, la voiture n'est pas correctement isolée !

#seuillage à partir d'une image HSV

#Q5
def mini(l):
    '''retourne le minimum de la liste l'''
    m=l[0]
    for e in l:
        if e<m:
            m=e
    return(m)

def maxi(l):
    '''retourne le maximum de la liste l'''
    m=l[0]
    for e in l:
        if e>m:
            m=e
    return(m)
#>>> maxi([4,1,6])
#6
#>>> mini([4,1,6])
#1

#Q6
def RGB_to_HSV(rgb):
    '''retourne la liste de 3 éléments [h,s,v] calculée à partir de la liste de 3 éléments  [r,g,b]'''
    R,G,B=rgb
    Cmax=maxi(rgb)
    delta=maxi(rgb)-mini(rgb)
    eps=0.000000001
    #calcul de H
    if abs(delta) < eps:
        H=0
    else:
        if R==Cmax:
            H=1/6*(((G-B)/delta)%6)
        elif G==Cmax:
            H=1/6*(2+(B-R)/delta)
        elif B==Cmax:
            H=1/6*(4+(R-G)/delta)
    #calcul de S
    if abs(Cmax)<eps:
        S=0
    else:
        S=delta/Cmax
    
    V=Cmax
    return([H,S,V])

#blanc
#>>> rgb_to_hsv([1,1,1])
#[0, 0, 1]
#noir
#>>> rgb_to_hsv([0,0,0])
#[0, 0, 0]
#rouge
#>>> rgb_to_hsv([1,0,0])
#[0.0, 1.0, 1]

#Q7
def conversion_RGB_HSV(im_rgb):
    '''convertit une image au format rgb au format hsv'''
    a,b,c=im_rgb.shape    
    im_hsv=np.zeros([a,b,c])    
    for i in range(a):
        for j in range(b):
           hsv=RGB_to_HSV(im_rgb[i,j])
           im_hsv[i,j]=hsv
    return(im_hsv)

#Q8
s_hsv=[0.7,1,0.5,1,0,1]

#Q9
img_hsv=conversion_RGB_HSV(img)
img_s1=seuillage(img_hsv,s_hsv)

plt.figure(2)
plt.imshow(img_s1) 
#plt.imshow(img_s,cmap='gray')
plt.show()

#Q10 : version amméliorée du seuillage 
def seuillage_pixel2(p,seuil):
    amin,amax,bmin,bmax,cmin,cmax=seuil
    if amax<amin: #cas où il faut prendre l'intervalle disjoint
        test_a= (0<p[0]<amax or amin<p[0]<1)
    else :
        test_a = amin<p[0]<amax
    
    if test_a and bmin<p[1]<bmax and cmin<p[2]<cmax:
        p=[1,1,1] 
    else:
        p=[0,0,0] 
    return(p)

#Q3
def seuillage2(im,seuil):       
    '''seuille l'image im en utilisant le tableau seuil=[hmin,hmax,smin,smax,vmin,vmax]'''
    a,b,c=im.shape    
    im_s=np.zeros([a,b,c])  
    for i in range(a):
        for j in range(b):
            im_s[i,j]=seuillage_pixel2(im[i,j],seuil)
    return(im_s)

#seuillage sur image 2
img=mpimg.imread('im2.png')
img_hsv=conversion_RGB_HSV(img)
s_hsv=[0.8,0.2,0.5,1,0,1]
img_s2=seuillage2(img_hsv,s_hsv)
plt.figure(3)
plt.imshow(img_s2) 
#plt.imshow(img_s2,cmap='gray')
plt.imsave("im_s2.png",img_s2,cmap='gray')

#comparaison avec l'ancienne technique
s_hsv=[0,0.2,0.5,1,0,1]
img_s3=seuillage(img_hsv,s_hsv)
plt.figure(4)
plt.imshow(img_s3)
#plt.imshow(img_s2,cmap='gray')
plt.imsave("im_s3.png",img_s3,cmap='gray')


#Q10-11
def cherche_centre(im):
    '''détermine le centre de gravité avec les formules du barycentre, utilisation des fonctions numpy pour réaliser la somme , im est l'image seuillée'''
    h=im.shape[0] #hauteur de l'image en pixels
    l=im.shape[1] #largeur de l'image en pixels
    im2D = im[:,:,0] #conversion de l'image : le contenu d'un pixel sera un nombre (ex : 1) au lieu d'une liste de 3 nombres identiques (ex : [1,1,1])
    
    sL=np.sum(im2D,0) #liste contenant la somme des lignes pour chaque colonne
    nC=np.arange(l) # liste contenant les indexs des colonnes : commence à zéro
    pos_p_x=sL*nC # liste contenant les positions pondérées
    
    sC=np.sum(im2D,1) #liste contenant la somme des colonnes pour chaque ligne
    nL=np.arange(h) #liste contenant les indexs des lignes 
    pos_p_y=sC*nL  #liste contenant les positions pondérées
    
    s=(np.sum(sL,0)) #somme de tous les éléments de la matrice
    
    if s>0: #calcul dans le cas où s n'est pas nul
        xg=np.sum(pos_p_x,0)/s #somme sur les colonnes des positions pondérées 
        yg=np.sum(pos_p_y,0)/s #somme sur les lignes des positions pondérées
    else: # si tous les pixels sont noirs, on place le cdg au centre de l'image
        xg=l/2
        yg=h/2
    return xg,yg

plt.figure(2)    
x,y=cherche_centre(img_s1)
plt.plot([x],[y],'g^')

plt.figure(3)
x,y=cherche_centre(img_s2)
plt.plot([x],[y],'r^')

plt.show()






