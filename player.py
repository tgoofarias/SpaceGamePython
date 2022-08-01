class Player:
    def __init__(self, position):
        self.playerSprite = ".O"
        self.position = position
        self.life = 3

    def getPosition(self):
        return self.position

    def getLife(self):
        return self.life

    def createPlayer(self, space):
        matrix = space.getMatrix()

        matrix[self.position[0]][self.position[1]] = 1

        space.setMatrix(matrix)

    def movePlayer(self, space, enemy, direction):
        matrix = space.getMatrix()

        if direction == 'a' and self.position[1] > 0:
            matrix[self.position[0]][self.position[1]] = 0
            self.position[1] -= 1
        elif direction == 'd' and self.position[1] < space.coluna - 1:
            matrix[self.position[0]][self.position[1]] = 0
            self.position[1] += 1
        elif direction == 'w' and self.position[0] > 0:
            matrix[self.position[0]][self.position[1]] = 0
            self.position[0] -= 1
        elif direction == 's' and self.position[0] < space.linha - 1:
            matrix[self.position[0]][self.position[1]] = 0
            self.position[0] += 1
        elif direction == 'j':
            self.shoot(direction, enemy)

        matrix[self.position[0]][self.position[1]] = 1

        space.setMatrix(matrix)

    def collision(self):
        self.life -= 1

    def shoot(self, direction, enemy):
        if (direction == 'j'):
            enemyPos = enemy.getPosition()

            if (enemyPos[0] == self.position[0] or enemyPos[1] == self.position[1]):
                enemy.loseLife()
