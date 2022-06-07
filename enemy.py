#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random


# Space Game Enemies 
# 
# level
# health
# exp
# loot

# In[20]:


player_level = 1
class Enemy():
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.exp = int(level*50*(level/player_level))
        self.loot = {'Element': random.randint(level, level*2)}
    damage_type = []
    description = ''
    
    
class Boss():
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.exp = level*250
    damage_type = []
    attack = []
    description = ''
    # loot = [random.randint(1, 3)]
    
    
#Enemies - Level 1
void_crab = Enemy('Void Crab', random.randint(1, 2))
void_crab.damage_type = ['Bludgeoning']
void_crab.description = ''
energy_slug = Enemy('Energy Slug', random.randint(2, 3))
energy_slug.damage_type = ['Bludgeoning']
energy_slug.description = ''


# print(void_crab.level)
# print(void_crab.name)
# print(void_crab.damage_type)
# print(void_crab.exp)
# print(void_crab.loot)
    


# In[ ]:





# In[ ]:




