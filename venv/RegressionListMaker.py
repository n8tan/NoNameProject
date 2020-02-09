#ROOT will indicate the first as well as starting position of the queue.

class ListManager:
    RegressionList = []

    def addToList(self, name):
        entryToAdd = BuildEntry()
        currentRegressionListLength = self.RegressionList.__len__()
        if currentRegressionListLength == 0:
            entryToAdd.before = 0
            entryToAdd.name = name
            entryToAdd.next = 1
        else:
            entryToAdd.before = currentRegressionListLength
            entryToAdd.name = name
            entryToAdd.next = currentRegressionListLength + 1
        self.RegressionList.append(entryToAdd)

    def printOutList(self):
        for unit in self.RegressionList:
            print(unit.before)
            print(unit.name)
            print(unit.next)

class BuildEntry:
    def __init__(self):
        self.before = 0
        self.name = ""
        self.next = 0

print("Starting")
manager = ListManager()
manager.addToList("bob")
manager.addToList("shark")
manager.addToList("Jam")
manager.printOutList()