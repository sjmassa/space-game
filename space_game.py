#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import os
import time
import random
import csv
from numpy import arange
import items
# import combat
# import termcolor

ckey = 0
time_var = 0
user_name = ''


# General Funtions

# In[2]:


def clr_scr():
    os.system('cls')
    print("\n\n")
    time.sleep(2)

def skip_line(x):
    line = "\n"
    print(line * x)

def print_text(x, y):
    if x != 0:
        for letter in x:
            print(letter, end="", flush=True)
            time.sleep(0)
    else:
        if y != 0:
            for letter in y:
                print(letter, end="", flush=True)
                time.sleep(0)

def press_continue():
    ckey = input("Press enter to continue:")
    while ckey != "":
        ckey = input("Press enter to continue:")
    print("-----------------------""\n")

def gen_text(printfast, printslow, sleep, line):
    print_text(printfast, printslow)
    time.sleep(sleep)
    skip_line(line)
    
def saving_checkpoint():
    for x in range (0,4):  
        b = "Saving Checkpoint" + "." * x
        print (b, end="\r")
        time.sleep(1)

def return_checkpoint():
    ckey = input("Press enter load last checkpoint:")
    while ckey != "":
        ckey = input("Press enter load last checkpoint:")
    clr_scr()


# Player choice function

# In[3]:


def choice_4(question, option1, option2, option3, option4, output1, output2, output3, output4, sleep, line):
    gen_text(question, 0, 2, 0)
    #Prints the different choice options
    if option1 != 0:
        print("1. ", end = "")
        gen_text(option1, 0, 0, 0)
    if option2 != 0:
        print("2. ", end = "")
        gen_text(option2, 0, 0, 0)
    if option3 != 0:
        print("3. ", end = "")
        gen_text(option3, 0, 0, 0)
    if option4 != 0:
        print("4. ", end = "")
        gen_text(option4, 0, 0, 0)
    gen_text("5. ...", 0, 0, 0)
    #Defines the available choices
    choice_1 = ['1', 'one', 'first']
    choice_2 = ['2', 'two', 'second']
    choice_3 = ['3', 'three', 'third']
    choice_4 = ['4', 'four', 'fourth', 'last']
    choice_5 = ['5', 'five', 'fifth', '...']
    #Starts infinite loop to compare the user input to the available choices
    #Then adds 1 to the house value and exits loop
    while True:
        global ckey
        ckey = input("> ").lower()
        time.sleep(2)
        print("")
        if ckey in choice_1:
            ckey = 1
            gen_text(output1, 0, sleep, line)
            return ckey
        elif ckey in choice_2:
            ckey = 2
            gen_text(output2, 0, sleep, line)
            return ckey
        elif ckey in choice_3:
            ckey = 3
            gen_text(output3, 0, sleep, line)
            return ckey
        elif ckey in choice_4:
            ckey = 4
            gen_text(output4, 0, sleep, line)
            return ckey
        #If one of the available choices was not a valid input,
        #cycles back through loop
        else:
            print(random.choice(["Not a valid option."]))

def yes_no(question, output1, output2, sleep, line):
    gen_text(question, 0, 1, 0)
    gen_text("1. Yes.", 0, 0, 0)
    gen_text("2. No.", 0, 0, 0)
    gen_text("3. ...", 0, 0, 0)
    #Defines the available choices
    choice_1 = ['1', 'one', 'first', 'yes']
    choice_2 = ['2', 'two', 'second', 'no']
    choice_3 = ['3', 'three', 'third', '...']
    #Starts infinite loop to compare the user input to the available choices
    #Then adds 1 to the house value and exits loop
    while True:
        global ckey
        ckey = input("> ").lower()
        time.sleep(1)
        if ckey in choice_1:
            ckey = 1
            gen_text(output1, 0, sleep, line)
            return ckey
        elif ckey in choice_2:
            ckey = 2
            gen_text(output2, 0, sleep, line)
            return ckey
        elif ckey in choice_3:
            ckey = 3
            gen_text(output2, 0, sleep, line)
            return ckey
        #If one of the available choices was not a valid input,
        #cycles back through loop
        else:
            print(random.choice(["Not valid input."]))

# yes_no("test", 'testout1', 'testout2', 0, 0)


# Health Functions

# In[4]:


#Health Version 2
current_health = 100
max_health = 100

def health():
    global current_health
    if current_health > 75:
        print("Health: Good\n--------------------")
        return
    elif current_health > 50:
        print("Health: Weakened\n--------------------")
        return
    elif current_health > 25:
        print("Health: Very Weak\n--------------------")
        return
    elif current_health > 0:
        print("Health: Critical\n--------------------")
        return

medpack_num = 0
medpack_plus = 0
medpack_plusplus = 0

def medpack():
    global current_health
    global max_health
    global medpack_num
    global medpack_plus
    global medpack_plusplus
    
    #Displays Health and Medpack status
    health()
    print("Medpacks: "+str(medpack_num)+"\n--------------------")
    
    #Medpack use loop
    if medpack_num == 0:
        gen_text("You have no medpacks.", 0, 0, 1)
    else:
        yes_no("Use a medpack?", 0, 0, 0, 0)
        if ckey == 1:
            if current_health == max_health:
                print("Your health is already full!")
                return
            current_health += 15+medpack_plus+medpack_plusplus
            medpack_num -= 1
            if current_health > max_health:
                current_health = max_health
            health()
            print("Medpacks: "+str(medpack_num)+"\n--------------------")
            return


# Energy Functions

# In[5]:


#Energy Version 2
current_energy = 100
max_energy = 100

def energy():
    global current_energy
    if current_energy > 75:
        print("Energy: High\n--------------------")
        return
    elif current_energy > 50:
        print("Energy: Moderate\n--------------------")
        return
    elif current_energy > 25:
        print("Energy: Low\n--------------------")
        return
    elif current_energy > 0:
        print("Energy: Very Low\n--------------------")
        return

booster_num = 2
booster_plus = 0
booster_plusplus = 0

def booster():
    global current_energy
    global max_energy
    global booster_num
    global booster_plus
    global booster_plusplus
    
    #Displays Energy and Booster status
    energy()
    print("Boosters: "+str(booster_num)+"\n--------------------")
    
    #Booster use loop
    if booster_num == 0:
        gen_text("You have no boosters.", 0, 0, 1)
    else:
        yes_no("Use a booster?", 0, 0, 0, 0)
        if ckey == 1:
            if current_energy == max_energy:
                print("Your energy is already full!")
                return
            current_energy += 15+booster_plus+booster_plusplus
            booster_num -= 1
            if current_energy > max_energy:
                current_energy = max_energy
            energy()
            print("Boosters: "+str(booster_num)+"\n--------------------")
            return


# Inventory

# In[19]:


#Inventory
# inventory_dict = {items.medpack.name:1, items.element.name:8, items.booster.name:2, items.pipe.name:1}
inventory_dict = {}

#Keys
equip_keys = []

#Equipment Variables
equip_weapon = items.fists
equip_armor = items.no_armor
equip_pack = items.pack_none

#Inventory variables
inv_default = 6
inv_max = inv_default + equip_pack.slots
current_inv = len(inventory_dict)

#Create inventory CSV from dictionary.
def create_inv_csv():
    file = open('inventory.csv', 'w')
    writer = csv.DictWriter(file, fieldnames=['Item', 'Number'])
    writer.writeheader()
    for key, value in inventory_dict.items():
        writer.writerow({'Item' : key, 'Number': value})
    file.close()

create_inv_csv()


# In[21]:


def open_create_inventory():
    #Open existing inventory.
    old_inv_file = open('inventory.csv', 'r')
    old_inv_read = csv.DictReader(old_inv_file, fieldnames=['Item', 'Number'])
    #Create new inventory file.
    new_inv_file = open('inventory_new.csv', 'w')
    new_inv_write = csv.DictWriter(new_inv_file, fieldnames=['Item', 'Number'])
    return old_inv_file, old_inv_read, new_inv_file, new_inv_write

def close_inventory(file_1, file_2):
    file_1.close()
    file_2.close()

def adding_item(item, new_item_amount):
    global current_inv
    global inv_max
    
    #First test.
    if item.stack == 1 and current_inv == inv_max:
        print("Your inventory is full.")
        return new_item_amount
    
    #Open inventory files.
    old_inv_file, old_inv_read, new_inv_file, new_inv_write = open_create_inventory()
    
    #Start inventory process.
    for row in old_inv_read:
        if row['Item'] != item.name or row['Item'] == item.name and int(row['Number']) == item.stack:
            new_inv_write.writerow(row)
            continue         
        #Item was found and stack not full.
        elif row['Item'] == item.name and int(row['Number']) < item.stack:  
            new_item_amount += int(row['Number'])     
            if new_item_amount >= item.stack:
                new_inv_write.writerow({'Item' : item.name, 'Number' : item.stack})
                new_item_amount -= item.stack    
                continue
            elif new_item_amount < item.stack:
                new_inv_write.writerow({'Item' : item.name, 'Number' : new_item_amount})
                continue
    #After inventory has been copied and any possible stacking done.
    while current_inv < inv_max:
        if new_item_amount == 0:
            break
        if new_item_amount > item.stack:
            new_inv_write.writerow({'Item' : item.name, 'Number' : item.stack})
            current_inv += 1
            new_item_amount -= item.stack
        elif new_item_amount <= item.stack and new_item_amount != 0:
            new_inv_write.writerow({'Item' : item.name, 'Number' : new_item_amount})
            current_inv += 1
            new_item_amount -= new_item_amount    
    #Last check.
    if new_item_amount > 0:
        print("Your inventory is full.")
      
    close_inventory(old_inv_file, new_inv_file)    
    os.remove('inventory.csv')
    os.rename('inventory_new.csv', 'inventory.csv')   
    return new_item_amount
   

print(adding_item(items.booster, 5))


# In[18]:


def create_dict_from_file(file):
    for row in file:
        #Ignore header.
        if row['Item'] == 'Item':
            continue
        else:
            temp_keys += [row['Item']]
            temp_values += [row['Number']]

def create_inv_temp_dict(file):
    #Compile inventory into a dictionary.
    temp_keys = []
    temp_values = []
    temporary_dict = {}    
    n = 0
    #Create key, value lists.
    for row in file:
        #Ignore header.
        if row['Item'] == 'Item':
            continue
        else:
            temp_keys += [row['Item']]
            temp_values += [row['Number']]
    #Create dictioary.
    for i in temp_keys:
        if i not in temporary_dict:
            temporary_dict[temp_keys[n]] = [temp_values[n]]
            n += 1
        elif i in temporary_dict:
            temporary_dict[temp_keys[n]] += [temp_values[n]]
            n += 1
        #Sorts temp_keys list.
    temp_keys.sort() 
    return temp_keys, temporary_dict

def sort_inv_dict():
    #Open files.
    old_inv_file, old_inv_read, new_inv_file, new_inv_write = open_create_inventory()
    #Creates a dictionary from inventory.csv.
    temp_keys, temporary_dict = create_inv_temp_dict(old_inv_read)
    for key in temporary_dict:
        for value in temporary_dict[key]:
            new_inv_write.writerow({'Item' : key, 'Number' : value})
        # if i not in temporary_dict:
        #     new_inv_write.writerow({'Item' : i, 'Number' : item.stack})
        # elif i in temporary_dict:
        #     new_inv_write.writerow({'Item' : item.name, 'Number' : item.stack})
            
    close_inventory(old_inv_file, new_inv_file)    
    os.remove('inventory.csv')
    os.rename('inventory_new.csv', 'inventory.csv')   

sort_inv_dict()
    
    


# In[51]:


diction = ['blah', 'blah', 'item', 'item']
diction_num = [1, 2, 1, 3]
new_dict = {}
n=0
for i in diction:
    if i not in new_dict:
        new_dict[diction[n]] = [diction_num[n]]
        n+=1
    elif i in new_dict:
        print('test')
        new_dict[diction[n]] += [diction_num[n]]
        n+=1
print(new_dict)

for key in new_dict:
    for value in new_dict[key]:
        print(key, value)


# In[8]:


#Display Inventory
def show_inventory():
    global equip_keys
    global inventory_dict
    global inv_default
    global current_inv
    global equip_keys
    print(f"Keys: {', '.join(equip_keys)}")
    print(f"Inventory: {current_inv}/{inv_max}")
    print("-----------------------------")
    empty_bag_var = 0
    num = 1
    for key, value in inventory_dict.items():
        if value > 0:
            print(f"{num}. {key} - x{value}")
            num += 1
            empty_bag_var += 1
    if empty_bag_var == 0:
        print("Your inventory is empty.")
    print("-----------------------------")

#Display Inventory Status
def inv_status():
    global inv_plus
    global inv_plusplus
    global inv_max
    global inventory_dict
    global current_inv
    print(f"Inventory: {current_inv}/{inv_max}\n--------------------")
    
def pack():
    print(f"Pack: {pack_list_keys[1]} + {pack_list_values[1]} Slots")
    print("-----------------------------")

#Equipment Display Funcion
def equipment():
    if equip_pack == items.pack_none:
        print("Pack: "+equip_pack.name)
    else:
        print(f"Pack: {equip_pack.name} + {equip_pack.slots} Slots")
    print(f"Weapon: {equip_weapon.name}, DPS: {equip_weapon.dps}")
    if equip_armor == items.no_armor:
        print("Suit: None")
    else:
        print(f"Suit: {equip_armor.name}, Armor: {equip_armor.armor}")
    print("-----------------------------")

equipment()
show_inventory()


# Psionic Functions

# In[8]:


psionics = ''


# Help List Functions

# In[193]:


def help_list():
    print("---------------------------------------------")
    print("Available player commands:\n")
    print("help - Lists command options.")
    print("stat - Displays Health, Energy, and Inventory Status.")
    print("inv - Lists players inventory and equipped items.")
    print("map - Displays the map.")
    print("log - Displays log files.")
    print("clear - Clears screen.")
    print("---------------------------------------------")
    
def status():
    health()
    energy()
    inv_status()
    # skills()
    
def help_commands(player_input):
    help_options = ['help', 'stat', 'inv', 'skill', 'map', 'clr']
    if player_input in help_options:
        if player_input == 'help':
            help_list()
        elif player_input == 'stat':
            status()
        elif player_input == 'health':
            health()
        elif player_input == 'energy':
            energy()
        elif player_input == 'inv':
            equipment()
            inventory_list()
        elif player_input == 'clr':
            clr_scr()
    return

# help_commands(input())
# status()
# inventory_list()
# help_list()


# Use Items

# In[ ]:





# Test Environment

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Game Start

# In[194]:


choose_your_own = "Choose your own adventure:"
alone_on_mars = "Space Game"
angry_pom = "A Python Production"
gen_text(choose_your_own.center(50), 0, 0, 1)
gen_text(0, alone_on_mars.center(50), 0, 1)
gen_text(angry_pom.center(50), 0, 0, 1)
print("\n")
help_list()
print("\n\n")
press_continue()


# Introduction

# In[195]:


# #clrscr()
# intro = """You are a one of a few new recruits sent to a Mars colony financed
# by United Habitation Group. You've been traveling 7 months, during which
# time you've learned everything you would need to survive there."""
# intro_2 = "At least you hope so...."

# gen_text(intro, 0, 2, 1)
# gen_text(intro_2, 0, 2, 1)
# press_continue()


# Second text

# In[46]:


# landing = "After a day of hectic unpacking, you settle into your room for a much needed rest..."
# start_noise_1 = "*KABOOOOOOM!!!*"
# what_happen = "You jump out of bed! Alarms start to blare and you hear people shouting!"
# start_noise_2 = "*CRASH!*"
# silence = "... ... ..."

# gen_text(landing, 0, 2, 0)
# gen_text(0, start_noise_1, 2, 0)
# gen_text(what_happen, 0, 2, 0)
# gen_text(start_noise_2, 0, 2, 0)
# gen_text(0, silence, 2, 1)
# press_continue()


# Chapter 1 - Awakening<br>
# Checkpoint 1<br>
# First set of choices to leave current room.<br>

# In[47]:


#First checkpoint loop
#clrscr()
saving_checkpoint()
while True:
    gen_text(0, "Chapter 1 - Awakening", 2, 1)
    global ckey
    #First question
    awake = "You awake in darkness with a splitting headache. All is silent..."
    question_1 = "What do you do?"
    option1 = "Try and feel your way around."
    option2 = "Stay still and listen."
    output1 = """You reach your hand up and touch your head, your hand comes away
wet with blood. As you fumble your way around trying to get your bearings, you are
quickly out of breath. The room feels hotter than you remembered. Finally, you touch a
door handle."""
    output2 = """You instinctively lay still, listening. You hear nothing, but you notice the
air is warmer than you remember, and it feel like you can't quite get enough air.
Reaching up to feel your head, your hand comes away wet with blood."""
    gen_text(awake, 0, 2, 0)
    choice_4(question_1, option1, option2, 0, 0, output1, output2, 0, 0, 1, 0)
    print(ckey)
    
    #Option 2 continuation
    option1 = "Get up."
    option2 = "Keep lying still."
    output1 = """Summoning your courage, you start moving. Slowly feeling your way around, 
you eventually find a door handle."""
    output2 = """Fear grips you. What has happened? All different scenarios run through your head, 
none have good outcomes. Every little noise now is loaded with dread possibilities.
How much time has gone by?"""
    if ckey == 2:
        choice_4(question_1, option1, option2, 0, 0, output1, output2, 0, 0, 1, 0)
        
        #Option 2 further continuation
        option1 = "Time for action!"
        option2 = "It's best to just wait for help."
        output1 = """Finally summoning your courage, you start moving. Slowly feeling your way around, 
you eventually find a door handle."""
        output2 = """You pull your knees up to your chest. Someone will come to help, you're sure of it.
You start to feel light headed, and the air is getting even warmer. It's comforting in a strange way.
A sense of calm comes over you; yes...someone will come. Eventually you doze off."""
        print(ckey)
        if ckey == 2:
            choice_4(question_1, option1, option2, 0, 0, output1, output2, 0, 0, 1, 0)
            if ckey == 2:
                gen_text(0, "Game Over", 3, 0)
                return_checkpoint()
            continue
    break


# Chapter - Leaving Safety<br>
# Checkpoint 1<br>
# First set of choices to leave current room.<br>

# In[ ]:




