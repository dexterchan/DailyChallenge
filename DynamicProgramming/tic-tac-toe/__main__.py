from __future__ import annotations
from .tic_tac_toe import *
if __name__ == "__main__":
    tic_tac_toe_game: Tic_Tac_Toe_Game = Tic_Tac_Toe_Game(
        dimension=3
    )
    tic_tac_toe_game.play()
