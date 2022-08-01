from re import A
import space
import player
import enemy
import GUI

space = space.Space(10, 10)
player = player.Player([5, 5])
enemy = enemy.Enemy()
GUI = GUI.GUI()

space.createMatrix()
player.createPlayer(space)
enemy.createEnemy(space, player)

while True:
    space.createSpace(player, enemy)
    GUI.showHealthBar(player, enemy)
    space.printSpace()

    direction = GUI.directionMenu()

    if direction == 'o':
        break

    player.movePlayer(space, enemy, direction)
    enemy.moveEnemy(space, player)

    if(player.getLife() == 0 or enemy.getLife() == 0):
        space.createSpace(player, enemy)
        GUI.showHealthBar(player, enemy)
        space.printSpace()
        break

if (player.getLife() != 0 and direction != 'o'):
    print('VOCÊ VENCEU')
elif (player.getLife() == 0):
    print('VOCÊ PERDEU!')