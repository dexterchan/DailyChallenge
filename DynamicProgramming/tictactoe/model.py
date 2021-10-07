from __future__ import annotations
from abc import abstractmethod
from os import stat
from typing import Protocol, Tuple, List
from enum import Enum
from abc import ABC
from .loghelper import get_logger, logging

logger = get_logger(__name__, logging.INFO)

class Memory(Enum):
    BLANK = 0
    ME = 1
    YOU = 2

    @staticmethod
    def symbol(memory: Memory) -> str:
        if memory == Memory.BLANK:
            return " "
        elif memory == Memory.ME:
            return "M"
        elif memory == Memory.YOU:
            return "Y"

    @staticmethod
    def translate(mark: Mark, myMark: Mark) -> Memory:
        """
            translate the Mark to Memory Unit
        """
        if mark == Mark.BLANK:
            return Memory.BLANK
        elif mark == myMark:
            return Memory.ME
        else:
            return Memory.YOU

class Mark(Enum):
    BLANK = 0
    CROSS = 1
    NOUGHT = 2

    @staticmethod
    def symbol(mark: Mark) -> str:
        if mark == Mark.BLANK:
            return " "
        elif mark == Mark.CROSS:
            return "X"
        elif mark == Mark.NOUGHT:
            return "O"

class State:
    def __init__(self, dimension: int = 3) -> None:
        self._state: List[Memory] = None
        self.N = dimension
        self.this_move: Tuple[int, int] = None
        pass

    @property
    def key(self) -> str:
        m_list = [Memory.symbol(m) for m in self._state]
        key = "".join(m_list).replace(" ", "_")
        return key

    @classmethod
    def replicate_from_Grid(cls,
                            grid: Grid,
                            my_mark: Mark,
                            this_move: Tuple[int, int] = None) -> State:
        new_state = cls(dimension=grid.N)

        new_state._state = [Memory.translate(
            mark=mark, myMark=my_mark) for mark in grid._grid]

        if this_move is not None:
            exclude_index = grid._inx(
                position=this_move
            )
            new_state._state[exclude_index] = Memory.BLANK
            new_state.this_move = this_move
        return new_state

    def _inx(self, position: Tuple[int, int]) -> None:
        """
            translate position to arrayindex
        """
        (row, column) = position
        return (row-1) * self.N + (column-1)

    def __str__(self) -> str:
        """
            render the state
        """

        lines = [f"state:{self.key}"]  # [f"state:{self.key}"]
        for r in range(self.N):
            line = "|"
            for c in range(self.N):
                line += Memory.symbol(memory=self._state[
                    self._inx(
                        position=(r+1, c+1)
                    )
                ])
                line += "|"
            lines.append(line)
        lines.append(f"last move:{self.this_move}")
        return "\n".join(lines)

class Grid():
    def __init__(self, dimension: int = 3) -> None:
        self._grid = [Mark.BLANK] * (dimension*dimension)
        self.N = dimension
        pass

    def render(self) -> None:
        """
            render the grid
        """
        for r in range(self.N):
            line = "|"
            for c in range(self.N):
                line += Mark.symbol(mark=self._grid[
                    self._inx(
                        position=(r+1, c+1)
                    )
                ])
                line += "|"
            print(line)
        pass

    def get_value(self, position: Tuple[int, int]) -> Mark:
        return self._grid[
            self._inx(position=position)
        ]

    def validate_new_place(self, position: Tuple[int, int]) -> bool:
        """
            check if the new place is valid
        """
        (row, column) = position
        logger.debug(f"validate new place: {row}:{type(row)}, {column}:{type(column)}, ")
        if row < 1 or row > self.N:
            raise Exception(f"row {row} out of bound")
        if column < 1 or column > self.N:
            raise Exception(f"column {column} out of bound")

        inx = self._inx(
            position=position
        )
        if self._grid[inx] != Mark.BLANK:
            raise Exception(f"Position {position} occupied")

        return True

    def _inx(self, position: Tuple[int, int]) -> None:
        """
            translate position to arrayindex
        """
        (row, column) = position
        return (row-1) * self.N + (column-1)

    def update(self, position: Tuple[int, int], mark: Mark) -> None:
        if self.validate_new_place(
            position=position
        ):
            # Update the grid with the mark
            self._grid[self._inx(
                position=position
            )] = mark
        else:
            raise Exception("update failure")



class Place_Interface(Protocol):
    def place_mark(self, grid: Grid, mark:Mark) -> Tuple[int, int]:
        pass
    
    def sync_name(self, name:str) -> None:
        pass

    def get_scene_key(self, grid: Grid , mark:Mark) ->str:
        state = State.replicate_from_Grid(
            grid=grid,
            my_mark=mark
        )
        return state.key

class Manual_Console_Impl(Place_Interface):
    def __init__(self, name:str) -> None:
        self.name = name

    def place_mark(self, grid: Grid, mark:Mark) -> Tuple[int, int]:
        scene_key = self.get_scene_key(grid=grid, mark=mark)
        print(f"{self.name} - {Mark.symbol(mark)} input now")
        print(f"{self.name} Current state: {scene_key}")
        row: int = int(input("input row coordinate: "))
        column: int = int(input("Input column coordinate: "))
        position = (row, column)
        return position

    def sync_name(self, name:str) -> None:
        self.name = name + "-human"


class Brain(ABC):
    @abstractmethod
    def pick_space(self, scene_key:str) -> Tuple[int,int]:
        pass


class AI_Impl(Place_Interface):
    def __init__(self, name:str, brain:Brain) -> None:
        self.name:str = name
        self.brain:Brain = brain

    def place_mark(self, grid: Grid, mark:Mark) -> Tuple[int, int]:
        scene_key = self.get_scene_key(
            grid=grid, mark=mark
        )
        print(f"{self.name} - {Mark.symbol(mark)} input now")
        print(f"{self.name} - Current state: {scene_key}")
        return self.brain.pick_space(
            scene_key=scene_key
        )
    
    def sync_name(self, name:str) -> None:
        self.name = name + "-AI"