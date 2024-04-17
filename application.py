import hierarchy
import random

#Zainub Siddiqui
#This file includes the Game class which will manage the application of the game

class Game():
    def __init__(self):
        self.__hero = hierarchy.hero()
        self.__merfolk = hierarchy.merfolk()
        self.__monster = hierarchy.seaSerpent()
        self.__trickster = hierarchy.jellyfish()
    def introduction(self):
        print("\nWeclome Oceanus! \nYou will embark on a journey as a fearless ocean explorer, \nventuring into the mysterious underwater realm to uncover the lost city of Areadon.")
        print("Encounter sea creatures, fight, and outsmart your way to collecting 5 keys that unlock the secrets of Areadon.")
        print("\nAre you ready to plunge into the depths and discover what lies beneath?")

        while True:
            try:
                choice = int(input("1) Start Adventure \n2) Quit \n>> ")) 
                if (choice == 1):
                    return True
                elif (choice == 2):
                    return False
                else:
                    print("Invalid input - please enter 1 or 2.\n")
            except ValueError:
                print("Invalid input - try again.\n")
        
    def GameOver(self):
        if (self.__hero.getKeys() == 5):
            print("\nHooray, you've obtained 5 keys! You've reached the Lost City of Aredaen and won the game! :)")
            return True
        elif (self.__hero.getHealth() <= 0):
            print("\nUnfortunately, your health has reached zero. You have died, game over! :(")
            return True
        else:
            return False
    
    def fightOver(self, character):
        #print(f"hero health: {self.__hero.getHealth()}, monster health: {self.__monster.getHealth()}, trickster health: {self.__trickster.getHealth()} ")
        if (self.__hero.getHealth() <= 0):
            print("Oceanus: Oh no! I've been defeated by the enemy.")
            return True

        if (self.__monster.getHealth() <= 0 or self.__trickster.getHealth() <= 0):
            if character == "Scylla":
                self.__monster.dropKey()
                self.__hero.addItem("Key")
                print("Oceanus: Victory! I've defeated the sea serpent and retrieved a key!")
                #reset monster
                self.__monster.setHealth(100)
            elif character == "Jellikin":
                print("\nOceanus: The Jellikin is defeated! And it dropped a treasure box. Lucky me!")
                self.openTreasureBox()  
                #reset
                self.__trickster.setHealth(100)
            return True
        return False
        
    def displayStats(self):
        while True:
            try:
                choice = input("\nDisplay Hero Information? (Y/N): ")
                if choice.lower() == 'y':
                    self.__hero.displayStats()
                    break
                elif choice.lower() == 'n':
                    break
            except ValueError:
                print("Invalid input - Please enter 'Y' or 'N'.")

    #randomly encounter sea creature
    def encounter(self):
        character = random.choice([self.__merfolk, self.__monster, self.__trickster])

        if character == self.__merfolk:
            print("\nYou encounter the docile and friendly merfolk, known as Kelpa.")
            self.__merfolk.giveInfo()
            return 1
        
        elif character == self.__monster:
            print("\nYou encounter the monstrous sea serpent, known as Scylla.")
            print("Scylla is a formidable foe, be prepared for a tough battle! Note: sea serpents tend to hide keys beneath their scales..")
            return 2            
        
        elif character == self.__trickster:
            print("\nYou now encounter the cunning jellyfish, known as Jellikin!")
            print("Jellikin can be tricky and might try to steal from you! Fight back and you might stumble across a discovery!")
            return 3
    
    def enounterMerfolk(self):
        print("\nWhat would you like to do:")
        print("1) Request healing assistance")
        print("2) Buy mystery box for 2 pearls")
        print("3) Attack the merfolk")
        print("4) Leave without taking any action")

        while True:
            try:
                choice = int(input(">> ")) #error handling
                if choice in [1,2,3,4]:
                    break
            except ValueError:
                print("Invalid input. Please enter choice (1-4).")
        return choice
    
    def MerfolkChoice(self, choice):
        if choice == 1: #heal hero
            print(self.__merfolk.healHero(self.__hero))
        elif choice == 2: #sell box
            outcome = self.__merfolk.sellBox(self.__hero)
            if (outcome):
                self.openTreasureBox()
        elif choice == 3: #retreat from attack
            print(self.__merfolk.retreat())
        elif choice == 4:
            print("\nKelpa: Farewell, traveler. May the currents guide you safely.")
    
    def encounterSeaSerpent(self):
        choice = 0
        while(choice != 3 and not self.fightOver("Scylla")):
            print("\nWhat would you like to do:")
            print("1) Attack the sea serpent")
            print("2) Defend against the sea serpent's attack")
            print("3) Retreat from the encounter") #if 3, tell hero they will miss out on chance of item

            while True:
                try:
                    choice = int(input(">> ")) #error handling
                    if choice in [1,2,3]:
                        break
                except ValueError:
                    print("Invalid input. Please enter choice (1-3).")
                
            if choice == 1: #attack
                randNum = random.randint(0,1)
                result = self.__hero.attack(self.__monster, randNum) #hero attack

                #monster not dead
                if (result != 0):
                    #randomly select type of attack by sea serpent
                    attacks = ["Venomous Bite", "Constrict"]
                    selectedAttack = random.choice(attacks)
                    if selectedAttack == "Venomous Bite":
                        self.__monster.venomousBite(self.__hero, random.randint(0, 1)) 
                    else:
                        self.__monster.constrictEnemy(self.__hero, random.randint(0,1))
            elif choice == 2: #defend against sea serpent
                self.__hero.defend(self.__monster._damage)
            elif choice == 3: #retreat from attack
                self.__merfolk.retreat()
            elif choice == 4:
                print("Retreating..")

    def encounterJellyfish(self):
        self.__trickster.stealPearl(self.__hero, random.randint(0, 9)) 
        print("\nWhat would you like to do:")
        print("1) Fight Jellikin")
        print("2) Defend against Jellikin's attack")
        print("3) Run Away")
        
        while True:
            try:
                choice = int(input(">> ")) #error handling
                if choice in [1,2,3]:
                    break
            except ValueError:
                print("Invalid input. Please enter choice (1-3).")

        if choice == 1: #attack
            randNum = random.randint(0,1)
            self.__trickster.electricShock(self.__hero, randNum) #monster return attack
            if self.__hero.getHealth() != 0:
                self.__hero.attack(self.__trickster, random.randint(0, 1)) #hero attack
        elif choice == 2: #defend against sea serpent
            self.__hero.defend(self.__trickster._damage)
        elif choice == 3:
            print("Retreating..")
        self.fightOver("Jellikin")
              
    #Open treasure box and append to hero's inventory
    def openTreasureBox(self):
        boxItem = random.choice(["Pearl", "Hook", "Potion", "Knife", "Key"])

        print(f"\nOpening treasure box...You found {boxItem}!")
        print(f"Adding {boxItem} to inventory..")
        self.__hero.addItem(boxItem)
        return True





