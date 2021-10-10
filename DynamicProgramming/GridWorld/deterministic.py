"""
Applying Dynamic programming to search for most efficient policy to 
reach the terminal with high reward.
However, it still requires full model of environment. 
In the read world, the complexity of the environment may not fully satisfy 
the condition of "complete knowledge of full model of enviroment".
Therefore, it is a determinsitic model as described in
 https://towardsdatascience.com/reinforcement-learning-dynamic-programming-2b89da6ea1b
 
For non-deterministic model, please refer to Monte Carlo method:
reference: https://towardsdatascience.com/reinforcement-learning-rl-101-with-python-e1aa0d37d43b

"""
from .model import Grid, Action, Policy, Values, NO_REWARD, Reward
from typing import Dict, List, Tuple
from random import choices, random
import math
from .loghelper import get_logger, logging

logger = get_logger(__name__, logging.DEBUG)


class Deterministic_Optimizer:
    GAMMA = 0.9
    thresold = 1e-4
    ACTIONS = (Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT)

    def _init_value_iteration(self, grid: Grid) -> Tuple[Policy, Values]:
        policy: Policy = dict()
        for state in grid.actions.keys():
            policy[state] = choices(self.ACTIONS)

        values: Values = dict()
        states = grid.all_states()
        for state in states:
            if state in grid.actions:
                values[state] = NO_REWARD
            else:
                values[state] = NO_REWARD
        return policy, values

    def optimize(self, grid: Grid) -> Tuple[Policy, Values]:
        states = grid.all_states()
        policy, values = self._init_value_iteration(grid=grid)

        # repeat until convergence
        # Values[state] = max[action]{sum[state',reward]{p(state',reward|state,action) [reward + GAMMA * Values[state']]}}
        iteration = 0
        while True:
            # Maximize value function first
            max_change = 0
            for state in states:
                old_vs = values[state]

                # Values[state] only has policy if not a terminal state
                if state not in policy or grid.is_terminal(s=state):
                    continue
                new_v = float("-inf")
                # Find action leading to max value function
                for action in grid.actions[state]:
                    grid.state = state
                    reward = grid.move(action=action)

                    v = reward + self.GAMMA * values[grid.state]
                    logger.debug(
                        f"{iteration}:{state}->{grid.state} action:{action} reward:{reward} v:{v}"
                    )
                    new_v = v if v > new_v else new_v
                values[state] = new_v
                max_change = max(max_change, abs(new_v - old_vs))
            iteration += 1
            if max_change < self.thresold:
                break

        # Find policy leading to optimal value function
        for state in policy.keys():
            best_act = None
            best_value = float("-inf")
            if state not in policy or grid.is_terminal(s=state):
                continue
            for action in grid.actions[state]:
                grid.state = state
                reward = grid.move(action=action)

                v = reward + self.GAMMA * values[grid.state]
                if v > best_value:
                    best_act = action
                    best_value = v
            policy[state] = best_act
            pass
        return policy, values
