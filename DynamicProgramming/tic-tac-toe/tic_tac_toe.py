from __future__ import annotations
from enum import Enum
from typing import Dict, Tuple
import pprint


class GameState(Enum):
    INIT = 0
    PLAYING = 1
    CROSS_WIN = 2
    NOUGHT_WIN = 3
    DRAW = 4


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


class Agent():
    def __init__(self, name: str, mark: Mark) -> None:
        self.name = name
        self.mark = mark
        self.MAX_TRIAL = 2
        pass

    def place(self, position: Tuple[int, int], grid: Grid) -> None:
        num_trial = 0
        exception = None

        while num_trial < self.MAX_TRIAL:
            try:
                num_trial += 1
                grid.update(position, self.mark)
                print(f"{self.name} places at {position}")
                break
            except Exception as ex:
                exception = ex
                print(ex)
                print(f"try again... {num_trial}")
            if num_trial < self.MAX_TRIAL:
                position = self.input()
            else:
                num_trial += 1

        if num_trial > self.MAX_TRIAL:
            raise Exception(
                f"Exceed MAX {self.MAX_TRIAL} trial... last error....{exception}")
        pass

    def input(self) -> Tuple[int, int]:
        """
            basically accept input from the console
        """
        print(f"{self.name} input now")
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
    # @staticmethod
    # def check_row_result(grid: Grid) -> Tuple[GameState, int]:
    #     row = col = grid.N
    #     winner_mark = None
    #     all_filled = True
    #     win_row = None
    #     got_winner = False
    #     # Check Row
    #     for r in range(1, row+1):
    #         first_value = grid.get_value(
    #             position=(r, 1)
    #         )
    #         if first_value == Mark.BLANK:
    #             all_filled = False
    #             continue
    #         got_winner = True
    #         for c in range(2, col+1):
    #             _value = grid.get_value(
    #                 position=(r, c)
    #             )
    #             if _value == Mark.BLANK:
    #                 all_filled = False
    #             if first_value != _value:
    #                 got_winner = False
    #                 break
    #         if got_winner:
    #             winner_mark = first_value
    #             win_row = r
    #             break
    #     if got_winner:
    #         if winner_mark == Mark.CROSS:
    #             return GameState.CROSS_WIN, win_row
    #         elif winner_mark == Mark.NOUGHT:
    #             return GameState.NOUGHT_WIN, win_row
    #         else:
    #             raise Exception("Invalid game state")
    #     elif all_filled:
    #         return GameState.DRAW, -1
    #     return GameState.PLAYING, -1

    # @staticmethod
    # def check_column_result(grid: Grid) -> Tuple[GameState, int]:
    #     row = column = grid.N
    #     winner_mark = None
    #     all_filled = True
    #     win_column = -1
    #     got_winner = False
    #     # Check Column
    #     for c in range(1, column+1):
    #         first_value = grid.get_value(
    #             position=(1, c)
    #         )
    #         if first_value == Mark.BLANK:
    #             all_filled = False
    #             continue
    #         got_winner = True
    #         for r in range(2, row+1):
    #             _value = grid.get_value(
    #                 position=(r, c)
    #             )
    #             print(f"check point {(r,c)}")
    #             if _value == Mark.BLANK:
    #                 all_filled = False
    #             if first_value != _value:
    #                 got_winner = False
    #                 break
    #         if got_winner:
    #             winner_mark = first_value
    #             win_column = c
    #             break
    #     if got_winner:
    #         if winner_mark == Mark.CROSS:
    #             return GameState.CROSS_WIN, win_column
    #         elif winner_mark == Mark.NOUGHT:
    #             return GameState.NOUGHT_WIN, win_column
    #         else:
    #             raise Exception("Invalid game state")
    #     elif all_filled:
    #         return GameState.DRAW, -1
    #     return GameState.PLAYING, -1


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
            print(ex)

    def run_agent_turn(self, agent: Agent) -> None:
        position: Tuple[int, int] = agent.input()
        agent.place(
            position=position,
            grid=self.grid
        )