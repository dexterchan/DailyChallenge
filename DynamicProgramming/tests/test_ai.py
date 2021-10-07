from tictactoe.tic_tac_toe import *
from tictactoe.statistics import Statistics
from tictactoe.ai import Epsilon_Greedy

statistics_dict = {"my_statistics": {"_________": {"2_2": {"win": 1}}, "Y___M____": {"1_2": {"win": 1}}, "YM_YM____": {"3_2": {"win": 1}}, "____Y____": {"1_1": {"loss": 1}}, "MY__Y____": {"2_1": {"loss": 1}}}, "file_name": "game.statistics.json", "dim": 3}

statistics = Statistics(
    file_name="game.statistics.json", dim=3
)

ep = Epsilon_Greedy(
    statistics=statistics, min_probability_try_new=0.5
)
pick = ep.pick_space(
    scene_key="_________"
)
print(pick)

pick = ep.pick_space(
    scene_key="Y________"
)
print(pick)

pick = ep.pick_space(
    scene_key="MY__Y____"
)
print(pick)