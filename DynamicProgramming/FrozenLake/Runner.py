from __future__ import annotations
from functools import reduce
from .Arena import *
from copy import deepcopy
import heapq


class Bellman_Runner:
    MAX_ITERATION = 1000
    DISCOUNT = 0.8
    THRESHOLD = 0.1

    @staticmethod
    def _render_raw_values(length: int, width: int, values: List[float]):
        buffer: StringIO = StringIO()
        for r in range(length):
            for c in range(width):
                inx = r * width + c
                buffer.write("{:10.3f} ".format(values[inx]))
            buffer.write("\n")
        print(buffer.getvalue())

    def calculate_value_function(self, game: Board) -> List[float]:
        """Iterate each state to calculate the Volume function iteratively"""
        game_board = game.board
        prob_dist = game.Prob
        value_function = [0] * len(game_board)

        def sum_up_value_function(val_func) -> float:
            return reduce(lambda a, b: a + b, val_func)

        run = True
        count = 0

        while run and count < self.MAX_ITERATION:
            old_value_function = deepcopy(value_function)
            for pos in range(len(game_board)):
                """[summary]"""

                def calculate_value_per_action(action: Action) -> float:
                    _v = 0.0
                    for action_prob in prob_dist[pos][action]:
                        reward = action_prob.reward
                        new_state = action_prob.state
                        prob = action_prob.prob
                        _v += (
                            reward
                            + self.DISCOUNT * prob * old_value_function[new_state]
                        )
                    return _v

                _v_list = []
                for action in prob_dist[pos].keys():
                    _v_list.append(calculate_value_per_action(action))
                value_function[pos] = max(_v_list)
                pass
            new_sum = sum_up_value_function(val_func=value_function)
            old_sum = sum_up_value_function(val_func=old_value_function)

            if abs(old_sum - new_sum) < self.THRESHOLD:
                run = False
                break
            count += 1
            pass

        return value_function
