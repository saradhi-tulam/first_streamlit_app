
import streamlit

streamlit.title("hello, how are you?")

streamlit.header("header test")

streamlit.text("text test")

streamlit.header('🍌🥭  Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Display the table on the page.

my_fruit_list = my_fruit_list.set_index('Fruit')
                                        
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


# donvert to pandas readable format 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# create dataframe
streamlit.dataframe(fruityvice_normalized)
