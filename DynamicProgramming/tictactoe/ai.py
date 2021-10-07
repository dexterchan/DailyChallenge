import logging
from .statistics import Statistics
from typing import List, Tuple, Dict
from random import random, choice
from collections import namedtuple
from heapq import heapify
from .loghelper import get_logger
ScorePoint = namedtuple("ScorePoint", ["coordinate", "score"])
ScoreBook = namedtuple("ScoreBook", ["scene_key", "score_dict","score_list"])

logger = get_logger(__name__, logging.INFO)
class Epsilon_Greedy:
    WIN_SCORE: int = 2
    DRAW_SCORE: int = 1
    LOSS_SCORE: int = -2
    MAX_SCORE: int = 2**31/2-1

    def __init__(self, statistics: Statistics, min_probability_try_new: float) -> None:
        self.statistics: Statistics = statistics
        self.min_odds_try_new: float = min_probability_try_new
        self.scores_cache:Dict[str, ScoreBook] = {}
        self._init_score()
        pass
    
    def _init_score(self) -> None:
        """
            Init the statistics to gather scores
        """
        for scene_key, score_page_dict in self.statistics.my_statistics.items():
            
            score_dict:Dict[str,float] = {}
            score_list:List[ScorePoint] = []
            for pos, result_map in score_page_dict.items():
                score_point = 0
                for outcome, num in result_map.items():
                    if outcome == "win":
                        score_point += self.WIN_SCORE * num
                    elif outcome == "loss":
                        score_point += self.LOSS_SCORE * num
                    else:
                        score_point += self.DRAW_SCORE * num
                score_point_obj = ScorePoint(
                    coordinate=pos,
                    score=score_point
                )
                score_dict[pos] = score_point 
                score_list.append(( self.MAX_SCORE-score_point,score_point_obj))
            #Efficient way to pick up N largest score
            heapify(score_list )
            score_book = ScoreBook(
                    scene_key=scene_key, 
                    score_dict=score_dict,
                    score_list=score_list
                )
            self.scores_cache[scene_key] = score_book
        pass

    def pick_space(self, scene_key:str) -> Tuple[int,int]:
        spaces:List[Tuple[int,int]] = self._get_avaialble_spaces(
            scene_key=scene_key, 
            dim=self.statistics.dim)
        #Rolls the dice to switch 
        dice_switch = random()
        if dice_switch < self.min_odds_try_new:
            # 2) randomly pick up a space
            #insert the space into heap
            logger.info(f"randomly pick a point after dice roll {dice_switch}")
            return self._random_space(spaces)
        else:
            #1) get the space of largest score
            return self._get_largest_score(
                scene_key=scene_key,
                spaces=spaces
            )
            
    
    def _get_largest_score(self, scene_key:str,  spaces:List[Tuple[int,int]]) -> Tuple[int, int]:
        if scene_key in self.scores_cache:
            score_list = self.scores_cache[scene_key].score_list
            if len(score_list) > 0:
                logger.info(f"pick most efficient one: {scene_key}")
                return self._translate_coordinate_2_tuple(score_list[0][1].coordinate)
            else:
                logger.info(f"empty statistics {scene_key}, randomly pick one")
                return self._random_space(spaces)
        else:
            logger.info(f"not found any scene {scene_key}, randomly pick one")
            return self._random_space(spaces)

    def _translate_coordinate_2_tuple(self, coordinate:str) -> Tuple[int, int]:
        l = coordinate.split("_")
        return (l[0],l[1])
    def _random_space(self, spaces:List[Tuple[int,int]]) -> Tuple[int,int]:
        return choice(spaces)

    def _get_avaialble_spaces(self, scene_key:str, dim:int) -> List[ Tuple[int, int] ]:
        spaces = []
        for i in range(len(scene_key)):
            if scene_key[i] == "_":
                row = int(i / dim) + 1
                col = int(i % dim) + 1
                spaces.append(
                    (row, col)
                )
        return spaces
        
