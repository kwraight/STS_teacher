import streamlit as st
import pandas as pd
import numpy as np
import os

st.title('Welcome')

st.write("A webApp for STS teaching")

st.write("---")

st.write('Pages:')
pyFiles = [f for f in os.listdir(os.getcwd()+"/pages") if ".py" in f]
pyFiles = sorted(pyFiles)
for e,pf in enumerate(pyFiles,1):
    st.write(f"{e}. {pf.split('_')[-1].split('.')[0]}")

st.write("---")