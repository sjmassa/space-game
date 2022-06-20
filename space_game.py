#!/usr/bin/env python
# coding: utf-8

# ### saving game needs to be done
# ### Room inventory needs to be figured out
# ### Make initial save file/dialog
# ### Create combat system

# In[73]:


# General imports
import sys
import os
import time
import random
import csv
from numpy import arange

# Game imports
from items import backpack
from items import armor
from items import weapon
from items import consumable


# ### Saved Variables

# In[74]:


# General variables
user_name = ''
player_game_state = 0
player_input = 0

# Health
current_health = 50
max_health = 100
medpack_plus = 0
medpack_plusplus = 0

# Energy
current_energy = 50
max_energy = 100
booster_plus = 0
booster_plusplus = 0

# Keys
equip_keys = []

# Equipment Variables
equip_weapon = 'Fists'
equip_armor = 'None'
equip_pack = 'None'

# Inventory variables
inventory = {}
inv_default = 6
inv_max = inv_default + backpack[equip_pack]

# Map
current_map = 'maps\map_start.txt'

help_options = ['help', 'h', '?', 'stat', 'inv', 'map', 'log', 'clear', 'back', 'repeat', 'save', 'exit']


# ### General Funtions

# In[75]:


def clrscr():
    try:
        os.system('cls')
    except Exception:
        pass
    print('\n')
    time.sleep(2)
    return

def skip_line(x):
    line = "\n"
    print(line * x)

def print_text(text, speed):
    if text != 0:
        for letter in text:
            print(letter, end="", flush=True)
            time.sleep(speed)
            
def gen_text(text, speed, sleep, line):
    print_text(text, speed)
    time.sleep(sleep)
    skip_line(line)

def press_continue():
    ckey = input("Press enter to continue:")
    while ckey != "":
        ckey = input("Press enter to continue:")
    print("-----------------------""\n")
    
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


# ### Player choice functions

# In[76]:


def choice_yes_no(dialog, output1, output2, speed, sleep, line):
    if dialog != 0:
        gen_text(dialog, speed, sleep, line)
    #Defines the available choices
    #Starts infinite loop to compare the user input to the available choices
    #Then adds 1 to the house value and exits loop
    x = 1
    while True:
        player_input = input(">>> ").lower().strip()
        time.sleep(1)
        if player_input == 'y' or player_input == 'yes':
            player_input = 'y'
            gen_text(output1, speed, sleep, line)
            return player_input
        elif player_input == 'n' or player_input == 'no':
            player_input = 'n'
            gen_text(output2, speed, sleep, line)
            return player_input
        elif player_input in help_options:
            return_variable = help_commands(player_input)
            if return_variable == 'break':
                break
        elif x < 3:
            print("Not a valid option.")
            x += 1
            continue
        elif x == 3:
            print("Type 'help' for available commands.")
            x = 0
            continue

def choice_two(dialog, option1, option2, output1, output2, speed, sleep, line):
    while True:
        if dialog != 0:
            gen_text(dialog, speed, sleep, line)
        #Prints the different choice options
        if option1 != 0:
            print("1. ", end = "")
            gen_text(option1, speed, sleep, line)
        if option2 != 0:
            print("2. ", end = "")
            gen_text(option2, speed, sleep, line)
        gen_text("3. ...", speed, sleep, line)
        #Defines the available choices
        choice_1 = ['1', 'one', 'first']
        choice_2 = ['2', 'two', 'second']
        choice_3 = ['3', 'three', 'third', '...']
        #Starts infinite loop to compare the user input to the available choices
        #Then adds 1 to the house value and exits loop
        x = 1
        while True:
            player_input = input(">>> ").lower().strip()
            time.sleep(1)
            print("")
            if player_input in choice_1:
                player_input = 1
                gen_text(output1, speed, sleep, line)
                return player_input
            elif player_input in choice_2:
                player_input = 2
                gen_text(output2, speed, sleep, line)
                return player_input
            elif player_input in choice_3:
                help_list()
                continue
                x = 0
            elif player_input in help_options:
                return_variable = help_commands(player_input)
                if return_variable == 'break':
                    break
            elif x < 3:
                print("Not a valid option.")
                x += 1
                continue
            elif x == 3:
                print("Type 'help' for available commands.")
                x = 0
                continue

def choice_four(dialog, option1, option2, option3, option4, output1, output2, output3, output4, speed, sleep, line):
    while True:
        if dialog != 0:
            gen_text(dialog, speed, sleep, line)
        #Prints the different choice options
        if option1 != 0:
            print("1. ", end = "")
            gen_text(option1, speed, sleep, line)
        if option2 != 0:
            print("2. ", end = "")
            gen_text(option2, speed, sleep, line)
        if option3 != 0:
            print("3. ", end = "")
            gen_text(option3, speed, sleep, line)
        if option4 != 0:
            print("4. ", end = "")
            gen_text(option4, speed, sleep, line)
        gen_text("5. ...", speed, sleep, line)
        #Defines the available choices
        choice_1 = ['1', 'one', 'first']
        choice_2 = ['2', 'two', 'second']
        choice_3 = ['3', 'three', 'third']
        choice_4 = ['4', 'four', 'fourth', 'last']
        choice_5 = ['5', 'five', 'fifth', '...']
        #Starts infinite loop to compare the user input to the available choices
        #Then adds 1 to the house value and exits loop
        while True:
            player_input = input(">>> ").lower().strip()
            time.sleep(1)
            print("")
            if player_input in choice_1:
                player_input = 1
                gen_text(output1, speed, sleep, line)
                return player_input
            elif player_input in choice_2:
                player_input = 2
                gen_text(output2, speed, sleep, line)
                return player_input
            elif player_input in choice_3:
                player_input = 3
                gen_text(output3, speed, sleep, line)
                return player_input
            elif ckplayer_inputey in choice_4:
                player_input = 4
                gen_text(output4, speed, sleep, line)
                return player_input
            elif player_input in choice_5:
                help_list()
                continue
                x = 0
            elif player_input in help_options:
                return_variable = help_commands(player_input)
                if return_variable == 'break':
                    break
            elif x < 3:
                print("Not a valid option.")
                x += 1
                continue
            elif x == 3:
                print("Type 'help' for available commands.")
                x = 0
                continue
                
def are_you_sure():
    gen_text("Are you sure? y/n.", .05, 0, 0)
    player_input = input(">>> ").lower().strip()
    time.sleep(1)
    if player_input == 'y' or player_input == 'yes':
        return
    elif player_input == 'n' or player_input == 'no':
        return 'break'


# ### Health Functions

# In[77]:


#Health Version 2
def health():
    if current_health > 75:
        print("Health: Good")
        return
    elif current_health > 50:
        print("Health: Weakened")
        return
    elif current_health > 25:
        print("Health: Very Weak")
        return
    elif current_health > 0:
        print("Health: Critical")
        return

def medpack():
    global current_health
    #Displays Health and Medpack status
    health()
    medpack_num = 0
    for inv_item in list(inventory.keys()):    
        if inv_item == 'Medpack':
            for inv_stack in inventory[inv_item]:
                medpack_num += inv_stack
    print("Medpacks: "+str(medpack_num)+"\n--------------------")
        
    
    #Medpack use loop
    if medpack_num == 0:
        gen_text("You have no medpacks.", .05, .5, 1)
    else:
        player_input = choice_yes_no("Use a medpack? y/n.", 0, 0, 0, .2, 0)
        if player_input == 'y':
            if current_health == max_health:
                print("Your health is already full!")
                return
            current_health += 15+medpack_plus+medpack_plusplus
            inventory_remove('Medpack', 1)
            if current_health > max_health:
                current_health = max_health
            health()
            return
        elif player_input == 'n':
            return


# ### Energy Functions

# In[78]:


#Energy Version 2
def energy():
    global current_energy
    if current_energy > 75:
        print("Energy: High")
        return
    elif current_energy > 50:
        print("Energy: Moderate")
        return
    elif current_energy > 25:
        print("Energy: Low")
        return
    elif current_energy > 0:
        print("Energy: Very Low")
        return

def booster():
    global current_energy
    #Displays Energy and Booster status
    energy()
    booster_num = 0
    for inv_item in list(inventory.keys()):    
        if inv_item == 'Booster':
            for inv_stack in inventory[inv_item]:
                booster_num += inv_stack
    print("Boosters: "+str(booster_num)+"\n--------------------")
        
    
    #Medpack use loop
    if booster_num == 0:
        gen_text("You have no boosters.", .05, .5, 1)
    else:
        player_input = choice_yes_no("Use a booster? y/n.", 0, 0, 0, .2, 0)
        if player_input == 'y':
            if current_energy == max_energy:
                print("Your energy is already full!")
                return
            current_energy += 15+booster_plus+booster_plusplus
            inventory_remove('Booster', 1)
            if current_energy > max_energy:
                current_energy = max_energy
            energy()
            return
        elif player_input == 'n':
            return


# ### Inventory

# In[79]:


def current_inv_num():
    x = 0
    for items, stacks in inventory.items():
        for stack in stacks:
            x += 1
    return x

def inventory_list():
    if len(equip_keys) > 0:
        print(f"Keys: {', '.join(equip_keys)}")
    else:
        print(f"Keys: None")
    current_inv = current_inv_num()
    print(f"Inventory: {current_inv}/{inv_max}")
    print("-----------------------------")
    if current_inv == 0:
        print("Your inventory is empty.")
    else:
        x = 1
        for item, stacks in inventory.items():
            for stack in stacks:
                print(f"{x}. {item} - {stack}")
                x += 1
    print("-----------------------------")
    
def inventory_list_short():
    if len(equip_keys) > 0:
        print(f"Keys: {', '.join(equip_keys)}")
    else:
        print(f"Keys: None")
    current_inv = current_inv_num()
    print(f"Inventory: {current_inv}/{inv_max}")
    print("-----------------------------")


# In[80]:


# Find the item in the dictionaries.
def inventory_find(new_item):
    if new_item in weapon:
        item_dictionary = weapon
        stack_max = 1
    elif new_item in consumable:
        item_dictionary = consumable
        stack_max = consumable[new_item]
    return item_dictionary, stack_max

def inventory_find_player_input(player_input):
    for inv_item in list(inventory.keys()):    
        row = 1
        if row == player_input:
            print(inv_item)
            return inv_item

# Add item to inventory.
def inventory_add(new_item, new_item_amount):
    current_inv = current_inv_num()
    item_dictionary, stack_max = inventory_find(new_item)
    
    # Check for full inventory.
    if item_dictionary[new_item] == 1 and current_inv == inv_max:
        print("Your inventory is full.")
        return new_item_amount
       
    # If item in inventory, increase item stack if possible.
    for inv_item, inv_stacks in inventory.items():    
        stack_index = 0
        if inv_item == new_item:
            for inv_stack in inv_stacks:
                while new_item_amount > 0 and inventory[new_item][stack_index] < stack_max:
                    inventory[new_item][stack_index] += 1
                    new_item_amount -= 1
                stack_index += 1
    
    # Adding item to a new slot.
    while current_inv < inv_max:
        if new_item_amount == 0:
            break
        if new_item not in inventory:
            if new_item_amount > stack_max:
                inventory[new_item] = [stack_max]
                current_inv += 1
                new_item_amount -= stack_max
            elif new_item_amount <= stack_max and new_item_amount > 0:
                inventory[new_item] = [new_item_amount]
                current_inv += 1
                new_item_amount -= new_item_amount  
        if new_item in inventory:
            if new_item_amount > stack_max:
                inventory[new_item] += [stack_max]
                current_inv += 1
                new_item_amount -= stack_max
            elif new_item_amount <= stack_max and new_item_amount > 0:
                inventory[new_item] += [new_item_amount]
                current_inv += 1
                new_item_amount -= new_item_amount            
            
    # Last check.
    if new_item_amount > 0:
        print("Your inventory is full.")
        
    return new_item_amount

# Remove item from inventory.
def inventory_remove(item_name, amount_to_remove):
    for inv_item in list(inventory):    
        stack_index = 0
        if inv_item == item_name:
            for inv_stack in inventory[inv_item]:
                while amount_to_remove > 0 and inventory[item_name][stack_index] > 0:                        
                    inventory[item_name][stack_index] -= 1
                    amount_to_remove -= 1
                    if inventory[item_name][stack_index] == 0 and len(inventory[item_name]) > 1:
                        del inventory[item_name][stack_index]
                    elif inventory[item_name][stack_index] == 0 and len(inventory[item_name]) == 1:
                        del inventory[item_name]
                        break
                stack_index += 1
                
def inventory_sort():
    global inventory
    temp_inventory = {}
    sorted_inventory = sorted(inventory)
    for item in sorted_inventory:
        for value in sorted(inventory[item], reverse=True):
            if item in temp_inventory:
                temp_inventory[item] += [value]
            else:
                temp_inventory[item] = [value]
    inventory = temp_inventory
    
def item_use(item):    
    if item in consumable:
        if item == 'Medpack':
            medpack()
            return
        elif item == 'Booster':
            booster()
            return
        else:
            gen_text("That item has no use here.", .03, 0, 0)
    elif item not in inventory:
        gen_text("You do not have this item.", .03, 0, 0)
        return
    elif item not in consumable:
        gen_text("This item is not usable.", .03, 0, 0)
        return
    
# Allows player to add/remove/sort inventory.
def inventory_manage():
    inventory_list()
    print("Use | Delete | Sort | Back")
    print("-----------------------------")
    x = 1
    while True:
        player_input = input(">>> ")
        player_input = player_input.lower().strip()
        if player_input[:3] == 'use':
            gen_text("Use which item?", .03, 0 ,0)
            while True:
                player_item = ''                
                player_input_item = input(">>> ")
                if player_input in help_options:
                    return_variable = help_commands(player_input)
                    if return_variable == 'break':
                        break
                try:
                    player_input_item = int(player_input_item)
                    inv_item = inventory_find_player_input(player_input_item)
                except ValueError:
                    player_input_item = player_input_item.lower().strip()
                    inv_item = player_input_item.capitalize()
                if inv_item not in inventory:
                    gen_text("You don't have that item.", .03, 0 ,0)
                    continue
                item_use(inv_item)
                break
        elif player_input[:3] == 'del':
            gen_text("Delete which item?", .03, 0 ,0)
            while True:                
                player_input = input(">>> ")
                player_input = player_input.lower().strip()
                try:
                    player_input_item = int(player_input)
                    inv_item = inventory_find_player_input(player_input_item)
                except ValueError:
                    player_input_item = player_input.lower().strip()
                    inv_item = player_input_item.capitalize()
                if inv_item not in inventory:
                    gen_text("You don't have that item.", .03, 0 ,0)
                    continue
                gen_text("How many?", .03, 0 ,0)
                while True:
                    player_input = input(">>> ").lower().strip()
                    if player_input in help_options:
                        return_variable = help_commands(player_input)
                        if return_variable == 'break':
                            break
                    try:
                        player_input_num = int(player_input)
                        break
                    except ValueError:
                        gen_text("Enter a number.", .03, 0 ,0)
                        continue
                        break     
                return_variable = are_you_sure()
                if return_variable == 'break':
                    break
                inventory_remove(inv_item, player_input_num)
                break
        elif player_input[:4] == 'sort':
            inventory_sort()
            inventory_manage()
            return
        elif player_input[:4] == 'back':
            return
        elif player_input in help_options:
            return_variable = help_commands(player_input)
            if return_variable == 'break':
                break
        elif x < 3:
            gen_text("Not a valid option.", .03, 0 ,0)
            x += 1
            continue
        elif x == 3:
            gen_text("Type 'help' for available commands.", .03, 0 ,0)
            x = 0
            continue
        continue
        
# inventory_manage()


# In[81]:


# Make Test Inventory
inventory = {}
inventory['Medpack'] = [1]
inventory['Element'] = [5]
inventory['Booster'] = [2, 3]
# inventory_list()


# ### Equipment and Pack Displays

# In[82]:


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


# ### Map Display

# In[83]:


def map_header():
    print("-----------------------------------------------------------"); time.sleep(.2)
    print(f'{"*: Player": <20} {"!: Enemies": <20} {"?: Items": <20}'); time.sleep(.2)
    print(f'{"H: Health Station": <20} {"C: Comms": <20} {"T: Terminal": <20}'); time.sleep(.2)
    print(f'{"W: Workbench": <20} {"V: Vendor": <20} {"N: NPC": <20}'); time.sleep(.2)
    print(f'{"D: Door New": <20} {"L: Door Locked": <20} {"U: Door Unlocked": <20}'); time.sleep(.2)
    print("-----------------------------------------------------------"); time.sleep(.2)


def display_map():
    map_header()
    with open(current_map) as map:
        for line in map:
            print(line, end='')
            time.sleep(.1)
    print('')
            
# display_map()


# ### Help Options

# In[84]:


def help_list():
    print("---------------------------------------------")
    print("Available player commands:")
    print("help - Lists command options.")
    print("stat - Displays Health, Energy, and Equipment.")
    print("inv - Lists players inventory and equipped items.")
    print("use - Use an item.")
    print("map - Displays the map.")
    print("log - Displays log files.")
    print("clear - Clears screen.")
    print("back - Goes to previes menu if available.")
    print("repeat - Repeats last dialog.")
    print("save - Saves the game.")
    print("exit - Exits the game.")
    print("---------------------------------------------")
    
def status():
    health()
    energy()
    equipment()
    inventory_list_short()
    
def help_commands(player_input):
    if player_input in help_options:
        if player_input == 'help':
            help_list()
        elif player_input == 'stat':
            status()
        elif player_input == 'inv':
            inventory_list()
        elif player_input == 'map':
            display_map()
        elif player_input == 'log':
            pass
        elif player_input == 'repeat':
            return 'break'
        elif player_input == 'clear':
            clrscr()
        elif player_input == 'back':
            return
        elif player_input == 'save':
            save_game_dialog()
        elif player_input == 'exit':
            exit_game()
    return


# ### Saving game  - Incomplete

# In[85]:


def save_game():
    pass

def save_game_dialog():
    while True:
        player_input = input("Create new save 's', or overwrite 'o' existing? ")
        player_input = player_input.lower().strip()
        if player_input == 's' or player_input == 'new' or player_input == 'new save':
            gen_text("Saving...", .1, 1, 1)
            return
        elif player_input == 'o' or player_input == 'overwrite':
            gen_text("Creating new save...", .1, 1, 1)
            return
        continue

# save_game_dialog()


# ### Exiting game

# In[86]:


def exit_game():
    while True:
        player_input = input("Would you like to save before exiting? ")
        player_input = player_input.lower().strip()
        if player_input == 'yes' or player_input == 'y':
            save_game()
            sys.exit()
        elif player_input == 'no' or player_input == 'n':
            gen_text("Existing game...", .05, 0, 0)
            sys.exit()

# exit_game()


# ### Combat

# In[ ]:





# ### Test Game

# In[87]:


player_game_state = 1


# In[88]:


# gen_text("A choose your own adventure:".center(50), .05, 0, 1)
# gen_text("Space Game".center(50), .1, 0, 1)
# gen_text("A Python Production".center(50), .05, 0, 1)
# help_list()
# print("\n")
# press_continue()


# In[89]:


# dialog = "You awaken with a headache."
# option1 = "Stay still and listen."
# option2 = "Explore the room."
# output1 = "All is quiet."
# output2 = """The room is a mess, after picking your way around some fallen shelves,
# something freezes the blood in your veins. You notice a foot sticking out from under one of the overturned shelves."""
# choice_two(dialog, option1, option2, output1, output2, .05, .5, 0)
# print('next')


# In[ ]:




