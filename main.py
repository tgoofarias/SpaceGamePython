import space
import player
import GUI

space = space.Space(7, 10)
player = player.Player([5, 5])
GUI = GUI.GUI()

space.createMatrix()
space.printMatrix()
player.createPlayer(space)

while True:
    space.createSpace(player)
    space.printSpace()

    direction = GUI.directionMenu()

    if direction == 'o':
        break

    player.movePlayer(space, direction)