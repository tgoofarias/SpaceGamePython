import space
import player

space = space.Space(7, 10)
player = player.Player([5, 5])

space.createMatrix()
space.printMatrix()
player.createPlayer(space)

while True:
    space.createSpace(player)
    space.printSpace()

    direction = input("Direção: ")

    if direction == '-1':
        break

    player.movePlayer(space, direction)