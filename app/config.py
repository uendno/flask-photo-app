import os
from importlib import import_module

env = os.getenv('ENV')
config_name = 'app.cfg.' + env
module = import_module(config_name)
config = module.Config
