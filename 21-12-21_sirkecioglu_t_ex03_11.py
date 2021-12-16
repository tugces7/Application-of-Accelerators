#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python
# coding: utf-8

# Applications of Accelerators Lecture
# Python Exercise 3
# Tugce Sirkecioglu 3301159
# December 2021

# Write a python function with the name of "get_rigidity" to calculate the magnetic rigidity and put your code as usual on your GitHUB and provide the link here.

# Data is taken from the Question 5.

class Rigidity:
    def __init__(self,  kineticenergy, restmass, lorentzfactor, chargestate):
        self.ekin = kineticenergy
        self.m0 = restmass
        self.beta = lorentzfactor
        self.Q = chargestate

    def get_rigidity(self):
        print ((((self.ekin/(self.m0*931.5))+1)*self.m0*1.661E-27*self.beta*2.997E8)/(self.Q*1.602E-19))
        
p7TeV = Rigidity(7000000, 1.007276,0.999999991, 1)

p7TeV.get_rigidity()
