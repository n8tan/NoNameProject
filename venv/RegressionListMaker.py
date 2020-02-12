
class ListManager:
    RegressionList = []

    def addToList(self, name):
        self.RegressionList.append(name)

    def printOutList(self):
        for name in self.RegressionList:
            print("------------------")
            print("Build name:" + name)
        print("------------------")

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
manager.printOutList()

manager.insertIntoList("couch",2)
manager.printOutList()