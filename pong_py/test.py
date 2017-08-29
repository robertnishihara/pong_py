from pongjs import PongJS
import matplotlib as mpl
import numpy as np
import time
# mpl.use("MacOSX")

import matplotlib.pyplot as plt

game = PongJS()
terminated = False
game.init()
animation = True
#animation = False

x = []
y = []

if animation:
    plt.ion()
    plt.figure()
    plt.show()
    plt.pause(0.01)
step = 0

ns = game.get_state()

while not terminated:
    step += 1

    # if step % 5 == 0:
    #     ipdb.set_trace()

    #ns, r, terminated = game.step(0)

    if ns[0] > 0:
        ACTION = 2
    else:
        ACTION = 1
    #ACTION = np.random.choice([1, 2])
    #ACTION = 0
    ns, r, terminated = game.step(ACTION)

    ###### CHEAT #######
    #game.left_pad.set_position(game.left_pad.x, ns[1])
    ####################

    if animation:
        x.append(game.ball.x)
        y.append(game.ball.y)

        # if ns[0] < 0:
        #     ipdb.set_trace()

        #print(ns[0], ns[1])

        plt.plot([game.right_pad.x, game.left_pad.x],
                [game.right_pad.y, game.left_pad.y], 'o')
        if step % 5 == 0:
            for line in plt.axes().lines:
                line.remove()
            plt.plot(x, y, c='black')
            plt.draw()
            plt.pause(0.01)

print("XXX", step)
