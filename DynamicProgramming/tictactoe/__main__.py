from __future__ import annotations
from .tic_tac_toe import *
from .statistics import Statistics


if __name__ == "__main__":
    DIM = 3
    tic_tac_toe_game: Tic_Tac_Toe_Game = Tic_Tac_Toe_Game(
        dimension=DIM
    )
    statistics: Statistics = Statistics(
        "game.statistics.json", dim=DIM
    )
    tic_tac_toe_game.play()
    (agentA_state, agentB_state) = tic_tac_toe_game.get_agent_state()
    print(f"A:{agentA_state}")
    print(f"B:{agentB_state}")
    statistics.update_statistics(
        state_list=tic_tac_toe_game.agentA.state_history,
        final_game_state=agentA_state
    )
    statistics.update_statistics(
        state_list=tic_tac_toe_game.agentB.state_history,
        final_game_state=agentB_state
    )
    statistics.save()
