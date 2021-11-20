from enum import Enum
from io import StringIO
from typing import List, Tuple, Dict, NamedTuple
import random
from collections import deque, namedtuple
from functools import reduce


class State(Enum):
    ICE = "I"
    HOLLOW = "H"
    START = "S"
    END = "E"


class Action(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3


Action_Probability = namedtuple("Action_Probability", ["prob", "state", "reward"])
NORMAL_REWARD = -1
FINAL_REWARD = 1

WORST_REWARD = -(2 ** 32)


class Board:
    INVALID_POS = -1

    def _random_board(self, length: int, width: int) -> bool:
        """Randomize the game board, and assign it

        Args:
            length (int): [description]
            width (int): [description]

        Returns:
            bool: valid board created
        """
        board = [
            random.choice([State.HOLLOW, State.ICE]) for i in range(length * width)
        ]
        # board = [State.HOLLOW] * (length * width)
        START = 0
        END = len(board) - 1
        board[0] = State.START
        board[len(board) - 1] = State.END

        # DFS to check if the map is valid
        self.board = board

        def DFS() -> bool:
            pos = START
            explorePosStack = deque()
            Visited: List[bool] = [False] * (self.w * self.l)
            explorePosStack.append(pos)

            while len(explorePosStack) > 0:

                pos = explorePosStack.pop()

                Visited[pos] = True
                for a in range(len(Action)):
                    action = Action(a)
                    newpos = self.move(pos=pos, action=action)
                    # print(
                    #     f"depth:{len(explorePosStack)}..{pos}..{newpos}..{self.board[newpos] == State.END}"
                    # )

                    if newpos == Board.INVALID_POS or Visited[newpos]:
                        continue
                    elif self.check_die(pos=newpos):
                        # print(f"Die at {newpos}")
                        continue
                    elif self.check_win(pos=newpos):
                        # print(f"Win at {newpos}")
                        return True
                    else:
                        explorePosStack.append(newpos)
                pass
            if pos == END:
                return True
            else:
                return False

        return DFS()

    def check_win(self, pos: int) -> bool:
        if pos >= 0 and pos < len(self.board):
            return self.board[pos] == State.END
        else:
            return False

    def check_die(self, pos: int) -> bool:
        if pos >= 0 and pos < len(self.board):
            return self.board[pos] == State.HOLLOW
        else:
            return False

    def _convert_pos_row_column(self, pos: int) -> Tuple[int, int]:
        return (int(pos / self.w), int(pos % self.w))

    def move(self, pos: int, action: Action) -> int:
        row, col = self._convert_pos_row_column(pos)
        if action == Action.LEFT:
            col -= 1
        elif action == Action.UP:
            row -= 1
        elif action == Action.RIGHT:
            col += 1
        elif action == Action.DOWN:
            row += 1
        if row < 0 or row >= self.l:
            return Board.INVALID_POS
        if col < 0 or col >= self.w:
            return Board.INVALID_POS
        return row * self.w + col

    def i_move(self, action: Action) -> None:
        newpos = self.move(pos=self.pos, action=action)
        if newpos != Board.INVALID_POS:
            self.pos = newpos

    def __init__(self, length: int, width: int) -> None:
        self.l = length
        self.w = width
        self.pos = 0
        gen_ok = False
        cnt = 0

        while not gen_ok and cnt < 1000:
            print(f"Generate board {cnt}")
            gen_ok = self._random_board(length=length, width=width)
            cnt += 1
            # self.render()

    def render(self) -> None:
        graph: StringIO = StringIO()
        for r in range(self.l):
            for c in range(self.w):
                pos = r * self.w + c
                if pos == self.pos:
                    graph.write(f"({self.board[pos].value})")
                else:
                    graph.write(f" {self.board[pos].value} ")
            graph.write("\n")
        print(graph.getvalue())

    def populate_transition_probaility(self, deterministic: bool) -> None:
        """Populate probability and reward for each state
        if deterministic = True, probability = 1 for each action to other state
        """
        self.Prob: List[Dict] = [None] * len(self.board)
        for pos in range(len(self.board)):
            self.Prob[pos] = {}
            for a in range(len(Action)):
                action = Action(a)
                self.Prob[pos][action] = []

                def move_prob_action(prob: float, prob_action: Action):
                    if self.board[pos] == State.END or self.board[pos] == State.HOLLOW:
                        newpos = pos
                    else:
                        newpos = self.move(pos=pos, action=prob_action)

                    if newpos == Board.INVALID_POS:
                        self.Prob[pos][action].append(
                            Action_Probability(
                                prob=prob, state=pos, reward=NORMAL_REWARD
                            )
                        )
                    elif self.board[newpos] == State.HOLLOW:
                        self.Prob[pos][action].append(
                            Action_Probability(
                                prob=prob, state=newpos, reward=WORST_REWARD
                            )
                        )
                    elif self.board[newpos] == State.ICE:
                        self.Prob[pos][action].append(
                            Action_Probability(
                                prob=prob, state=newpos, reward=NORMAL_REWARD
                            )
                        )
                    elif self.board[newpos] == State.END:
                        self.Prob[pos][action].append(
                            Action_Probability(
                                prob=prob, state=newpos, reward=FINAL_REWARD
                            )
                        )

                def find_probability(action: Action, prob_action: Action) -> float:
                    if action == prob_action:
                        return 0.5
                    else:
                        return 0.5 / (len(Action) - 1)

                if deterministic:
                    move_prob_action(prob=1, prob_action=action)
                else:
                    for pa in range(len(Action)):
                        prob_action = Action(pa)
                        prob = find_probability(action=action, prob_action=prob_action)
                        move_prob_action(prob=prob, prob_action=prob_action)
        pass
