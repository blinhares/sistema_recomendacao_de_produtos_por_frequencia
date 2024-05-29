#rodar stream lite sem o comando no terminal
#nao funciona com cx_freeze
import os
import streamlit.web.bootstrap as st_boots
from streamlit import config as _config

MAIN_APP_NAME = "main.py" #nome do arquivo principal

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, MAIN_APP_NAME)

_config.set_option("server.headless", True)
args = []

st_boots.run(filename,
             True, 
             args, # type: ignore
             flag_options={})