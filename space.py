class Space:
    def __init__(self, linha, coluna):
        self.spaceSprite = "_|"
        self.linha = linha
        self.coluna = coluna
        self.matrix = []
        self.space = []
    
    def getSpaceSprite(self):
        return self.spaceSprite

    def getMatrix(self):
        return self.matrix

    def setMatrix(self, matrix):
        self.matrix = matrix

    def createMatrix(self):
        for c in range(self.linha):
            self.matrix.append([])
            for i in range(self.coluna):
                self.matrix[c].append(0)

    def printMatrix(self):
        for c in range(self.linha):
            print(self.matrix[c])

    def createSpace(self, player, enemy):
        self.space = self.matrix
        for c in range(self.linha):
            for i in range(self.coluna):
                if self.matrix[c][i] == 0:
                    self.space[c][i] = self.spaceSprite
                elif self.matrix[c][i] == 1:
                    self.space[c][i] = player.playerSprite
                elif self.matrix[c][i] == 2:
                    self.space[c][i] = enemy.enemySprite

    def printSpace(self):
        for c in range(self.linha):
            for i in range(self.coluna):
                print(self.space[c][i], end="   ")
            print("\n")
