# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(f"Customize Your Smoothie :balloon: {st.__version__}")
st.write(
  """Choose the fruits that you want in your custom smoothie
  """)

option = st.selectbox(
    "What is your favorite fruit>",
    ("Banana", "Strawberries", "Peaches"),)

st.write("Your favorite fruit is:", option)

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options")
st.dataframe(data=my_dataframe, use_container_width=True)
