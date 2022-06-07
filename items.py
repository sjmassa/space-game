# Space Game Items
#All items
#Parent class
class Item:
    def __init__(self, name, usable, stack):
        self.name = name
        self.usable = usable
        self.stack = stack
        self.description = ''

#Weapons subclass
class Weapon(Item):
    def __init__(self, name, usable, stack, dps, hands):
        self.dps = dps
        self.hands = 0
        self.damage_type = []
        super().__init__(name, usable, stack)
        
#Armor subclass
class Armor(Item):
    def __init__(self, name, usable, stack, armor):
        self.name = name
        self.armor = armor
        self.description = ""    
        self.damage_resistance = []
        super().__init__(name, usable, stack)

#Backpacks subclass
class Backpack(Item):
    def __init__(self, name, usable, stack, slots):
        self.slots = slots
        super().__init__(name, usable, stack)

#Backpacks
pack_none = Backpack('None', 0, 0, 0)
pack_small = Backpack('Small', 0, 1, 4)
pack_medium = Backpack('Medium', 0, 1, 8)
pack_large = Backpack('Large', 0, 1, 12)

#Weapons
#DPS - 1
fists = Weapon('Fists', 0, 1, 0, 1)
# fists.damage_type = ['Bludgeoning']
#DPS - 2
pipe = Weapon('Pipe', 1, 2, 1, 1)
# pipe.damage_type = ['Bludgeoning']
wrench = Weapon('Wrench', 1, 2, 1, 1)
# wrench.damage_type = ['Bludgeoning']
hammer = Weapon('Hammer', 1, 2, 1, 1)
# hammer.damage_type = ['Bludgeoning']
#DPS - 3
knife = Weapon('Knife', 1, 3, 1, 1)
knife.damage_type = ['Slashing']
#DPS - 5
handgun = Weapon('Handgun', 1, 5, 1, 1)
# handgun.damage_type = ['Impact', 'Piercing']
#DPS - 10
shotgun = Weapon('Shotgun', 1, 10, 2, 1)
# shotgun.damage_type = ['Impact', 'Piercing']
#Lazergun
    
#Starting Armor
no_armor = Armor('None', 0, 0, 1)
#Level 1
durasuit = Armor('Dura-Suit', 0 ,1, 1)
durasuit.description = "A proprietary general-purpose, padded jumpsuit made by United Habitation Group. Flexible, breathable, and tear resistant."
# durasuit.damage_resistance = ['Bludgeoning']
#Level 2
dura_mach2 = Armor("Dura-Suit Mach 2", 0, 2, 1)
dura_mach2.description = "Carbon plate reinforced Dura-Suit, designed for construction and extraction in earth-like environments."
# dura_mach2.damage_resistance = ['Bludgeoning', 'Slashing']
#Level 3
envirosuit = Armor('Enviro-Suit', 0, 3, 1)
envirosuit.description = "A Dura-Suit Mach 2 augmented with nano-fortified technology. Designed for hazardous environments."
# envirosuit.damage_resistance = ['Bludgeoning', 'Slashing', 'Piercing']
#Level 4
exosuit = Armor('Exo-Suit', 0, 4, 1)
exosuit.description = "UHG's most advanced suit. Capable of withstanding extreme outer-Earth environments."
# exosuit.damage_resistance = ['Bludgeoning', 'Slashing', 'Piercing', 'Impact']

#Keys
keycard_basic = ['Keycard Rank 1', 'Keycard Rank 2', 'Keycard Rank 3', 'Keycard Rank 4']
keycard_extra = ['Weapons Locker']
keys = []

#Consumables
medpack = Item('Medpack', 1, 1)
booster = Item('Booster', 1, 3)
element = Item('Element', 1, 10)
bullet_9mm = Item('9mm Rounds', 1, 50)