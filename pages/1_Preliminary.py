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

prelim_markdown = read_markdown_file(os.getcwd()+"/pages/md_preliminary.md")
st.markdown(prelim_markdown, unsafe_allow_html=True)

st.stop()

sel_matter=st.selectbox("Does it matter?",["Choose","Don't know","Yes","No"])
if sel_matter=="Choose":
    st.stop()
elif sel_matter=="Yes":
    st.write("__Welcome to STS!__")
elif sel_matter=="No":
    st.write("Sit back, relax and enjoy the ride")
elif sel_matter=="Don't know":
    st.write("Carry on")
else:
    st.write("sel_matter error")

st.write("Here are some issues...")
rad_issues=st.radio("Issues:",["Politics","Economics","Society"])
if rad_issues=="Politics":
    st.write("Science has a position of _authority_ in society. Is it justified?")
elif rad_issues=="Economics":
    st.write("Science costs money. Investment comes from governments and private companies. Does this affect the output?")
elif rad_issues=="Society":
    st.write("Science affects all society. Should it seek _permission_, or _trust_ from (all) citizens?")
else:
    st.write("rad_issues error")

sel_def=st.selectbox("Condition definitions",["Select","Necessary","Sufficient","Equivalence","Family Resemblence"])
if sel_def=="Select":
    st.stop()
elif sel_def=="Necessary":
    st.write("_Necessary Condition_: essential requirement")
    st.write(" * e.g. Breaking eggs is a _necessary condition_ to make omelettes")
    st.write(" * Is there a property (set) of science that must be present?")
elif sel_def=="Sufficient":
    st.write("_Sufficient Condition_: enough on its own")
    st.write(" * e.g. Smoke is a sufficient condition to conclude fire")
    st.write(" * Is there unique property (set) of science?")
elif sel_def=="Equivalence":
    st.write("_Equivalence Condition_: A Necessary and Sufficient condition")
    st.write(" * e.g. A bachelor is an unmarried male")
    st.write(" * Is there a uniquely definitive property (set)?")
elif sel_def=="Family Resemblence":
    st.write("_Family Resemblance_: overlapping groups without universal property (set)")
    st.write(" * e.g. \"game\" is not uniquely defined - many examples without _common_ characteristic")
    st.write(" * What are the overlapping of sets?")
else:
    st.write("sel_def error")
