import random

class Enemy:
    def __init__(self):
        self.enemySprite = ".V"

    def createEnemy(self, space, player):
        matrix = space.getMatrix()
        playerPos = player.getPosition()

        while True:
            posx = random.randint(0, 9)
            posy = random.randint(0, 9)

            if (posx != playerPos[0] and posy != playerPos[1]):
                break
        
        matrix[posx][posy] = 2

        space.setMatrix(matrix)

