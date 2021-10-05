from .tic_tac_toe import AgentPlayResult, State
from typing import List
from collections import defaultdict

import json
import os


class Statistics:
    """
        Statistic collects state list and update the win/loss statistic of each move in each state.
        A key is derived from the state. win,loss,draw statistic with the coordinates save into Dict:
        win, loss, draw e.g.
        {
            state_key:{
                win: {
                <row>_<col>: <win figure>
                },
                loss:{
                    <row>_<col>: <loss figure>
                }
                draw: {
                    <row>_<col> : draw figure
                }
            }
        }
        then statistic persists the state list into a file for later iteration update
    """

    def __init__(self, file_name: str) -> None:
        self.my_statistics = {}
        self.file_name = file_name
        if os.path.isfile(file_name):
            with open(file_name, "r") as f:
                self.my_statistics = json.load(f)

    def update_statistics(self, state_list: List[State], final_game_state: AgentPlayResult) -> None:
        if final_game_state == AgentPlayResult.DRAW:
            flag = "draw"
        elif final_game_state == AgentPlayResult.WIN:
            flag = "win"
        elif final_game_state == AgentPlayResult.LOSS:
            flag = "loss"

        for state in state_list:
            state_key = state.key
            self.my_statistics[state_key] = self.my_statistics.get(
                state_key, {})
            self.my_statistics[state_key][flag] = self.my_statistics[state_key].get(flag, {
            })
            row_col = f"{state.this_move[0]}_{state.this_move[1]}"
            self.my_statistics[state_key][flag][row_col] = self.my_statistics[state_key][flag].get(
                row_col, 0) + 1
            pass
        pass

    def save(self) -> None:
        with open(self.file_name, "w") as f:
            json.dump(self.my_statistics, f)
