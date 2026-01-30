# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f"Customize Your Smoothie :balloon: {st.__version__}")
st.write(
  """Choose the fruits that you want in your custom smoothie
  """)

option = st.selectbox(
    "What is your favorite fruit>",
    ("Banana", "Strawberries", "Peaches"),)

st.write("Your favorite fruit is:", option)

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options")
st.dataframe(data=my_dataframe, use_container_width=True)
