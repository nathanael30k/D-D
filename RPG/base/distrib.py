# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 23:35:19 2018

@author: Nessim
"""
import numpy as np
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
    