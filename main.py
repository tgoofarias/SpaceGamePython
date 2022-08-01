import space
import player
import enemy
import GUI

space = space.Space(10, 10)
player = player.Player([5, 5])
enemy = enemy.Enemy()
GUI = GUI.GUI()

space.createMatrix()
space.printMatrix()
player.createPlayer(space)
enemy.createEnemy(space, player)

while True:
    space.createSpace(player, enemy)
    space.printSpace()

    direction = GUI.directionMenu()

    if direction == 'o':
        break

    player.movePlayer(space, enemy, direction)
    enemy.moveEnemy(space, player)
