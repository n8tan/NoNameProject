
class ListManager:
    RegressionList = []

    def addToList(self, name):
        entryToAdd = BuildEntry()
        currentRegressionListLength = self.RegressionList.__len__()
        lastEntryPosition = currentRegressionListLength - 1
        #If no entries exist, set first entry as the root
        if currentRegressionListLength == 0:
            entryToAdd.before = "ROOT"
        else:
            #Set current entry's "before" to the name of the previous entry
            entryToAdd.before = self.RegressionList[lastEntryPosition].name
            #Set "next" of the previous entry to point to the current entry
            self.RegressionList[lastEntryPosition].next = name
        entryToAdd.name = name
        entryToAdd.next = "NONE"
        self.RegressionList.append(entryToAdd)

    def printOutList(self):
        for unit in self.RegressionList:
            print("Build before:"+ unit.before + " Build name:" + unit.name + " Build next:" + unit.next)

    def insertIntoList(self, name, position):
        entryToInsert = BuildEntry()
        previousEntryPosition = position - 1

        #Set entry's "before" to name of the previous entry.
        entryToInsert.before = self.RegressionList[previousEntryPosition].name
        #Set previous entry's "next" to current position.
        self.RegressionList[previousEntryPosition].next = name
        #Set next entry's "before" to name of entry to insert
        self.RegressionList[position].before = name

        entryToInsert.name = name
        #Set current entry's "next" to next entry's name
        entryToInsert.next = self.RegressionList[position].name
        self.RegressionList.append(entryToInsert)

class BuildEntry:
    def __init__(self):
        self.before = ""
        self.name = ""
        self.next = ""

print("Starting")
manager = ListManager()
manager.addToList("bob")
manager.addToList("shark")
manager.addToList("Jam")
manager.addToList("Potato")
manager.printOutList()

manager.insertIntoList("couch",2)
print("-------------------")
manager.printOutList()