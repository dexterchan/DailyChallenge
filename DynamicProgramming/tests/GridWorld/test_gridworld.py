from __future__ import annotations

from GridWorld.model import *
from GridWorld.deterministic import *
from GridWorld.loghelper import get_logger, logging

logger = get_logger(__name__, logging.DEBUG)
opt = Deterministic_Optimizer()
grid = Grid.get_sample_grid()

(policy, values) = opt.optimize(grid=grid)
logger.debug(policy)
logger.debug(values)
