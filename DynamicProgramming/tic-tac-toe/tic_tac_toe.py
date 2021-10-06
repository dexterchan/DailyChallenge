from __future__ import annotations
from enum import Enum
import logging
from typing import Dict, Tuple, List


logging.basicConfig(
    format="%(asctime)-15s %(levelname)s %(message)s (%(filename)s:%(lineno)s)")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class AgentPlayResult(Enum):
    DRAW = 0
    WIN = 1
    LOSS = 2


class GameState(Enum):
    INIT = 0
    PLAYING = 1
    CROSS_WIN = 2
    NOUGHT_WIN = 3
    DRAW = 4


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


class Agent():
    """
        Agent records each move from Grid to State.
        Keeping the same coordinate, each Mark of the Grid will be translated to Memory of the State.
        IN each move, State persists the position of the Move.
        After each turn of placing, agent will append State into a State List.
        The state list will be used for training automation bot.
    """

    def __init__(self, name: str, mark: Mark) -> None:
        self.name = name
        self.mark = mark
        self.MAX_TRIAL = 2
        self.state_history: List[State] = []
        pass

    def place(self, position: Tuple[int, int], grid: Grid) -> None:
        num_trial = 0
        exception = None

        while num_trial < self.MAX_TRIAL:
            try:
                num_trial += 1
                grid.update(position, self.mark)
                print(f"{self.name} places at {position}")

                state = State.replicate_from_Grid(
                    grid=grid,
                    my_mark=self.mark,
                    this_move=position
                )
                print(state)
                self.state_history.append(state)
                break
            except Exception as ex:
                exception = ex
                logger.error(ex)
                print(f"try again... {num_trial}")
            if num_trial < self.MAX_TRIAL:
                position = self.input(grid=grid)
            else:
                num_trial += 1

        if num_trial > self.MAX_TRIAL:
            raise Exception(
                f"Exceed MAX {self.MAX_TRIAL} trial... last error....{exception}")
        pass

    def input(self, grid: Grid) -> Tuple[int, int]:
        """
            basically accept input from the console
        """
        state = State.replicate_from_Grid(
            grid=grid,
            my_mark=self.mark
        )
        print(f"{self.name} - {Mark.symbol(self.mark)} input now")
        print(f"Current state: {state.key}")
        row: int = int(input("input row coordinate: "))
        column: int = int(input("Input column coordinate: "))
        position = (row, column)
        return position


class Judge:

    @staticmethod
    def check_result(grid: Grid) -> Dict:
        game_state, c = Judge.check_column_result(
            grid=grid
        )
        if game_state != GameState.PLAYING:
            return {
                "game_state": game_state,
                "type": "Column",
                "inx": c
            }
        game_state, r = Judge.check_row_result(
            grid=grid
        )
        if game_state != GameState.PLAYING:
            return {
                "game_state": game_state,
                "type": "Row",
                "inx": r
            }
        game_state, d = Judge.check_diagonal(
            grid=grid
        )
        return {
            "game_state": game_state,
            "type": "diagonal",
            "inx": d
        }

    @staticmethod
    def check_diagonal(grid: Grid) -> Tuple[GameState, int]:
        dim = grid.N
        backslash_mark = grid.get_value(position=(1, 1))
        slash_mark = grid.get_value(position=(1, dim))
        backslash_win = True
        slash_win = True
        if backslash_mark == Mark.BLANK:
            backslash_win = False
        if slash_mark == Mark.BLANK:
            slash_win = False
        for d in range(2, dim+1):
            new_b_value = grid.get_value(position=(d, d))
            if new_b_value != backslash_mark:
                backslash_win = False
            new_s_value = grid.get_value(position=(d, dim-(d-1)))
            if new_s_value != slash_mark:
                slash_win = False
        if backslash_win:
            # if backslash_mark == Mark.CROSS:
            #     return GameState.CROSS_WIN, 1
            # elif backslash_mark == Mark.NOUGHT:
            #     return GameState.NOUGHT_WIN, 1
            return Judge._resolve_CROSS_NOUGHT_WIN(
                ref_mark=backslash_mark, inx=1
            )
        if slash_win:
            # if slash_mark == Mark.CROSS:
            #     return GameState.CROSS_WIN, 2
            # elif slash_mark == Mark.NOUGHT:
            #     return GameState.NOUGHT_WIN, 2
            return Judge._resolve_CROSS_NOUGHT_WIN(
                ref_mark=slash_mark, inx=2
            )
        return GameState.PLAYING, -1

    @staticmethod
    def check_column_result(grid: Grid) -> Tuple[GameState, int]:
        row = column = grid.N
        all_filled = True
        for col in range(1, column+1):
            ref_mark = grid.get_value(
                position=(1, col)
            )
            if ref_mark == Mark.BLANK:
                all_filled = False
            all_match = True
            for row in range(2, row+1):
                value = grid.get_value(position=(row, col))
                if ref_mark != value:
                    all_match = False
                if value == Mark.BLANK:
                    all_filled = False
            if all_match and ref_mark != Mark.BLANK:
                print(f"Got match in column {col}")
                return Judge._resolve_CROSS_NOUGHT_WIN(ref_mark=ref_mark, inx=col)
        if all_filled:
            return GameState.DRAW, -1
        return GameState.PLAYING, -1

    @staticmethod
    def check_row_result(grid: Grid) -> Tuple[GameState, int]:
        row = column = grid.N
        all_filled = True
        for row in range(1, row+1):
            ref_mark = grid.get_value(
                position=(row, 1)
            )
            if ref_mark == Mark.BLANK:
                all_filled = False
            all_match = True
            for col in range(2, column+1):
                value = grid.get_value(position=(row, col))
                if ref_mark != value:
                    all_match = False
                if value == Mark.BLANK:
                    all_filled = False
            if all_match and ref_mark != Mark.BLANK:
                print(f"Got match in row {row}")
                return Judge._resolve_CROSS_NOUGHT_WIN(ref_mark=ref_mark, inx=row)
        if all_filled:
            return GameState.DRAW, -1
        return GameState.PLAYING, -1

    @staticmethod
    def _resolve_CROSS_NOUGHT_WIN(ref_mark: Mark, inx: int) -> Tuple[GameState, int]:
        if ref_mark == Mark.CROSS:
            return GameState.CROSS_WIN, inx
        elif ref_mark == Mark.NOUGHT:
            return GameState.NOUGHT_WIN, inx


class Tic_Tac_Toe_Game:
    """
        Tick Tac Toe Game supports two players 
        Agent A and Agent B takes turn to make the space with X and O
        in a N X N grid.
        Agent A marks CROSS - "X".
        Agent B marks NOUGHT - "O".
        Each grid cell contains possibles values: X,O,BLANK
        Grid validate each mark from the agent.

        The player who succeeds in placing N of their marks in a horizontal, vertical, or diagonal row is the winner

        After each Agent places his/her mark, the judge will check the winner.
        If the grid is filled without winners, judge declares a "draw".
    """

    def __init__(self, dimension: int = 3) -> None:
        self.agentA = Agent(name="A", mark=Mark.CROSS)
        self.agentB = Agent(name="B", mark=Mark.NOUGHT)
        self.grid = Grid(
            dimension=dimension
        )
        self.state = GameState.INIT
        pass

    def play(self) -> None:
        self.state = GameState.PLAYING

        try:
            while (True):
                # agent A turn:
                self.run_agent_turn(agent=self.agentA)
                self.grid.render()
                result = Judge.check_result(
                    self.grid
                )
                print(result)
                if result["game_state"] != GameState.PLAYING:
                    break
                # agent B turn:
                self.run_agent_turn(agent=self.agentB)
                self.grid.render()
                result = Judge.check_result(
                    self.grid
                )
                print(result)
                if result["game_state"] != GameState.PLAYING:
                    break
        except Exception as ex:
            logger.error(ex)
        self.final_game_state = result["game_state"]

    def get_agent_state(self) -> Tuple[AgentPlayResult, AgentPlayResult]:
        # Agent A state:
        agentA_state = None
        agentB_state = None

        if self.final_game_state == GameState.DRAW:
            agentA_state = AgentPlayResult.DRAW
            agentB_state = AgentPlayResult.DRAW
        elif self.final_game_state == GameState.CROSS_WIN:
            agentA_state = AgentPlayResult.WIN if self.agentA.mark == Mark.CROSS else AgentPlayResult.LOSS
            agentB_state = AgentPlayResult.WIN if self.agentB.mark == Mark.CROSS else AgentPlayResult.LOSS
        elif self.final_game_state == GameState.NOUGHT_WIN:
            agentA_state = AgentPlayResult.WIN if self.agentA.mark == Mark.NOUGHT else AgentPlayResult.LOSS
            agentB_state = AgentPlayResult.WIN if self.agentB.mark == Mark.NOUGHT else AgentPlayResult.LOSS
        return agentA_state, agentB_state

    def run_agent_turn(self, agent: Agent) -> None:
        position: Tuple[int, int] = agent.input(self.grid)
        agent.place(
            position=position,
            grid=self.grid
        )
