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
st.write("- A brief history")
st.write("- A couple of riddles")
st.write("- Popper & revolutions")


st.write("---")

st.write("## A brief history")


st.write("---")

st.write("## A couple of riddles")


st.write("---")

st.write("## Popper & revolutions")
