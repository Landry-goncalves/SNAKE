from jeu.food import Food
import core
from jeu.player import Player

player = Player()
food = Food()

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    print("Setup En marche-----------")


def run():
    #affichage
    player.draw_player(core.screen)
    food.draw_food(core.screen)

    #clavier
    if core.getkeyPress():
        if core.getkeyPressValue() == 1073741906:
            player.change_direction("Z")
        if core.getkeyPressValue() == 1073741905:
            player.change_direction("S")
        if core.getkeyPressValue() == 1073741903:
            player.change_direction("D")
        if core.getkeyPressValue() == 1073741904:
            player.change_direction("Q")




    #mise a jour (deplacement)
    player.move()


if __name__ =='__main__':
    core.main(setup, run)
