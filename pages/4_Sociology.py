import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
import numpy as np

import os
from pathlib import Path
import json
import subprocess
         
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

fileName=os.path.basename(__file__).split('_')[-1].split('.')[0]
st.title(fileName)

if st.checkbox("View disclaimer"):
    st.write("## :warning: :exclamation: Disclaimer :exclamation: :warning:")

    st.write("### WARNING")
    st.write("To tell this story I have omitted many details. \
            Almost everything mentioned here is truncated and \
            much more can and has been said.")
    st.write("__Other views are available__")


st.write("---")

prelim_markdown = read_markdown_file(os.getcwd()+"/pages/md_sociology.md")
st.markdown(prelim_markdown, unsafe_allow_html=True)

st.stop()