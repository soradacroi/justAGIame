from game import Game
import random
import numpy as np

env = Game(num_goal=150)


class Model:
    def __init__(self) -> None:
        weights = [random.randrange(-4, 4) for _ in range(19)]

        self.weights = weights

    def play_move(self, env):
        pass

    def train(self, prev_env: list, env: list, game_state: str):
        pass


model = Model()
for i in range(500):
    prev_env = env.send_board().copy()
    action = model.play_move(env=env)  # TODO: make the Model
    env.play_step(action=action)
    model.train(prev_env, env.send_board(), env.check_game_state())

    if env.check_game_state() != "PLAYING":
        env.reset()

