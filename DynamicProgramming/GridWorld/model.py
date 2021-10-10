from __future__ import annotations
from collections import namedtuple
from enum import Enum
from typing import List, Dict, Set
from typing_extensions import TypeAlias
from .loghelper import get_logger, logging

logger = get_logger(__name__, logging.INFO)


"""
    A simple maze game to demonstrate Bellman equation
    Code referenced from https://towardsdatascience.com/reinforcement-learning-dynamic-programming-2b89da6ea1b
"""


State = namedtuple("State", ["row", "column"])
Reward: TypeAlias = float


class Action(Enum):
    UP = "U"
    DOWN = "D"
    RIGHT = "R"
    LEFT = "L"

    def __str__(self):
        return self.value


Actions: TypeAlias = Dict[State, List[Action]]
Rewards: TypeAlias = Dict[State, Reward]
Policy: TypeAlias = Dict[State, Action]
Values: TypeAlias = Dict[State, Reward]

NO_REWARD: Rewards = 0.0


class Grid:
    def __init__(self, width, height, start: State):
        self.width: int = width
        self.height: int = height
        self.start: State = start
        self._state: State = None

    def set(self, rewards: Rewards, actions: Actions) -> None:
        self.rewards: Rewards = rewards
        self.actions: Actions = actions

    @property
    def state(self) -> State:
        return self._state

    @state.setter
    def state(self, value: State) -> None:
        self._state = value

    def is_terminal(self, s: State) -> bool:
        """
        it is a terminal if not in possible actions
        """
        return s not in self.actions

    def game_over(self) -> bool:
        """
        Game over if state of itself is not in possible actions
        """
        return self.state not in self.actions

    def move(self, action: Action) -> Reward:
        """
        check if action is possible, then moves in that direction
        """
        (row, column) = self.state
        if action in self.actions[self.state]:
            if action == Action.UP:
                row -= 1
            elif action == Action.DOWN:
                row += 1
            elif action == Action.RIGHT:
                column += 1
            elif action == Action.LEFT:
                column -= 1
        self.state = State(row=row, column=column)
        return self.rewards.get(self.state, NO_REWARD)

    def all_states(self) -> Set[State]:
        """
        return set of all possible states
        """
        return set(list(self.rewards.keys()) + list(self.actions.keys()))

    @classmethod
    def get_sample_grid(cls) -> Grid:
        """
        return a sample grid
        Note: u should develop your own graph algorithm
        to explore construct a grid from a 2-dimension array
        """
        sample_grid = Grid(width=3, height=4, start=State(2, 0))
        rewards: Rewards = {State(0, 3): 1, State(1, 3): -1}
        actions: Actions = {
            State(0, 0): [Action.DOWN, Action.RIGHT],
            State(0, 1): [Action.LEFT, Action.RIGHT],
            State(0, 2): [Action.LEFT, Action.DOWN, Action.RIGHT],
            State(1, 0): [Action.UP, Action.DOWN],
            State(1, 2): [Action.UP, Action.DOWN, Action.RIGHT],
            State(2, 0): [Action.UP, Action.RIGHT],
            State(2, 1): [Action.LEFT, Action.RIGHT],
            State(2, 2): [Action.LEFT, Action.RIGHT, Action.UP],
            State(2, 3): [Action.LEFT, Action.UP],
        }
        sample_grid.set(rewards=rewards, actions=actions)
        return sample_grid
