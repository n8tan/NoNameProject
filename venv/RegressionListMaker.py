
class ListManager:
    RegressionList = []

    def addToList(self, name):
        self.RegressionList.append(name)

    def computeMaximumBoxWidth(self):
        longestLength = 0
        for entry in self.RegressionList:
            if longestLength < len(entry):
                longestLength = len(entry)
        return longestLength

    def printOutList(self):
        maxLength = self.computeMaximumBoxWidth()
        prefixTextToAdd = " Build name: "
        maxLength += len(prefixTextToAdd)
        padding = 0
        for name in self.RegressionList:
            print("+" + "-"*maxLength + "+")
            padding = len(name)
            padding = maxLength - padding - len(prefixTextToAdd)
            print("|" + " Build name: " + name + " "*padding + "|")
        print("+" + "-"*maxLength + "+")

    def insertIntoList(self, name, position):
        position -= 1
        self.RegressionList.insert(position,name)

    def removeFromList(self, name):
        self.RegressionList.remove(name)



print("Starting")
manager = ListManager()
manager.addToList("bob")
manager.addToList("shark")
manager.addToList("Jam")
manager.addToList("Potato")
manager.addToList("Crocodile")
manager.printOutList()

manager.insertIntoList("couch",2)
manager.printOutList()