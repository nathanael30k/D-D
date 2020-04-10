# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 22:29:54 2018

@author: Nessim
"""

import numpy as np
from random import randint
import matplotlib.pyplot as plt

# Class
    
class distrib:

    # La classe distrib représente une distribution de probabilité sur les 
    # entiers naturels.
    #
    # Attributs:
    # - proba: tableau des probabilités associés à chaque nombre entier à partir 
    #   de 0.
    #
    # Méthodes:
    # - constructeur prenant en argument le tableaux de probabilités.
    # - redéfinition de la multiplication par un scalaire et entre distributions.
    # - redéfinition de l'addition par un scalaire et entre distributions.
    # - check(): retourne la somme des probabilités; doit etre quasi égal à 1.
    # - max(): renvoie la valeur maximale prise par la variable aléatoire et 
    #   supprime les zeros inutiles en fin de tableau.
    # - inf(x): renvoie la probabilité d'obtenir un score inférieur à x (voir 
    #   commentaire de la fonction pour l'argument facultatif)
    # - sup(x): renvoie la probabilité d'obtenir un score supérieur à x (voir 
    #   commentaire de la fonction pour l'argument facultatif)
    # - expected(): renvoie l'espérence de la variable aléatoire.
    # - roll(): renvoie le résultat du lancer
    # - show(): montre le graphique de la distibution de probabilité
    # - check(): retourne la somme des probabilités; doit etre quasi égal à 1.
    
    def __init__(self,proba):
        self.proba = proba       

    def __mul__(self,x):

        if type(x)== int:
            # la multiplication par un entier x correspond à multiplier le 
            #résultat du tirage par x
            
            #initialisation du tableau de proba final
            index_max = (len(self.proba)-1)*x
            output = [0.]*(index_max+1)
            
            for i in range(len(self.proba)):
                output[x*i] = self.proba[i]

            return distrib(output)
        
        if type(x)==type(self):
            
            proba1 = self.proba
            proba2 = x.proba
            
            #initialisation du tableau de proba final
            index_max = (len(proba1)-1)*(len(proba2)-1)
            output = np.array([0.]*(index_max+1))
            
            for i in range(len(proba1)):
                probatemp = (i*x).proba
                probatemp.extend([0.] * (index_max+1 - len(probatemp)))
                output += float(proba1[i])*np.array(probatemp)
            return distrib(list(output))

    def __rmul__(self,x):
        #commutativité du produit
        return self.__mul__(x)     
    
    
    def __add__(self,other):
        
        if type(other)==type(self):
            A = self.proba
            B = other.proba
            # A et B sont des distributions de probabilités représentant 2 variables
            #aléatoires INDEPENDENTES a et b
            
            # Cette fonction renvoie la distribution de probabilité de la variable 
            #aléatoire (a+b)
            
            # Valeur max de la somme des variables aléatoires
            index_max = (len(A)-1)+(len(B)-1)
            
            # Initialisation du tableau de la distribution finale
            
            C = [0]*(index_max+1)
    
            # Extension des tableaux des distributions jusqu'à la taille de la 
            #distribution finale
            A += [0]*(-len(A)+index_max+1)
            B += [0]*(-len(B)+index_max+1)
    
            # Computation
            #Balayage des valeurs de C
            for k in range(index_max+1):
                # Balayage des valeurs de A et B
                for i in range(index_max+1):
                    C[k] += A[i] * B[k-i]          
            #Affiche la somme des probabilités (doit etre égale à 1)
            output = distrib(C)
            return output
    
        if type(other)== int:
            return self + other*bernouilli(1)
        
    def __radd__(self,x):
        #commutativité du produit
        return self.__add__(x)
    
    
    def max(self):
        while self.proba[len(self.proba)-1]==0:
            del self.proba[len(self.proba)-1]
        return len(self.proba)-1
    
    
    def inf(self,x,equal=False):
        #proba de faire un score inferieur à x (ou égale si equal = True)
        output = 0
        for i in range(x):
            output += self.proba[i]
        if equal:
            output += self.proba[x]
        return output
            
    def sup(self, x, equal = True):
        #proba de faire un score supérieur à x (ou égale si equal = True)
        a= not(equal)
        return 1-self.inf(x,a)
    
    def expected(self):
        expected = 0
        for i in range(len(self.proba)):
            expected +=float(i)*self.proba[i]
        return expected
    
    def roll(self):
        if 1-self.check()>0.01:
            self.proba[0]+=1-self.check()
            return np.random.choice(len(self.proba),p=self.proba)
        return 666
    
    def show(self):
        plt.figure()
        plt.plot(self.proba)
    
    def check(self):
        return sum(self.proba)
        
        

class dice:
    
    def __init__(self,table):
        self.table = np.array(table)
        
    def __add__(self,other):
        if type(self)==type(other):
            return dice(self.table+other.table)
        return dice(self.table+[other,0,0,0,0,0,0,0,0,0])


    def __radd__(self,other):
        if type(self)==type(other):
            return dice(self.table+other.table)
        return dice(self.table+[other,0,0,0,0,0,0,0,0,0])
    
    def __mul__(self,x):
        return dice(x*self.table)
    
    def __rmul__(self,x):
        return dice(x*self.table)
    
    def __str__(self):
        name = ""
        dice = [0,"d2","d3","d4","d6","d8","d10","d12","d20","d100"]
        for i in range(9):
            if self.table[i+1] != 0:
                name += str(self.table[i+1])+dice[i+1]+"+"
        if self.table[0]==0:
            name = name[:-1]
        else:
            name += str(self.table[0])
        return name
        
    
    def roll(self):
        result = 0
        dice = [1,2,3,4,6,8,10,12,20,100]
        for i in range(10):
            for j in range(self.table[i]):
                result += randint(1,dice[i])
        return result
    
    def expected(self):
        expected = self.table[0]
        dice = [1,2,3,4,6,8,10,12,20,100]
        for i in range(9):
            expected +=self.table[i+1]*(dice[i+1]+1)/2
        return expected
    
    def max(self):
        return self.dice_distrib().max()
        
    
    def dice_distrib(self):
        output = self.table[0]*distrib([0,1])
        dice = [1,2,3,4,6,8,10,12,20,100]
        for i in range(9):
            for j in range(self.table[i+1]):
                output =output +distrib([0]+[1/dice[i+1]]*dice[i+1])
        return output
    
    def inf(self,x,equal=False):
        #proba de faire un score inferieur à x (ou égale si equal = True)
        return self.dice_distrib().inf(x,equal)
            
    def sup(self, x, equal = True):
        #proba de faire un score supérieur à x (ou égale si equal = True)
        return self.dice_distrib().sup(x,equal)

# Methods

def bernouilli(p):
    return distrib([1-p,p])

# Base de données
d2 = dice([0,1,0,0,0,0,0,0,0,0])
d3 = dice([0,0,1,0,0,0,0,0,0,0])
d4 = dice([0,0,0,1,0,0,0,0,0,0])
d6 = dice([0,0,0,0,1,0,0,0,0,0])
d8 = dice([0,0,0,0,0,1,0,0,0,0])
d10 = dice([0,0,0,0,0,0,1,0,0,0])
d12 = dice([0,0,0,0,0,0,0,1,0,0])
d20  = dice([0,0,0,0,0,0,0,0,1,0])
d100  = dice([0,0,0,0,0,0,0,0,0,1])