from .Arena import *
from .Runner import *

l = 3
w = 4
board = Board(length=l, width=w)
board.render()
board.populate_transition_probaility(deterministic=False)

# for pos in range(len(board.Prob)):

#     for a in range(len(Action)):
#         action = Action(a)
#         prob_actionlist = board.Prob[pos][action]
#         if len(prob_actionlist) < len(Action):
#             print(
#                 f"{pos}:  action{str(action)} - {len(prob_actionlist)} - {prob_actionlist}"
#             )

bellman = Bellman_Runner()
state_value_function = bellman.calculate_state_value_function(game=board)
print("State Value Function:\n")
Bellman_Runner._render_raw_values(length=l, width=w, values=state_value_function)
policy_function = bellman.find_policy_function(
    game=board, state_value_function=state_value_function
)
print("Policy function\n")
Bellman_Runner._render_raw_values(length=l, width=w, values=policy_function)


# print((board.Prob[0][Action.LEFT]))
# board.i_move(action=Action.LEFT)
# board.render()

# board.i_move(action=Action.RIGHT)
# board.render()

# board.i_move(action=Action.DOWN)
# board.render()
