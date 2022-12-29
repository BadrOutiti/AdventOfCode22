class ValueDecider:
    def __init__(self, result, enemyValue):
        self._value = None
        self._result = result
        self._enemyValue = enemyValue
        self.set_value()

    def set_value(self):
        '''Set the value to the pick that the player should take: 0 = Siccor, 1 = Rock, 2 = Paper'''
        if self._result == "X":
            if self._enemyValue > 0:
                self._value = self._enemyValue - 1
            else:
                self._value = self._enemyValue + 2

        elif self._result == "Y":
            self._value = self._enemyValue
        elif self._result == "Z":
            if self._enemyValue < 2:
                self._value = self._enemyValue + 1
            else:
                self._value = self._enemyValue - 2

    @property
    def value(self):
        return self._value