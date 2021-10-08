from __future__ import annotations
from logging import addLevelName
from .tic_tac_toe import *
from .statistics import Statistics
from .ai import Epsilon_Greedy
import math

from .loghelper import get_logger, logging
logger = get_logger(__name__, logging.INFO)
import argparse
if __name__ == "__main__":
    DIM = 3
    
    parser = argparse.ArgumentParser(description="tictactoe")
    
    parser.add_argument("-s","--statisticfile", type=str, default="/tmp/game.statistics.json")
    parser.add_argument("--training", dest="training", action = "store_true")
    parser.add_argument("--iteration", dest="iteration", default=10)
    parser.add_argument("--learningrate", dest="learningrate", type=float, default=0.1)
    parser.add_argument("--min_probaility", dest="minprob", type=float, default=0.1)
    
    # flag_parser = parser.add_argument("--no-training", dest="training", action = "store_false")
    # parser.set_defaults(training=True)
    args = parser.parse_args()
    logger.error(args.training)

    human_player:bool = not args.training
    min_probability = args.minprob
    learning_rate = args.learningrate
    max_iteration = int(args.iteration) if not human_player else 1
    statistics: Statistics = Statistics(
            args.statisticfile, dim=DIM
        )
    iteration = 1
    while (iteration <= max_iteration):
        logger.info(f"iteration - {iteration}")
        
        min_probability_try_new = min_probability + (1-min_probability)* math.exp(-1 * iteration * learning_rate) if not human_player else 0.1

        ep_ai1 = Epsilon_Greedy(
            statistics=statistics, min_probability_try_new=min_probability_try_new
        )
        ep_ai2 = Epsilon_Greedy(
            statistics=statistics, min_probability_try_new=min_probability_try_new
        )
        
        A_brain = Manual_Console_Impl(
            name="A"
        ) if human_player else  AI_Impl(
            name="epA", brain=ep_ai1
        ) 

        B_brain = AI_Impl(
            name="epB", brain=ep_ai2
        )

        agentA:Agent=Agent(name="A", mark=Mark.CROSS, place_interface=A_brain)
        agentB:Agent=Agent(name="B", mark=Mark.NOUGHT, place_interface=B_brain)
        tic_tac_toe_game: Tic_Tac_Toe_Game = Tic_Tac_Toe_Game(
            dimension=DIM, 
            agentA=agentA, 
            agentB=agentB
        )
        
        
        tic_tac_toe_game.play()
        (agentA_state, agentB_state) = tic_tac_toe_game.get_agent_state()
        print(f"{iteration}:A:{agentA_state}")
        print(f"{iteration}:B:{agentB_state}")
        logger.info(f"{iteration}: min_probability_try_new: {min_probability_try_new}")
        statistics.update_statistics(
            state_list=tic_tac_toe_game.agentA.state_history,
            final_game_state=agentA_state
        )
        statistics.update_statistics(
            state_list=tic_tac_toe_game.agentB.state_history,
            final_game_state=agentB_state
        )
        statistics.save()
        iteration += 1
