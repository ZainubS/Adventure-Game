import pytest 
import hierarchy as characters
import Inventory
import RedBlackTree as RBT
import application as app

#Zainub Siddiqui
#Purpose - This file will include the testing suite using pytest

#***********************testing character functions************************
@pytest.fixture
def setCharacter():
    object = characters.character("testCharacter", 100, 20)
    return object

def test__characterInit__(setCharacter):
    assert setCharacter._name == "testCharacter"
    assert setCharacter._health == 100
    assert setCharacter._damage == 20

def test_getHealth(setCharacter):
    assert setCharacter.getHealth() == 100

def test_setHealth(setCharacter):
    assert setCharacter.setHealth(10) == True

def test_neg_setHealth(setCharacter):
    assert setCharacter.setHealth(105) == False

def test_gt_setHealth(setCharacter):
    assert setCharacter.setHealth(-1) == False

def test_fight_with_Monster():
    hero = characters.character("Oceanus", 100, 25)
    monster = characters.character("Scylla", 100, 30)
    assert hero.attack(monster, 0) == 2
    assert monster.attack(hero, 0) == 2

def test_fight_with_Trickster():
    hero = characters.character("Oceanus", 100, 25)
    trickster = characters.character("Jellikin", 100, 35)
    assert hero.attack(trickster, 0) == 2
    assert trickster.attack(hero, 0) == 2

def test_defend_with_Monster():
    hero = characters.character("Oceanus", 100, 25)
    monster = characters.character("Scylla", 100, 45)
    assert hero.defend(45) == 0
    assert monster.defend(25) == 0

def test_defend_with_Trickster():
    hero = characters.character("Oceanus", 50, 25)
    trickster = characters.character("Jellikin", 100, 15)
    assert hero.defend(15) == 5
    assert trickster.defend(25) == 0

def test_defend_with_Ally():
    hero = characters.character("Oceanus", 100, 25)
    ally = characters.character("Kelpa", 100, 35)
    assert hero.defend(35) == 0 
    assert ally.defend(25) == 0

#***********************testing hero functions************************
@pytest.fixture
def setHero():
    object = characters.hero()
    return object

def test_getPearls(setHero):
    assert setHero.getPearls() == 6
    
def test_keys_zero(setHero):
    assert setHero.getKeys() == 0

def test__heroInit__(setHero):
    assert setHero._name == "Oceanus"
    assert setHero._health == 100
    assert setHero._damage == 25

def test_decrement_zero(setHero):
    setHero.addItem("Key")
    setHero.addItem("Key")
    assert setHero.decrementKeys() == True

def test_empty_decrement_zero(setHero):
    assert setHero.decrementKeys() == False

def test_addItem(setHero):
    assert setHero.addItem("Knife") == True

def test_restoreHealth(setHero):
    assert setHero.restoreHealth() == f"Health restored to {setHero._health}!"

def test_decrementPearls(setHero):
    setHero.addItem("Pearl")
    setHero.addItem("Pearl")
    assert setHero.decrementPearls() == True

def test_zero_decrementPearls(setHero):
    assert setHero.decrementKeys() == False

#***********************testing merfolk functions************************
@pytest.fixture
def setMerfolk():
    object = characters.merfolk()
    return object

def test__merfolkInit__(setMerfolk):
    assert setMerfolk._name == "Kelpa"
    assert setMerfolk._health == 100
    assert setMerfolk._damage == 0

def test_giveInfo(setMerfolk):
   # assert setMerfolk.giveInfo() == "Welcome, brave adventurer! I am a Kelpa. If you need healing or wish to trade, I am here to assist you."
    assert setMerfolk.giveInfo() == 1
    
def test_healHero(setMerfolk):
    hero = characters.hero()
    hero.addItem("Pearl")
    hero.setHealth(50)
    assert setMerfolk.healHero(hero) == "Kelpa: Your wounds have been tended to. May your journey continue with strength."

def test_atMax_HealHero(setMerfolk):
    hero = characters.hero()
    hero.setHealth(100)
    assert setMerfolk.healHero(hero) == "Kelpa: Your health is already at its peak. There's no need for healing."

def test_sellBox(setMerfolk):
    hero = characters.hero()
    assert setMerfolk.sellBox(hero) == True

def test_retreat(setMerfolk):
    assert setMerfolk.retreat() == "Kelpa: You've chosen violence. We shall depart. \nThe Kelpa retreat to the depths of the ocean.."

#***********************testing SeaSerpent functions************************
@pytest.fixture
def setSerpent():
    object = characters.seaSerpent()
    return object

def test__SerpentInit__(setSerpent):
    assert setSerpent._name == "Scylla"
    assert setSerpent._health == 100
    assert setSerpent._damage == 30

def test_venomousBite_success(setSerpent):
    hero = characters.hero()
    assert setSerpent.venomousBite(hero, 1) == 1

def test_venomousBite_failure(setSerpent):
    hero = characters.hero()
    assert setSerpent.venomousBite(hero, 0) == 0

def test_dropKey(setSerpent):
    setSerpent._health = 0
    assert setSerpent.dropKey() == 1

def test_not_dropKey(setSerpent):
    setSerpent._health = 10
    assert setSerpent.dropKey() == 0
    
def test_constrictEnemy_success(setSerpent):
    hero = characters.hero()
    assert setSerpent.venomousBite(hero, 1) == 1

def test_constrictEnemy_failure(setSerpent):
    hero = characters.hero()
    assert setSerpent.venomousBite(hero, 0) == 0

#***********************testing Jellyfish functions************************
@pytest.fixture
def setJellyfish():
    object = characters.jellyfish()
    return object

def test__jfishInit__(setJellyfish):
    assert setJellyfish._name == "Jellikin"
    assert setJellyfish._health == 100
    assert setJellyfish._damage == 35

def test_stealPearl_Success(setJellyfish):
    hero = characters.hero()
    assert setJellyfish.stealPearl(hero, 1) == True

def test_electricShock_Success(setJellyfish):
    hero = characters.hero()
    assert setJellyfish.electricShock(hero, 1)== 1

def test_electricShock_Failure(setJellyfish):
    hero = characters.hero()
    assert setJellyfish.electricShock(hero, 0)== 0

def test_giveFalseInfo(setJellyfish):
    assert setJellyfish.giveFalseInfo() == "Jellikin: You're chasing after fairy tales, adventurer. There's no lost city in these waters!"
    
#***********************testing Game functions************************
@pytest.fixture
def setGame():
    game = app.Game()
    return game

def test_init_(setGame):
    setGame.__hero = characters.hero()
    setGame.__merfolk = characters.merfolk()
    setGame.__monster = characters.seaSerpent()
    setGame.__trickster = characters.jellyfish()

def test_GameOver(setGame):
    setGame._Game__hero.setHealth(0)
    assert setGame.GameOver() == True

def test_fightOver(setGame):
    setGame._Game__hero.setHealth(0)
    assert setGame.fightOver("Scylla") == True

def test_not_fightOver(setGame):
    setGame._Game__hero.setHealth(100)
    setGame._Game__trickster.setHealth(100)
    assert setGame.fightOver("Jellikin") == False

def test_openTreasure(setGame):
    assert setGame.openTreasureBox() == True
