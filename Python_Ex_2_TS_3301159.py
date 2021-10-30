#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# Applications of Accelerators Lecture
# Python Exercise 2
# Tugce Sirkecioglu 3301159
# October 2021

# Write a python class for a particle, don't forget the init, by giving Z and A. This class should have a method which gives the number of neutron back. Instantiate this class with an example.


# In[27]:


class Nuclide:
    def __init__(self, protonnumber, massnumber):
        self.Z = protonnumber
        self.A = massnumber

    def get_neutronnumber(self):
        print (self.A-self.Z)
        
Ra207 = Nuclide(88, 207)

Ra207.get_neutronnumber()


# In[ ]:




