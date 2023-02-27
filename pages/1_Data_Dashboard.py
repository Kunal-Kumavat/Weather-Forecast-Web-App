import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "weather forecast.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "Weather Forecasting.csv")

st.title("Dashboard")
st.subheader("Weather Forecasting Dataset")

options = st.selectbox('Please Select',["Dataset","Dashboard"])

if options == "Dataset":
    df = pd.read_csv(DATA_PATH)
    st.dataframe(df)
elif options == "Dashboard":
    img = image.imread(IMAGE_PATH)
    st.image(img)
