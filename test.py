# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 01:46:10 2019

@author: Nessim
"""

from dice import distrib

a=distrib([0,1,8])
print(a.proba)
a.show()
d4 = distrib([0,0.25,0.25,0.25,0.25])
d4.show()
d6 = distrib([0,1/6,1/6,1/6,1/6,1/6,1/6])
d6.show()
b = d4+d6 
b.show()