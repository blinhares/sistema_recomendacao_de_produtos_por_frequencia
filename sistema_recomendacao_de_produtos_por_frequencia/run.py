import streamlit
import streamlit.runtime.scriptrunner.magic_funcs
import streamlit.web.cli as stcli
import os, sys

# Importar as Bibliotecas do Arquivo main.py
import altair as alt
import streamlit as st


def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("main.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())