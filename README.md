# Oceanus: The Underwater Adventure Game

**Author:** Zainub Siddiqui  
**Course:** CS302 – Program 4/5  

---

## Overview
*Oceanus: The Underwater Adventure* is a **text-based RPG** where you play as **Oceanus**, a fearless ocean explorer. Venture into the mysterious underwater world to uncover the lost city of **Areadon**. Encounter sea creatures, collect keys, fight monsters, and manage your inventory to survive the depths!

---

## Objective
- Collect **5 keys** to unlock the **Lost City of Areadon**.  
- Survive battles with monsters and tricksters.  
- Strategically manage health, pearls, and inventory items.

---

## Features
- **Random Encounters**: Meet allies, monsters, and tricksters.  
  - **Merfolk (Kelpa)** – heal or buy mystery boxes.  
  - **Sea Serpent (Scylla)** – formidable monster guarding keys.  
  - **Jellyfish (Jellikin)** – tricky enemy that can steal pearls and attack.  
- **Combat System**:
  - Turn-based attacks and defenses.
  - Enemy-specific attacks (Venomous Bite, Constrict, Electric Shock).  
  - Success of attacks depends on random chance.  
- **Inventory Management**:
  - Items stored using a **Red-Black Tree** for efficient management.
  - Items include **Pearls, Keys, Hooks, Harpoons, Potions, and more**.
  - Supports adding, removing, and counting duplicates.  
- **Treasure Boxes**: Random rewards when interacting with certain characters.  
- **Hero Stats**: Track health, inventory, and collected keys.  
- **Win/Loss Conditions**:
  - **Win**: Collect all 5 keys.  
  - **Lose**: Hero health drops to zero.

---

## Getting Started

### Requirements
- Python 
- `pytest` (for running tests)

### Files
- `main.py` – Main game loop  
- `application.py` – Game mechanics and encounter handling  
- `hierarchy.py` – Characters and their abilities  
- `inventory.py` – Item class for inventory  
- `RedBlackTree.py` – Red-Black Tree implementation for inventory  
- `test_hierarchy.py` – Unit tests for characters, inventory, and game

### Running the Game
1. Open a terminal in the project directory.
2. Run the main game file:
   ```bash
   python main.py
