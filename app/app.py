import streamlit as st
import pandas as pd
from preprocessing import *

pokemon=pd.read_csv("data/pokemon.csv")

st.write("Pokemon Battle Predictor")
st.selectbox("Pokemon 1",pokemon["Name"])
st.selectbox("Pokemon 2",pokemon["Name"])

st.button("Predict Pokemon")
