from game import Game

env = Game()

while True:
    print(env)
    print(">> iput 1,2,3,4 for up down left right >>", end="")
    action = int(input())
    env.play_step(action)
