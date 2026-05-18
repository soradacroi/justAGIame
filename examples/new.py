from game import Game

env = Game()
print(env, "\n")
env.play_step(4)
print(env, "\n")
env.reset()
print(env)
print("\n----------\n")
env.play_step(4)
print(env, "\n")
env.reset()
print(env)
print("\n----------\n")
