from __future__ import annotations
from functools import reduce
from .Arena import *
from copy import deepcopy
from heapq import heapify
from typing import Tuple, Any, Union


class PrioritizedItem:
    def __init__(self, priority: float, value: Any) -> None:
        self.priority = priority
        self.value = value

    def __repr__(self):
        return f"{self.value}({self.priority})"

    def __lt__(self, other):
        return self.priority > other.priority


class Bellman_Runner:
    MAX_ITERATION = 1000
    DISCOUNT = 0.8
    THRESHOLD = 0.1

    @staticmethod
    def _render_raw_values(length: int, width: int, values: List[Union(float, Action)]):
        buffer: StringIO = StringIO()
        for r in range(length):
            for c in range(width):
                inx = r * width + c
                if isinstance(values[inx], float):
                    buffer.write("{:10.3f} ".format(values[inx]))
                else:
                    buffer.write(f"{str(values[inx])} ")
            buffer.write("\n")
        print(buffer.getvalue())

    def calculate_state_value_function(self, game: Board) -> List[float]:
        """Iterate each state to calculate the Volume function iteratively"""
        game_board = game.board
        prob_dist = game.Prob
        state_value_function = [0] * len(game_board)

        def sum_up_state_value_function(val_func) -> float:
            return reduce(lambda a, b: a + b, val_func)

        run = True
        count = 0

        while run and count < self.MAX_ITERATION:
            old_state_value_function = deepcopy(state_value_function)
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
                            + self.DISCOUNT * prob * old_state_value_function[new_state]
                        )
                    return _v

                _v_list = []
                for action in prob_dist[pos].keys():
                    _v_list.append(calculate_value_per_action(action))
                state_value_function[pos] = max(_v_list)
                pass
            new_sum = sum_up_state_value_function(val_func=state_value_function)
            old_sum = sum_up_state_value_function(val_func=old_state_value_function)

            if abs(old_sum - new_sum) < self.THRESHOLD:
                run = False
                break
            count += 1
            pass

        return state_value_function

    def find_policy_function(
        self, game: Board, state_value_function: List[float]
    ) -> List[Action]:
        """Extract the policy from the state_value function

        Args:
            game (Board): [game board]
            state_value_function (List[float]): [state value function]

        Returns:
            List[Action]: [description]
        """
        prob_dist = game.Prob
        policy_function = [None] * len(state_value_function)

        for pos in range(len(state_value_function)):
            _state_value_list: List[Tuple[float, Action]] = []

            for action, value in prob_dist[pos].items():
                action_prob_list: List[Action_Probability] = value
                # sum_v: float = reduce(
                #     lambda a, b: state_value_function[a.state]
                #     + state_value_function[b.state],
                #     action_prob_list,
                # )
                # if pos == 4:
                #     print(
                #         f"{pos}:action_prob_list({len(action_prob_list)}):{action} : {action_prob_list}\n"
                #     )
                sum_v = 0
                for action_prob in action_prob_list:
                    sum_v += (
                        self.DISCOUNT
                        * action_prob.prob
                        * state_value_function[action_prob.state]
                        + action_prob.reward
                    )

                _state_value_list.append(PrioritizedItem(priority=sum_v, value=action))

            # print(f"Pos:{pos} - {_state_value_list}")
            # Find the action with max value
            if len(_state_value_list) == 0:
                continue
            heapify(_state_value_list)
            policy_function[pos] = _state_value_list[0]

        return policy_function
