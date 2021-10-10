from __future__ import annotations
from collections import namedtuple
from enum import Enum
from typing import List, Dict
from typing_extensions import TypeAlias
from .loghelper import get_logger, logging

logger = get_logger(__name__, logging.INFO)

Position = namedtuple("Position", ["row", "column"])
Reward = namedtuple("Reward", ["row", "column"])
Action = namedtuple("Action", ["row", "column"])

class Action (Enum):
    UP = "U"
    DOWN = "D"
    RIGHT = "R"
    LEFT = "L"
    def __str__(self):
        return self.value

Actions: TypeAlias = Dict[ Position, List[Action] ]
Rewards: TypeAlias = Dict[ Position, Reward]

class Grid:
    def __init__(self, width, height, start: Position):
        self.width: int = width
        self.height: int = height
        self.start: Position = start
        self._state: Position = None

    def set(self, rewards: Rewards, actions: Actions) -> None:
        self.rewards: Rewards = rewards
        self.actions: Actions = actions

    @property
    def state(self) -> Position:
        return self._state

    @state.setter
    def state(self, value: Position) -> None:
        self._state = value

    def is_terminal(self, s: Position) -> bool:
        """
        it is a terminal if not in possible actions
        """
        return s not in self.actions

    def game_over(self) -> bool:
        """
        Game over if state of itself is not in possible actions
        """
        return self.state not in self.actions

    def move(self, action:Action) -> List[Reward] :
        """
            check if action is possible, then moves in that direction
        """
        if action in self.actions[self.state]:
            if action == 