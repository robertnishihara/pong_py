import numpy as np
from ball import Ball
from paddle import Paddle

class PongJS():
    # MDP to 
    def __init__():
        self.width = 640
        self.height = 480
        self.wall_width = 12
        self.dt = 0.005 # seconds
        self.left_pad = Paddle(0, self)
        self.right_pad = Paddle(1, self)
        self.ball = Ball(self)

    def step(self, action):
        # do logic for self
        self.left_pad.step(action, self.ball)
        self.right_pad.ai_step(self.ball)
        self.ball.update()
        return state, r, term

    def reward(self):
        return self.ball.left > self.width

    def reset(self):
        pass

