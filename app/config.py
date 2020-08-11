import os
from importlib import import_module

from app.constants.error_message import INVALID_ENVIRONMENT_VARIABLE

VALID_ENVS = ('dev', 'test', 'prod')

env = os.getenv('ENV')
if env not in VALID_ENVS:
    raise RuntimeError(INVALID_ENVIRONMENT_VARIABLE)

config_name = 'app.cfg.' + env
module = import_module(config_name)
config = module.Config
