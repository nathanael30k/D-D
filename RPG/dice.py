# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 22:29:54 2018

@author: Nessim
"""

import numpy as np
from random import randint
import matplotlib.pyplot as plt
    
class distrib:
    
    def __init__(self,min,max):
        self.proba=[0]*(min)+[1/(max-min+1)]*(max-min+1)
        
    def check(self):
        return sum(self.proba)
    
    def __rmul__(self,x):
        index_max = (len(self.proba)-1)*x
        product = [0]*(index_max+1)
        
        for i in range(len(self.proba)):
            product[x*i] = self.proba[i]
        output = distrib(0,index_max)
        output.proba = product
        return output
    
    def bernouilli(self,p1):
        index_max =len(p1.proba)+len(self.proba)-2
        proba1 = np.array(p1.proba)
        proba2 = np.array(self.proba+[0.]*(index_max+1-len(self.proba)))
        index_max =len(proba1)+len(proba2)-4
        output =  np.array([0]*(index_max+1))
        print(proba1[0])
        print(2*proba2)
        print(output.shape)
        print(proba2.shape)
        output = proba1[1]*proba2
        output[0] = proba1[0]
        outputdis = distrib(0,index_max-1)
        outputdis.proba = output
        return outputdis
    
    def bernouilli2(self,other,p1):
        index_max =len(p1.proba)+len(self.proba)-2
        proba1 = np.array(p1.proba)
        proba2 = np.array(self.proba+[0.]*(index_max+1-len(self.proba)))
        proba3 = np.array(other.proba+[0.]*(index_max+1-len(other.proba)))
        index_max =len(proba1)+len(proba2)-4
        output =  np.array([0]*(index_max+1))
        print(proba1[0])
        print(2*proba2)
        print(output.shape)
        print(proba2.shape)
        output = proba1[1]*proba2 + proba1[0]*proba3
        outputdis = distrib(0,index_max-1)
        outputdis.proba = output
        return outputdis
            
    
    def __mul__(self,x):
        index_max = (len(self.proba)-1)*x
        product = [0]*(index_max+1)
        
        for i in range(len(self.proba)):
            product[x*i] = self.proba[i]
        output = distrib(0,index_max)
        output.proba = product
        return output
    
    def __add__(self,other):
        A = self.proba
        B = other.proba
        # A et B sont des distributions de probabilités représentant 2 variables
        #aléatoires INDEPENDENTES a et b
        
        # Cette fonction renvoie la distribution de probabilité de la variable 
        #aléatoire (a+b)
        
        # Valeur max de la somme des variables aléatoires
        index_max = len(A)+len(B)
        
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
        output = distrib(0,index_max-1)
        output.proba = C
        return output
    def roll(self):
        return np.random.choice(len(self.proba),p=self.proba)
    
    
    def show(self):
        plt.figure()
        plt.plot(self.proba)
    


class dice:
    def __init__(self,table):
        self.table = np.array(table)
        
    def __add__(self,other):
        if type(self)==type(other):
            return dice(self.table+other.table)
        return dice(self.table+[other,0,0,0,0,0,0,0])


    def __radd__(self,other):
        if type(self)==type(other):
            return dice(self.table+other.table)
        return dice(self.table+[other,0,0,0,0,0,0,0])
    
    def __mul__(self,x):
        return dice(x*self.table)
    
    def __rmul__(self,x):
        return dice(x*self.table)
    
    def roll(self):
        result = 0
        dice = [1,4,6,8,10,12,20,100]
        for i in range(8):
            for j in range(self.table[i]):
                result += randint(1,dice[i])
        return result
    
    def expected(self):
        expected = self.table[0]
        dice = [1,4,6,8,10,12,20,100]
        for i in range(7):
            expected +=self.table[i+1]*(dice[i+1]+1)/2
        return expected
    
    def dice_distrib(self):
        output = distrib(self.table[0],self.table[0])
        dice = [1,4,6,8,10,12,20,100]
        for i in range(7):
            for j in range(self.table[i+1]):
                output +=distrib(1,dice[i+1])
        return output

d4 = dice([0,1,0,0,0,0,0,0])
d6 = dice([0,0,1,0,0,0,0,0])
d8 = dice([0,0,0,1,0,0,0,0])
d10 = dice([0,0,0,0,1,0,0,0])
d12 = dice([0,0,0,0,0,1,0,0])
d20  = dice([0,0,0,0,0,0,1,0])
d100  = dice([0,0,0,0,0,0,0,1])

#a = d10.dice_distrib().bernouilli(distrib(0,1))
#print(a.show())