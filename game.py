import random


class GameError(Exception):
    pass


class Game:
    """
    the game class

    ```
    action
    1 : up
    2 : down
    3 : left
    4 : right
    ```
    """

    def __init__(self, debug=False, goal=[2, 2], player=[0, 0]) -> None:
        self._player_pos = [0, 0]
        self._goal_pos = [random.randrange(1, 15), random.randrange(1, 15)]
        if debug is True:
            self._goal_pos = goal
            self._player_pos = player

        if self._player_pos == self._goal_pos:
            raise ZeroDivisionError(
                "tf are you doing bro, why are u putting player and the goal thingy in the same position."
            )

        self.state = [[0 for _ in range(16)] for _ in range(16)]

        self.state[self._player_pos[0]][self._player_pos[1]] = 1
        self.state[self._goal_pos[0]][self._goal_pos[1]] = 2

        self.level = 0
        self._game_state = "PLAYING"
        self.steps = 0
        self.score = 0

    def reset(self, debug=False, goal=[2, 2], player=[0, 0]):
        self.__init__(debug=debug, goal=goal, player=player)

    def check_game_state(self):
        if any(coord < 0 or coord > 15 for coord in self._player_pos):
            self._game_state = "LOST"
        elif self._player_pos == self._goal_pos:
            self._game_state = "WON"
        return self._game_state

    def play_step(self, action):
        """
        Action mapping:
        1 : up, 2 : down, 3 : left, 4 : right
        """
        if self._game_state != "PLAYING":
            board = "[" + "\n".join(" ".join(map(str, row)) for row in self.state) + "]"
            error = f"playing while you have {self._game_state}"
            raise GameError(error)

        prev_pos = self._player_pos.copy()

        if action == 1:
            self._player_pos[1] -= 1
        elif action == 2:
            self._player_pos[1] += 1
        elif action == 3:
            self._player_pos[0] -= 1
        elif action == 4:
            self._player_pos[0] += 1
        self.steps += 1

        status = self.check_game_state()

        if status == "WON":
            self.state[prev_pos[1]][prev_pos[0]] = 0
            self.state[self._player_pos[1]][self._player_pos[0]] = 3
            # print(self.steps, (self._goal_pos[0], self._goal_pos[1]))
            self.score = (self._goal_pos[0] + self._goal_pos[1]) / self.steps

        if status == "PLAYING":
            self.state[prev_pos[1]][prev_pos[0]] = 0
            self.state[self._player_pos[1]][self._player_pos[0]] = 1

        board = "[" + "\n".join(" ".join(map(str, row)) for row in self.state) + "]"

        return board, status

    def __str__(self) -> str:
        return "[" + "\n".join(" ".join(map(str, row)) for row in self.state) + "]"
