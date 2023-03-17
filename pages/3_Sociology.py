import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
import numpy as np

import os
import json
import subprocess

fileName=os.path.basename(__file__).split('_')[-1].split('.')[0]
st.title(fileName)

st.write('### Contents')
st.write("- Kuhn")
st.write("- Sociology of Scientific Knowledge")
st.write("- Latour")
st.write("- Pickering")


st.write("---")

st.write("## Kuhn")


st.write("---")

st.write("## Sociology of Scientific Knowledge")


st.write("---")

st.write("## Latour")


st.write("---")

st.write("## Pickering")
