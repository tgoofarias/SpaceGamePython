import random

class Enemy:
    def __init__(self):
        self.enemySprite = ".V"
        self.life = 100

    def getPosition(self):
        return self.position

    def getLife(self):
        return self.life

    def createEnemy(self, space, player):
        matrix = space.getMatrix()
        playerPos = player.getPosition()

        while True:
            posx = random.randint(0, 9)
            posy = random.randint(0, 9)

            if (posx != playerPos[0] and posy != playerPos[1]):
                break

        self.position = [posx, posy]
        matrix[posx][posy] = 2

        space.setMatrix(matrix)

    def moveEnemy(self, space, player):
        matrix = space.getMatrix()
        playerPos = player.getPosition()

        posx = random.randint(0, 9)
        posy = random.randint(0, 9)

        if (posx == playerPos[0] and posy == playerPos[1]):
            while True:
                posx = random.randint(0, 9)
                posy = random.randint(0, 9)

                if (posx != playerPos[0] and posy != playerPos[1]):
                    break

            player.collision()

        if (matrix[self.position[0]][self.position[1]] != 1):
            matrix[self.position[0]][self.position[1]] = 0
        matrix[posx][posy] = 2
        self.position = [posx, posy]

        space.setMatrix(matrix)

    def loseLife(self):
        self.life -= 20
