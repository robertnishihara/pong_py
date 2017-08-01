from pongjs import PongJS
import matplotlib as mpl
import time
# mpl.use("MacOSX")

import matplotlib.pyplot as plt

game = PongJS()
terminated = False
state = game.init()
plt.ion()

x = []
y = []

# fig = plt.figure()

# ax = fig.add_subplot(111)
# line1, = ax.plot(x, y, 'r-')
plt.figure()
plt.show()
plt.pause(0.05)
step = 0

while not terminated:
    step += 1
    ns, r, terminated = game.step(0)
    ## CHEAT
    game.left_pad.set_position(game.left_pad.x, ns[1])
    ##
    x.append(ns[0])
    y.append(ns[1]) 
    print(ns[0], ns[1])
    if step % 5 == 0:
        for line in plt.axes().lines:
            line.remove()
        plt.plot(x, y)
        plt.plot(game.left_pad.x, game.left_pad.y, 'o')
        plt.plot(game.right_pad.x, game.right_pad.y, 'o')
        plt.draw()
        plt.pause(0.05)
    # time.sleep(0.01)

# fig = plt.figure()
# plt.plot(x, y)
# plt.show()