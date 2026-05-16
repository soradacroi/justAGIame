from game import Game
from random import randrange

env = Game(debug=True)

env.play_step(4)
env.play_step(4)
env.play_step(4)
env.play_step(3)
env.play_step(2)
i = env.play_step(2)
print()
print(env.score)

env.reset(debug=True, goal=[0, 0])

env.play_step(4)
print(env)
