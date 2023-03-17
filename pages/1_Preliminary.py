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
st.write("- Disclaimer")
st.write("- Scientific Images")


st.write("---")

st.write("## Disclaimer")

st.write("### WARNING")
st.write("To tell this story I have omitted many details. \
         Almost everything mentioned here is truncated and \
         much more can and has been said.")
st.write("__Other views are available__")


st.write("---")

st.write("## Scientific Images")

