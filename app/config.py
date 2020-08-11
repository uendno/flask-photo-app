import os
from importlib import import_module

valid_envs = ('dev', 'test', 'prod')

env = os.getenv('ENV')
if env in valid_envs:
    config_name = 'app.cfg.' + env
    module = import_module(config_name)
    config = module.Config
else:
    raise RuntimeError('Value for environment variable ENV is not valid')
