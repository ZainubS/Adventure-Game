import os
import hierarchy as characters
import application as app
#Zainub Siddiqui, CS302 - Program 4/5
#Purpose - This will include the main file of the game

def main():
    
    game = app.Game()
    flag = game.introduction()

    while (flag == True and not game.GameOver()):

        character = game.encounter()
        #encounter ally - merfolk
        if (character == 1):
            choice = game.enounterMerfolk()
            game.MerfolkChoice(choice)
        #encounter monster - sea serpent
        elif (character == 2):
            choice = game.encounterSeaSerpent()
        #encounter trickster - jellyfish
        else:
            choice = game.encounterJellyfish()
        game.displayStats()

if __name__ == "__main__":
    main()