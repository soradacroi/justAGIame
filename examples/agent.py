import random
from game import Game

q_table = {}

learning_rate = 0.1
discount_factor = 0.9
epsilon = 1.0
epsilon_decay = 0.995
min_epsilon = 0.05
episodes = 1500


def get_state(env):
    dx = env._goal_pos[0] - env._player_pos[0]
    dy = env._goal_pos[1] - env._player_pos[1]
    return (dx, dy)


def get_q_values(state):
    if state not in q_table:
        q_table[state] = {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0}
    return q_table[state]


print("Training")

for episode in range(episodes):
    env = Game()
    state = get_state(env)
    done = False

    while not done:
        q_values = get_q_values(state)

        if random.uniform(0, 1) < epsilon:
            action = random.choice([1, 2, 3, 4])
        else:
            action = max(q_values, key=q_values.get)

        _, status = env.play_step(action)
        next_state = get_state(env)

        if status == "WON":
            reward = 100
            done = True
        elif status == "LOST":
            reward = -100
            done = True
        else:
            reward = -1

        next_q_values = get_q_values(next_state)
        max_future_q = max(next_q_values.values()) if not done else 0

        current_q = q_values[action]
        new_q = current_q + learning_rate * (
            reward + discount_factor * max_future_q - current_q
        )

        q_table[state][action] = new_q

        state = next_state

    epsilon = max(min_epsilon, epsilon * epsilon_decay)

    if (episode + 1) % 500 == 0:
        print(f"game {episode + 1} epsilon  {epsilon:.2f}")

print("Training Complete\n")

print()
env = Game()
env.reset(debug=True, goal=[10, 10], player=[2, 2])
state = get_state(env)
done = False
steps = 0


while not done and steps < 50:
    q_values = get_q_values(state)
    action = max(q_values, key=q_values.get)

    board, status = env.play_step(action)

    state = get_state(env)
    steps += 1

    if status == "WON":
        print(f"\nWON - {steps} steps")
        done = True
    elif status == "LOST":
        print("\nLOST")
        done = True

print(env.showscore())

games_won = 0
games_lost = 0
game_scores = []
more_steps = 0
for _ in range(1000):
    env = Game()
    env.reset()
    state = get_state(env)
    done = False
    steps = 0
    while not done and steps < 100:
        steps += 1
        q_values = get_q_values(state)
        action = max(q_values, key=q_values.get)

        __, status = env.play_step(action)

        state = get_state(env)

        if status == "WON":
            done = True
            games_won += 1
        elif status == "LOST":
            done = True
            games_lost += 1
    if steps >= 33:
        more_steps += 1
    game_scores.append(env.showscore())

print(games_won, games_lost, more_steps)
print(game_scores)
n = 0
for i in game_scores:
    if i == 0.0:
        n += 1
print(n)
