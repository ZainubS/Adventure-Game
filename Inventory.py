#Zainub Siddiqui
# Purpose - This file will include the inventory class

class Item():
    def __init__(self, name, count):
        self._name = name
        self._count = count
    def getCount(self):
        return self._count
    def getName(self):
        return self._name
    def decrementItem(self):
        self._count -= 1
    def incrementItem(self):
        self._count += 1
    def display(self):
        print(f"Item: {self._name}")
    def __lt__(self, other):
        return self._name < other._name
    def __ge__(self, other):
        return self._name >= other._name 
    def __eq__(self, other):
        return self._name == other._name
