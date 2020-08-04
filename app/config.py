import os
from importlib import import_module

list_env = ('dev', 'test', 'prod')

env = os.getenv('ENV')
if env in list_env:
    config_name = 'app.cfg.' + env
    module = import_module(config_name)
    config = module.Config
else:
    raise RuntimeError("Value for environment variable ENV is not valid")
