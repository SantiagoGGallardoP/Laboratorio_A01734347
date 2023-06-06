# -*- coding: utf-8 -*-
"""ActividadIntegradora_A01734347

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GSBYC61F8TF8Jj3M_5xzWGYdo5sVv46A
"""

import streamlit as st
import pandas as pd

st.title("Police Incident Reports from 2018 to 2020 ins San Francisco")

df= pd.read_csv("https://drive.google.com/file/d/11oLcKiW8SgCOp3tGiQCYuRG7pLL_J-Zf/view?usp=drive_link")

st.markdown("The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.")

mapa = df[df["City"] == "San Francisco"].copy()
mapa=mapa.dropna()
st.map(mapa.astype(int))
