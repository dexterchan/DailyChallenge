from .statistics import Statistics


class Epsilon_Greedy:
    WIN_SCORE: int = 2
    DRAW_SCORE: int = 0
    LOSS_SCORE: int = -2

    def __init__(self, statistics: Statistics, min_probability_try_new: float) -> None:
        self.statistics: Statistics = statistics
        self.min_odds_try_new: float = min_probability_try_new

        pass

    def init_scores(self) -> None:
        pass
