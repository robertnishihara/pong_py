from pongjs import PongJS


import gym
env = gym.make("CartPole-v0")
env.action_space.n = 3
env.observation_space


def transform_state(state):
    return state / 500

class PongJSEnv(object):
    def __init__(self):
        self.env = PongJS()
        self.action_space = env.action_space
        self.observation_space = env.observation_space

    def reset(self):
        self.env.init()
        return transform_state(self.env.get_state())

    def step(self, action):
        state, reward, done = self.env.step(action)
        return transform_state(state), 1, done, {}
        #return state, reward, done, {}
