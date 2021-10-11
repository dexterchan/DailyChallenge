from .tic_tac_toe import AgentPlayResult, State
from typing import List
from collections import defaultdict
from shutil import copyfile
import json
import os
from .io import State_IO


class Statistics:
    """
        Statistic collects state list and update the win/loss statistic of each move in each state.
        A key is derived from the state. win,loss,draw statistic with the coordinates save into Dict:
        win, loss, draw e.g.

        {
            state_key:{
                <row>_<col>:{
                    win: <win figure>,
                    loss:<loss figure>,
                    draw:<draw figure>
                }
            }
        }
        then statistic persists the state list into a file for later iteration update
    """

    def __init__(self, state_io:State_IO, dim:int) -> None:
        self.state_io = state_io
        obj = state_io.read()
        self.dim = dim
        self.num_samples = 0
        self.my_statistics = obj.get("my_statistics", {})
        self.dim = obj.get("dim", dim)
        self.num_samples = obj.get("num_samples", 0)
        

    def update_statistics(self, state_list: List[State], final_game_state: AgentPlayResult) -> None:
        if final_game_state == AgentPlayResult.DRAW:
            flag = "draw"
        elif final_game_state == AgentPlayResult.WIN:
            flag = "win"
        elif final_game_state == AgentPlayResult.LOSS:
            flag = "loss"

        for state in state_list:
            state_key = state.key
            row_col = f"{state.this_move[0]}_{state.this_move[1]}"

            self.my_statistics[state_key] = self.my_statistics.get(
                state_key, {})

            self.my_statistics[state_key][row_col] = self.my_statistics[state_key].get(
                row_col, {}
            )
            self.my_statistics[state_key][row_col][flag] = self.my_statistics[state_key][row_col].get(
                flag, 0
            ) + 1

            pass
        self.num_samples += 1
        pass

    def to_dict(self):
        d = self.__dict__
        new_d = {}
        exclude_fields = ["state_io"]
        for key, value in d.items():
            if key not in exclude_fields:
                new_d[key] = value
        return new_d

    def save(self) -> None:
        self.state_io.write(
            data=self.to_dict()
        )
