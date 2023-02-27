import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

socials  = ["LinkedIn", "Github", "GMail"]
linkedin = "https://www.linkedin.com/in/kunal-kumavat-7a7844200"
github   = "https://github.com/kunal-kumavat"
mail     = "kumavatkunal1@gmail.com"

with st.expander(label='Connect with me',expanded=True):
	a = st.selectbox("Socials", socials)
	if a =="LinkedIn":
		st.write(linkedin)
	elif a =="Github":
		st.write(github)
	elif a=="GMail":
		st.write(mail)

btn_click = st.button("Follow For More")

if btn_click == True:
    st.subheader("Thank You... :smile:")
    st.balloons()
