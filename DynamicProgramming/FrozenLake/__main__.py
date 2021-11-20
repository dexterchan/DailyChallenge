from .Arena import *
from .Runner import *

l = 3
w = 4
board = Board(length=l, width=w)
board.render()
board.populate_transition_probaility(deterministic=False)

bellman = Bellman_Runner()
values_matrix = bellman.calculate_value_function(game=board)
print(Bellman_Runner._render_raw_values(length=l, width=w, values=values_matrix))


# print((board.Prob[0][Action.LEFT]))
# board.i_move(action=Action.LEFT)
# board.render()

# board.i_move(action=Action.RIGHT)
# board.render()

# board.i_move(action=Action.DOWN)
# board.render()
