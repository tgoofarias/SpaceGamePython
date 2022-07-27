class Player:
    def __init__(self, position):
        self.playerSprite = ".O"
        self.position = position
    
    def createPlayer(self, space):
        matrix = space.getMatrix()

        matrix[self.position[0]][self.position[1]] = 1

        space.setMatrix(matrix)
    
    def movePlayer(self, space, direction):
        matrix = space.getMatrix()

        if direction == '4' and self.position[1] > 0:
            matrix[self.position[0]][self.position[1]] = 0
            self.position[1] -= 1
        elif direction == '6' and self.position[1] < space.coluna - 1:
            matrix[self.position[0]][self.position[1]] = 0
            self.position[1] += 1
        elif direction == '8' and self.position[0] > 0:
            matrix[self.position[0]][self.position[1]] = 0
            self.position[0] -= 1
        elif direction == '2' and self.position[0] < space.linha - 1:
            matrix[self.position[0]][self.position[1]] = 0
            self.position[0] += 1

        matrix[self.position[0]][self.position[1]] = 1

        space.setMatrix(matrix)
            
        
        

