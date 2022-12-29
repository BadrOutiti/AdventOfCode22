class Backpack:
    def __init__(self, comp1, comp2):
        self._comp1 = comp1
        self._comp2 = comp2

    def getSameItemsInComp(self):
        sameItemList = [x for x in self._comp1 if x in self._comp2]
