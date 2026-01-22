from .level1 import Level_1
from .level2 import Level_2
from .level3 import Level_3
from .level4 import Level_4
from .level5 import Level_5
from .level6 import Level_6
from .level7 import Level_7
from .level8 import Level_8
from .level9 import Level_9
from .level10 import Level_10
from .level11 import Level_11

LEVEL_QUANTITY = 11

__all__ = [f"Level_{i}" for i in range(1, LEVEL_QUANTITY + 1)] + ["LEVEL_QUANTITY"]