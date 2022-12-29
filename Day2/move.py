class Move:

    def __init__(self, move):
        self.move = move
        self.value = None
        self.move_value()

    def move_value(self):
        if self.move == "A" or self.move == "X":
            self.value = 0
        if self.move == "B" or self.move == "Y":
            self.value = 1
        if self.move == "C" or self.move == "Z":
            self.value = 2



