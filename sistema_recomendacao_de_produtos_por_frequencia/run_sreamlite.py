#rodar stream lite sem o comando no terminal

import os
import streamlit.web.bootstrap as st_boots
from streamlit import config as _config

MAIN_APP_NAME = "main.py" #nome do arquivo principal

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, MAIN_APP_NAME)

_config.set_option("server.headless", True)
args = []

# streamlit.cli.main_run(filename, args)
st_boots.run(filename,
             True, 
             args, # type: ignore
             flag_options={})