## Transformée de Fourier discrète

## Import des librairies

from math import pi,cos
from cmath import exp
from matplotlib import pyplot as plt
plt.close('all')

## Définition du signal test

def f1(t,A,fs):
    ws = 2*pi*fs
    return A*cos(ws*t)

def Affiche(fig,Lx,Ly,Col):
    plt.figure(fig)
    plt.plot(Lx,Ly,'o'+Col)
    plt.plot(Lx,Ly,'--'+Col)
    plt.show()
    plt.pause(0.000001)

def Donnees(N,fe,f,fs):
    Te = 1/fe
    t0 = 0
    Lt = [t0 + n*Te for n in range(N)]
    Lf = [fe*i/N for i in range(N//2+1)]
    Ly = [f(t,A,fs) for t in Lt]
    return Lt,Lf,Ly

N = 16
fs = 1
A = 1
fe = fs*N
Lt,Lf,Ly = Donnees(N,fe,f1,fs)
Affiche(1,Lt,Ly,'k')

## Transformée de Fourier classique

def f_ck(Ly,k):
    N = len(Ly)
    Somme = 0
    for n in range(N): # N-1 inclus
        Ajout = Ly[n]*exp(-1j*2*k*pi*n/N)
        Somme += Ajout
    return Somme

def dft(Ly):
    Somme = 0
    N = len(Ly)
    Nb = int(N/2)+1
    Res = []
    for k in range(Nb):
        ck = f_ck(Ly,k)
        Res.append(ck)
    return Res

def Arrondis(L,Crit):
    Taille = len(L)
    for i in range(Taille):
        c = L[i]
        re = c.real
        im = c.imag
        if abs(re) < Crit:
            re = 0
        if abs(im) < Crit:
            im = 0
        c = complex(re,im)
        L[i] = c

def Amplitudes(Lc,N):
    Taille = len(Lc)
    LA = []
    for i in range(Taille):
        c = Lc[i]
        if i==0:
            A = c / N
        else:
            A = 2*abs(c)/N
        LA.append(A)
    return LA

DFTN = dft(Ly)
Arrondis(DFTN,1e-10)
Amp = Amplitudes(DFTN,N)
print("Amp :",Amp)
Affiche(2,Lf,Amp,'k')

'''
Lf : liste des fréquences du signal échantillonné
Complexité : n²
'''

## Méthode matricielle

import numpy as np
def dft_mat(Ly):
    N = len(Ly)
    S = np.zeros([N,1]) #création d'un array vide N lignes et 1 colonne
    S[:,0] = Ly         #remplissage de la colonne 1 par les valeur de Ly
    Lv = np.zeros([N,1])
    Lv[:,0] = [i for i in range(N)]
    Lh = np.transpose(Lv)
    Mat = np.dot(Lv,Lh)*(-1j*2*pi)/N
    Mat = np.exp(Mat)
    Res = np.dot(Mat,S)
    Res_L = [Res[i,0] for i in range(N)]
    Res_L = Res_L[:int(N/2)+1]
    return Res_L

DFTN_Mat = dft_mat(Ly)
Arrondis(DFTN_Mat,1e-10)
Amp_Mat = Amplitudes(DFTN_Mat,N)
print("Amp_Mat :",Amp_Mat)
Affiche(3,Lf,Amp_Mat,'k')

## Transformée de Fourier rapide

def dft_rec_1(y): # N termes
    N = len(y)
    if N==2:
        y0,y1 = y
        return [y0+y1,y0-y1]
    else:
        Le = [y[i] for i in range(0,N,2)]
        Lo = [y[i] for i in range(1,N,2)]
        E = dft_rec_1(Le)
        O = dft_rec_1(Lo)
        Res = [0]*N
        Ind = N//2 # N/2 devrait fonctionner mais float
        w = exp(-1j*2*pi/N)
        for k in range(Ind):
            Res[k] = E[k] + O[k]*w**k
            Res[k+Ind] = E[k] - O[k]*w**k
        return Res

DFTN_Rec = dft_rec_1(Ly)
Arrondis(DFTN_Rec,1e-10)
DFTN_Rec = DFTN_Rec[:int(N/2)+1]
Amp_Rec = Amplitudes(DFTN_Rec,N)
print("Amp_Rec: ",Amp_Rec)
Affiche(4,Lf,Amp_Rec,'k')

''' Complexité
Auto-appel 2 fois à l'ordre N/2
O(n) à chaque étape
Résultat: n*ln(n)
'''

def dft_rec_2(y): # N/2+1 termes
    N = len(y)
    if N==2:
        y0,y1 = y
        return [y0+y1,y0-y1]
    else:
        Le = [y[i] for i in range(0,N,2)]
        Lo = [y[i] for i in range(1,N,2)]
        E = dft_rec_2(Le)
        O = dft_rec_2(Lo)
        E += [E[i].conjugate() for i in range(len(E)-2,-1,-1)]
        O += [O[i].conjugate() for i in range(len(O)-2,-1,-1)]
        Res = []
        Ind = N//2
        w = exp(-1j*2*pi/N)
        for k in range(Ind+1):
            Val = E[k] + O[k]*w**k
            Res.append(Val)
        return Res

DFTN_Rec = dft_rec_2(Ly)
Arrondis(DFTN_Rec,1e-10)
Amp_Rec = Amplitudes(DFTN_Rec,N)
print(Amp_Rec)
Affiche(5,Lf,Amp_Rec,'k')

''' Complexité
Auto-appel 2 fois à l'ordre N/2
O(n/2) à chaque étape
Résultat: n*ln(n) '''

## Application 1

def f2(t,A,fs):
    ws = 2*pi*fs
    return A*cos(ws*t)**45

N = 2**8
fs = 1
A = 4

def Etude(p,Col):
    fe = (N/p)*fs
    print(Col + " :",fe/2)
    Lt,Lf,Ly = Donnees(N,fe,f2,fs)
    Affiche(6,Lt,Ly,Col)
    DFTN_Rec = dft_rec_2(Ly)
    Arrondis(DFTN_Rec,1e-10)
    Amp_Rec = Amplitudes(DFTN_Rec,N)
    Affiche(7,Lf,Amp_Rec,Col)

p = 5
Col = 'k'
Etude(p,Col)

p = 10
Col = 'g'
Etude(p,Col)

p = 20
Col = 'r'
Etude(p,Col)

'''
On observe un repliement de spectre autour de fe/2
Condition de Shannon:
Pour obtenir la bonne représentation discrète du signal, il est nécessaire que la fréquence d'échantillonnage soit au moins égale à 2*fmax - Autrement dit, Te<Tmax/2 - Au moins 2 points par période
fe>2*fmax
'''

# Remarque: En résolvant l'équation, on obtient:
# p<2Nfs/fmax
fmax = 20
plim = N*fs/(2*fmax)
plim = round(plim,2)
print("Pour fmax=",fmax,", p<",plim)

## Application 2

def f3(t,A,fs):
    ws = 2*pi*fs
    return A*cos(ws*t)**3

def Etude(p,Col):
    fe = (N/p)*fs
    Lt,Lf,Ly = Donnees(N,fe,f3,fs)
    Affiche(8,Lt,Ly,Col)
    DFTN_Rec = dft_rec_2(Ly)
    Arrondis(DFTN_Rec,1e-10)
    Amp_Rec = Amplitudes(DFTN_Rec,N)
    Affiche(9,Lf,Amp_Rec,Col)

N = 2**8
fs = 1
A = 4

p = 1
Col = 'k'
Etude(p,Col)

p = 19.8
Col = 'g'
Etude(p,Col)

p = 19.9
Col = 'r'
Etude(p,Col)

'''
Pics élargis d'amplitude plus faible
Il faut que fs fasse partie de Lf
Autrement dit, que l'on échantillonne le signal sur un multiple de sa période
'''

# Remarque
ws = 2*pi*fs
wmax = 3*ws
fmax =wmax/(2*pi)
plim = N*fs/(2*fmax)
plim = round(plim,2)
print("Pour fmax=",fmax,", p<",plim)

## Pour aller plus loin... Pas proposé dans le sujet
''' Reconstruction du signal'''

def Donnees(N,fe,f,fs,Phi):
    Te = 1/fe
    t0 = 0
    Lt = [t0 + n*Te for n in range(N)]
    Lf = [fe*i/N for i in range(N//2+1)]
    Ly = [f(t,A,fs,Phi) for t in Lt]
    return Lt,Lf,Ly

def f4(t,A,fs,Phi):
    ws = 2*pi*fs
    return A*cos(ws*t+Phi)

N = 16
fs = 1
A = 1
Phi = 0.5
p = 1
fe = (N/p)*fs
Lt,Lf,Ly = Donnees(N,fe,f4,fs,Phi)

from cmath import phase
def Phase(Lc):
    L_Phi = []
    for c in Lc:
        Phi = phase(c)
        L_Phi.append(Phi)
    return L_Phi

DFTN = dft(Ly)
Arrondis(DFTN,1e-10)
Amp = Amplitudes(DFTN,N)
print("Amp :",Amp)

Ph = Phase(DFTN)
print("Ph :",Ph)

def Reconstruction(Lt,La,Lph):
    Lr = []
    for t in Lt:
        Val = 0
        for i in range(N//2+1):
            a = La[i]
            ph = Lph[i]
            Val += a*cos(2*pi*fs*t+ph)
        Lr.append(Val)
    return Lr

def Affiche_Rec(fig,Lx,Ly,Type,Col):
    plt.figure(fig)
    plt.plot(Lx,Ly,Type,Color=Col)
    plt.show()
    plt.pause(0.000001)

p=5
fe = (N/p)*fs
Lt,Lf,Ly = Donnees(N,fe,f4,fs,Phi)
DFTN = dft(Ly)
Arrondis(DFTN,1e-10)
Amp = Amplitudes(DFTN,N)
Ph = Phase(DFTN)
Lyr = Reconstruction(Lt,Amp,Ph)
Affiche_Rec(20,Lt,Ly,'o','k')
Affiche_Rec(20,Lt,Lyr,'--','0.50')

p=10
fe = (N/p)*fs
Lt,Lf,Ly = Donnees(N,fe,f4,fs,Phi)
DFTN = dft(Ly)
Arrondis(DFTN,1e-10)
Amp = Amplitudes(DFTN,N)
Ph = Phase(DFTN)
Lyr = Reconstruction(Lt,Amp,Ph)
Affiche_Rec(21,Lt,Ly,'o','k')
Affiche_Rec(21,Lt,Lyr,'--','0.50')