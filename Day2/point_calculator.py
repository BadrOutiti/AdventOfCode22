class pointCalculator:

    def __init__(self):
        self._points = 0


    def checkResult(self, ownMove, enemyMove):
        #Draw
        if(ownMove - enemyMove == 0):
            self._points += 3
        #Win
        elif(ownMove - enemyMove ==  1 or ownMove - enemyMove ==  -2):
            self._points += 6

    def getPointsForMove(self, ownMove):
        self._points += ownMove + 1

    @property
    def points(self):
        return self._points