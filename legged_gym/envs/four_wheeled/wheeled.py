from legged_gym import LEGGED_GYM_ROOT_DIR, envs
from time import time
from warnings import WarningMessage
import numpy as np
import os

from isaacgym import gymtorch, gymapi, gymutil

import torch
from  torch import Tensor
from typing import Tuple,Dict

from legged_gym.envs import LeggedRobot
from legged_gym import LEGGED_GYM_ROOT_DIR
from legged_gym.envs.base.base_task import BaseTask
from legged_gym.utils.terrain import Terrain
from legged_gym.utils.math import quat_apply_yaw, wrap_to_pi, torch_rand_sqrt_float
from legged_gym.utils.helpers import class_to_dict
from .four_wheeled_config import FourWheeledCfg, FourWheeledCfgPPO
class Wheeled(LeggedRobot):
    cfg : FourWheeledCfg
    pass







