import Inventory
import RedBlackTree as RBT
import application as app
#Zainub Siddiqui, CS302 - Program 4/5
#Purpose - This file will include the core hierarchy and its methods and members

#base class - common methods and members
class character():
    def __init__(self, name, health, damage):
        self._name = name
        self._health = health
        self._damage = damage  #how much damage can character do?
    def getHealth(self):
        return self._health
    def setHealth(self, amount):
        if amount < 0 or amount > 100:
            return False
        self._health = amount
        return True
    def attack(self, target, success):
        if (self._name == "Oceanus"):
            print(f"\n{self._name} attacks {target._name} with harpoon!")

        if (success == 1):
            #special case for jellikin..
            if (target._name == "Jellikin"):
                print(f"Attack Worked!") 
                target._health = 0 #jellikin dead

            else: #other characters
                target._health -= self._damage
                print(f"Attack Worked! {target._name} takes {self._damage} damage.") 

            #check if alive or dead
            if (target._health <= 0):
                target._health = 0
                print(f"{target._name}'s health: {target._health}")
                print(f"{target._name} is dead!")
                return 0 # target dead
            else:
                print(f"{target._name}'s health: {target._health}")
                return 1 # target still alive
        else:
            print(f"Attack didn't land. {target._name} is unaffected.")
            return 2
        
    def defend(self, damage):
        print(f"\n{self._name} defends against attack!")
        
        reduced_damage = damage - 10
        if (reduced_damage < 0): # ensure that there are no negatives
            reduced_damage = 0
        if (self._health == 100):
            print(f"{self._name} has max health! Defense not needed.")
            return 0
        else:
            self._health += 10
            if self._health > 100:
                self._health = 100
            print(f"{self._name} reduces incoming damage by 10.\n{self._name}'s health: {self._health}")
            return reduced_damage

#hero class - derived from character
class hero(character):
    def __init__(self):
        super().__init__("Oceanus", 100, 25)
       # self.__keys = 0
        self.__inventory = RBT.RBTree()
        
        self.__keys = Inventory.Item("Key", 0)
        self.__hook = Inventory.Item("Hook", 0)
        self.__pearls = Inventory.Item("Pearl", 5)
        self.__harpoon = Inventory.Item("Harpoon", 1)

        #default inventory in red black tree
        self.__inventory.insert(self.__hook)

        #insert 6 pearls as default
        for i in range(6):
            self.__inventory.insert(self.__pearls)
        self.__inventory.insert(self.__harpoon)

    def displayStats(self):
        print(f"\nHero Health: {self._health}")
        print("-------------------Inventory------------------")
      # print(f"Hero Keys: {self.__keys}")
        self.__inventory.display()

        count = self.__inventory.getCount()
        print("Number of items in Tree: ", count)
        print("----------------------------------------------")
        return 1

    def getPearls(self):
        return self.__inventory.getItemCount(self.__pearls)
    def getKeys(self):
        #return self.__keys
        return self.__inventory.getItemCount(self.__keys)
    def decrementKeys(self):
        if (self.__inventory.getItemCount(self.__keys) == 0):
            return False
        self.__inventory.decrementItem(self.__keys)
        return True
    def addItem(self, name): #add to red black tree
        item = Inventory.Item(name, 1)
        self.__inventory.insert(item)
        return True
    def restoreHealth(self):
        self._health = 100
        return f"Health restored to {self._health}!"
    def decrementPearls(self):
        if (self.__inventory.getItemCount(self.__pearls) == 0):
            return False
        self.__inventory.decrementItem(self.__pearls)
        #print(f"Oceanus has {self.__inventory.getItemCount(self.__pearls)} pearls left.")
        return True
    
#ally class - derived from character
class merfolk(character):
    def __init__(self):
        super().__init__("Kelpa", 100, 0)
    def giveInfo(self):
        print("\nKelpa: Welcome, brave adventurer! I am a Kelpa. If you need healing, I am here to assist you.")
        return 1
    def healHero(self, hero): #heal hero 
        if (hero.getHealth() == 100):
            return "Kelpa: Your health is already at its peak. There's no need for healing."
        else:
            hero.restoreHealth()
            return "Kelpa: Your wounds have been tended to. May your journey continue with strength."
    def sellBox(self, hero):
        print()
        if (hero.getPearls() < 2): 
            print("Kelpa: I'm afraid you don't have enough pearls for the mystery box.")
            return False
        else:
          print("Kelpa: Excellent choice! Trading in 2 pearls for a mystery box. Enjoy the surprise!")
          hero.decrementPearls()
          hero.decrementPearls()
          return True
          
    def retreat(self):
        #if hero tries attacking them - retreat
        return "Kelpa: You've chosen violence. We shall depart. \nThe Kelpa retreat to the depths of the ocean.."


#monster class - derived from character
class seaSerpent(character):
    def __init__(self):
        super().__init__("Scylla", 100, 30)
    def venomousBite(self, hero, success):
        print("\nScylla takes a venomous bite at the hero!")
        super().attack(hero, success)
        return success
    def dropKey(self):
        #drops key once dead
        if (self._health == 0):
            print("\nScylla dropped a key!")
            return 1
        return 0
    def constrictEnemy(self, hero, success):
        print("\nScylla attempts to constrict the hero!")
        super().attack(hero, success)
        return success

#trickster class - derived from character
class jellyfish(character):
    def __init__(self):
        #invoke base class constructor
        super().__init__("Jellikin", 100, 35)
    #Jellikin has 10% chance of stealing pearl
    def stealPearl(self, hero, success):
        print("\nWatch out, Jellikin tries to steal a pearl from you!")
        if (hero.getPearls() == 0):
            print("Jellikin: Hero doesn't have any pearls to steal..")
            return False
        else:
            if (success == 1):
                hero.decrementPearls()
                print("Jellikin steals a pearl from you!")
                return True
            else:
                print("Jellikin was unable to steal a pearl from you!")
                return False
    def electricShock(self, hero, success):
        print("\nJellikin attempts to shock you with it's tentacles!")
        super().attack(hero, success)
        return success     
    def giveFalseInfo(self):
        return "Jellikin: You're chasing after fairy tales, adventurer. There's no lost city in these waters!"
