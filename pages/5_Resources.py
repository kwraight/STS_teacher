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
st.write("- Reading list")
st.write("- Non-reading list")


st.write("---")

st.write("## Reading List")

st.write("### Philosophy of Science")

st.write("Overviews:")
st.write("* Philosophy of Science: A Very Short Introduction - _Samir Okasha_")
st.write("    * A good overview in the OUP _Very Short Introduction_ style")
st.write("    * [link](https://tinyurl.com/yb24gol6)")

st.write("- What Is this Thing Called Science? - _Alan Chalmers_")
st.write("  - A more comprehensive overview")
st.write("  - [link](https://tinyurl.com/yb6qfd2b)")

st.write("- Philosophy of Science: A Contemporary Introduction - _Alex Rosenburg & Lee McIntyre_")
st.write("  - Text used in current Philosophy Course")
st.write("  - [link](https://tinyurl.com/y9caxtss)")

st.write("A couple of classics:")
st.write("- Logic of Scientific Discovery - _Karl Popper_")
st.write("  - Popper’s classic work on _Falsificationism_")
st.write("  - [link](https://tinyurl.com/ycxxjdmz)")

st.write("- Structure of Scientific Revolutions - _Thomas Kuhn_")
st.write("  - Kuhn’s classic upset to traditional Philosophy of Science")
st.write("  - [link](https://tinyurl.com/yah8jeb5)")

st.write("### Studies of Science")

st.write("Sociology of Scientific Knowledge:")
st.write("- Scientific knowledge: a sociological analysis - _Barry Barnes, David Bloor & John Henry_")
st.write("  - The case for SSK along with some physics examples")
st.write("  - [link](https://tinyurl.com/ya8ov7dn)")

st.write("- The Mangle of Practice - _Andrew Pickering_")
st.write("  - Focussing on experiments and practice rather than theory and representation")
st.write("  - [link](https://tinyurl.com/ycc4rhln)")

st.write("History:")
st.write("- Leviathan and the Air-pump - _Steven Shapin & Simon Schaffer_")
st.write("  - Describes the rise of experimentalism in Science with Robert Boyle")
st.write("  - [link](https://tinyurl.com/ycpyopdg)")

st.write("Anthropology")
st.write("- Laboratory Life - _Bruno Latour & Steve Woolgar_")
st.write("  - Based on field-work in a biology lab, Latour takes an empirical approach to STS")
st.write("  - [link](https://tinyurl.com/y77gvw8f)")
 
st.write("Philosophy")
st.write("- The Social Construction of What? - _Ian Hacking_")
st.write("  - An analysis of SSK and the Science Wars")
st.write("  - [link](https://tinyurl.com/y83qm84d)")

st.write("### Studies of Physics")

st.write("Quantum Mechanics:")
st.write("- Quantum Mechanics: Historical Contingency and the Copenhagen Hegemony - _James Cushing_")
st.write("  - The story of the advent of QM and the choice of (metaphysical) interpretation")
st.write("  - [link](https://tinyurl.com/yafop3kj)")

st.write("Particles:")
st.write("- How Experiments End - _Peter Galison_")
st.write("  - Studies crucial experimental episodes in particle physics")
st.write("  - [link](https://tinyurl.com/y86gky5s)")

st.write("The Standard Model:")
st.write("- Constructing Quarks: A Sociological History of Particle Physics - _Andrew Pickering_")
st.write("  - Written by a physicist turned sociologist, based on historical record")
st.write("  - Not in the library :(")

st.write("Gravitational Waves:")
st.write("- Gravity's Kiss: The Detection of Gravitational Waves - _Harry Collins_")
st.write("  - Written by a sociologist whose work was embedded with the physicists")
st.write("  - Not in the library :(")


st.write("---")

st.write("## Non-reading list")

st.write("BBC Radio 4's _In Our Time_ episodes")
st.write(" - [Science and Religion](https://www.bbc.co.uk/programmes/p005479y)")
st.write(" - [20th Century Science](https://www.bbc.co.uk/programmes/p005457h)")
st.write(" - [The Scientific Method](https://www.bbc.co.uk/programmes/b01b1ljm)")
st.write(" - [The Scientist](https://www.bbc.co.uk/programmes/p00548jq)")
st.write(" - [Imperial Science](https://www.bbc.co.uk/programmes/p00547b5)")
st.write(" - [Vienna Circle](https://www.bbc.co.uk/programmes/b00lbsj3)")

st.write("How to think About Science")
st.write(" - CBC’s 24 part epic across STS")
st.write(" - [link](https://www.cbc.ca/radio/ideas/how-to-think-about-science-part-1-24-1.2953274)")

st.write("Social Science Bites")
st.write(" - Short introductions to all sorts of sociological studies (STS and more)")
st.write(" - [link](https://player.fm/series/social-science-bites)")

st.write("The Tribes of Science")
st.write(" - Concerning the sub-communities of science")
st.write(" - [link](https://www.bbc.co.uk/programmes/b012xns9/episodes/player)")

st.write("Four Thought")
st.write(" - How images and concepts interact")
st.write(" - [link](https://www.bbc.co.uk/programmes/b0b89nq2)")












